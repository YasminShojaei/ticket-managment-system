
import re
from datetime import datetime

def t_id_validator(value):
    pass
def ticket_code_validator(ticket_code):
    if not(type(ticket_code) == int and 0 < ticket_code ):
        raise ValueError("Invalid ticket code")
def source_validator(so):
    pass
def destination_validator(de):
    pass
def airline_validator(airline):
    pass
def start_date_validator(start_date):
    pass
def end_date_validator(value):
    pass
def price_validator(value):
    pass
def seat_no_validator(value):
    pass

class Validation:
    def person_validator(self, person):
        pass

    def ticket_validator(self, ticket):
        pass