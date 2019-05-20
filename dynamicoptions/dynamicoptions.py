"""
DynamicOptions:
load options for select fields from external sources such as SQL query and
JSON REST webservice
"""


from trac.core import Component, implements, ExtensionPoint, ComponentManager
from trac.ticket.api import TicketSystem
from api import ITicketFieldOptionsSource


def process_field(env, field, ts):
    f_name = field['name']
    config = ts.ticket_custom_section
    options_desc = config.get(f_name + '.options')

    env.log.warn("Options: %s", options_desc)
    # if options_desc == 'sql' or f_name == 'setor':
    options_mgr = DynamicOptionsManager(ts.compmgr)
    options_mgr.process(options_desc, field)
    # if options_desc == 'sql':
    #     base_sql = config.get(f_name + '.options.query')
    #     env.log.warn("base_sql %s", base_sql)
    #     field['options'] = [x[0] for x in env.db_query(base_sql % '')]


def gen_get_fields(ticket_system_get_fields):
    # env.log.warn("gen_get_fields")
    # env.log.warn("Env: %s", env)
    def do_get_fields(ticket_system):
        ticket_system.log.warn("do_get_fields")
        fields = ticket_system_get_fields(ticket_system)
        for field in fields:
            process_field(ticket_system.env, field, ticket_system)

        return fields

    return do_get_fields


injected_dynamic_options = False


def inject_dynamic_options():
    global injected_dynamic_options
    if not injected_dynamic_options:
        TicketSystem.get_custom_fields = gen_get_fields(TicketSystem.get_custom_fields)
        injected_dynamic_options = True

class DynamicOptionsManager(Component):
    sources = ExtensionPoint(ITicketFieldOptionsSource)

    def process(self, options_desc, field):
        for source in self.sources:
            self.env.log.warn("Using source %s", source)

            if source.can_handle(options_desc):
                field['options'] = source.get_all_options(field)