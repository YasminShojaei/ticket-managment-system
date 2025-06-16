from model.tools.validation import Validation

class Ticket:
    def __init__(self, id_, code, source, destination, airline, start_time, end_time, price, seat_number):
        self.id_ = id_
        self.code = code
        self.source = source
        self.destination = destination
        self.airline = airline
        self.start_time = start_time
        self.end_time = end_time
        self.price = price
        self.seat_number = seat_number

    def to_tuple(self):
        return (self.id_, self.code, self.source, self.destination, self.airline, self.start_time, self.end_time, self.price, self.seat_number)

    def validate(self):
        validator = Validation()
        return validator.ticket_validator(self)
