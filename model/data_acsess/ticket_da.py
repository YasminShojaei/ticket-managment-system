class TicketDa:
    def save(self, ticket):
        print("Ticket saved to db", ticket.t_id, ticket.ticket_code, ticket.source, ticket.destination, ticket.seat_number)
    def edit(self, ticket):
        pass
    def remove(self, ticket):
        pass
    def reset(self,ticket):
        pass
    def find_all(self):
        pass
    def find_by_t_id(self, id_):
        pass
    def find_by_ticket_code(self, id_, code):
        pass
