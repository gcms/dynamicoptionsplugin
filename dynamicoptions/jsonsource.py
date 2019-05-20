import urllib
import json

from jsonpath_ng import jsonpath, parse
# sudo easy_install jsonpath-ng

from trac.config import ConfigSection
from trac.core import Component, implements
from api import ITicketFieldOptionsSource

""" Example utilization
setor = select
setor.format = plain
setor.label = Setor
setor.options = json
setor.options.json.url = http://10.239.20.202:8090/resources/centroCusto?q=
setor.options.json.xpath = items[*].nome
setor.order = 0
setor.value =
"""
class JSONTicketOptionSource(Component):
    implements(ITicketFieldOptionsSource)

    ticket_custom_section = ConfigSection('ticket-custom',
        """In this section, you can define additional fields for tickets. See
        TracTicketsCustomFields for more details.""")

    def can_handle(self, kind):
        return kind.lower() == 'json'

    def get_all_options(self, field):
        config = self.ticket_custom_section

        f_name = field['name']
        url = config.get(f_name + '.options.json.url')

        response = urllib.urlopen(url)
        data = json.loads(response.read())

        xpath = config.get(f_name + '.options.json.xpath')
        if (xpath):
            data = [match.value for match in parse(xpath).find(data)]
        else:
            data = [x['nome'] for x in data['items']]

        return [("%s" % x) for x in data]