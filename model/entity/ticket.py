from model.tools.validation import *


# from view.ticket_view import ticket_code, source


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

    def __repr__(self):
        return (self.t_id, self.ticket_code, self.source, self.destination, self.airline, self.start_date,
                self.end_date, self.price)

    def to_tuple(self):
        return (
            self.t_id, self.ticket_code, self.source, self.destination, self.airline, self.start_date, self.end_date,
            self.price, self.seat_no)

    # def validate(self):
    #     validator = Validation()
    #     return validator.ticket_validator(self)

    @property
    def t_id(self):
        return self._t_id

    @t_id.setter
    def t_id(self, value):
        t_id_validator(value)
        self._t_id = value

    @property
    def ticket_code(self):
        return self._ticket_code

    @ticket_code.setter
    def ticket_code(self, value):
        ticket_code_validator(value)
        self._ticket_code = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        source_validator(value)
        self._source = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        destination_validator(value)
        self._destination = value

    @property
    def airline(self):
        return self._airline

    @airline.setter
    def airline(self, value):
        airline_validator(value)
        self._airline = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        start_date_validator(value)
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        end_date_validator(value)
        self._end_date = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        price_validator(value)
        self._price = value

    @property
    def seat_no(self):
        return self._seat_no

    @seat_no.setter
    def seat_no(self, value):
        seat_no_validator(value)
        self._seat_no = value
