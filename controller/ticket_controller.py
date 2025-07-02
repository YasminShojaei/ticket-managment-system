
from model.business_logic.ticket_bl import TicketBl
from model.data_acsess.ticket_manager import *

class TicketController:
    def __init__(self):
        self.ticket_bl = TicketBl()

    def get_all(self):
        return self.ticket_bl.get_all()

    def save(self, ticket):
        try:
            ticket.validate()
            self.ticket_bl.save(ticket)
            return "Ticket saved successfully"
        except ValueError as ve:
            return f"Validation error: {ve}"
        except Exception as e:
            return f"An error occurred: {e}"

    def edit(self, ticket):
        try:
            ticket.validate()
            self.ticket_bl.edit(ticket)
            return "Ticket updated successfully"
        except ValueError as ve:
            return f"Validation error: {ve}"
        except Exception as e:
            return f"An error occurred: {e}"

    def remove(self, code):
        try:
            self.ticket_bl.remove(code)
            return "Ticket removed successfully"
        except Exception as e:
            return f"An error occurred: {e}"