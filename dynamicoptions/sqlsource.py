from trac.config import ConfigSection
from trac.core import Component, implements
from api import ITicketFieldOptionsSource

""" Example utilization
origem = select
origem.format = plain
origem.label = Origem
origem.options = sql
origem.options.query = SELECT DISTINCT value FROM ticket_custom WHERE name = 'origem'
origem.order = 0
origem.value =
"""
class SQLTicketOptionSource(Component):
    implements(ITicketFieldOptionsSource)

    ticket_custom_section = ConfigSection('ticket-custom',
        """In this section, you can define additional fields for tickets. See
        TracTicketsCustomFields for more details.""")

    def can_handle(self, kind):
        return kind.lower() == 'sql'

    def get_all_options(self, field):
        config = self.ticket_custom_section

        f_name = field['name']
        base_sql = config.get(f_name + '.options.query')

        self.env.log.warn("base_sql %s", base_sql)

        return [x[0] for x in self.env.db_query(base_sql)]