class TicketDa:
    def save(self, ticket):
        print("Ticket saved to db", ticket.id, ticket.code, ticket.source, ticket.destination, ticket.seat_number)
    def edit(self, ticket):
        pass
    def remove(self, ticket):
        pass
    def find_all(self):
        pass
    def find_by_id(self, id_):
        pass
    def find_by_code(self, id_, code):
        pass
