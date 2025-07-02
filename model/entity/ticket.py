from model.tools.validation import Validation

class Ticket:
    def __init__(self, t_id, ticket_code, source, destination, airline, start_date, end_date, price, seat_no):
        self.t_id = t_id
        self.ticket_code = ticket_code
        self.source = source
        self.destination = destination
        self.airline = airline
        self.start_date = start_date
        self.end_date = end_date
        self.price = price
        self.seat_no = seat_no

    def to_tuple(self):
        return (self.t_id, self.ticket_code, self.source, self.destination, self.airline, self.start_date, self.end_date, self.price, self.seat_no)

    def validate(self):
        validator = Validation()
        return validator.ticket_validator(self)
