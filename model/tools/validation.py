import re
from datetime import datetime,date

def t_id_validator(value):
    pass

def ticket_code_validator(ticket_code):
    if not(type(ticket_code) == int and 0 < ticket_code ):
        raise ValueError("Invalid ticket code")

def source_validator(source):
    pass

def destination_validator(destination):
    pass

def airline_validator(airline):
    pass

def start_date_validator(start_date):
    try:
        if type(start_date) == str:
            datetime.strptime(start_date, '%d/%m/%Y')
        elif type(start_date) == date:
            pass
        else:
            raise ValueError("Invalid start date")
        return True
    except Exception as e:
        print(f"{e} خطا دارد ")


def end_date_validator(end_date):
    try:
        if type(end_date) == str:
            datetime.strptime(end_date, '%d/%m/%Y')
        elif type(end_date) == date:
            pass
        else:
            raise ValueError("Invalid end date")
        return True
    except Exception as e:
        print(f"{e} خطا دارد ")


def price_validator(price):
    if not (type(price) == int and 0 < price):
        raise ValueError("Invalid price")


def seat_no_validator(seat_no):
    if not (re.match(r"^\d{3}$", seat_no, re.I) and (1 < int(seat_no) < 232)):
        raise ValueError("Invalid Seat No")

def sold_validator(sold):
    pass



class Validation:
    def person_validator(self, person):
        pass

    def ticket_validator(self, ticket):
        pass