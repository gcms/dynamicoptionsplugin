from trac.core import Interface


class ITicketFieldOptionsSource(Interface):
    def can_handle(self, kind):
        "Should return if it can handle this kind of options"

    def get_all_options(self, field):
        """Should return the list of available options"""