from model.data_acsess.ticket_manager import TicketManager

class TicketBl:
    def __init__(self):
        self.manager = TicketManager()

    def get_all(self):
        return self.manager.read_all()

    def save(self, ticket):
        self.manager.save(ticket)

    def edit(self, ticket):
        self.manager.edit(ticket)

    def remove(self, t_id):
        self.manager.remove(t_id)


