import pickle
import os

file_name = "ticket.dat"

class TicketManager:
    def __init__(self):
        if not os.path.exists(file_name):
            with open(file_name, "wb") as f:
                pickle.dump([], f)

    def read_all(self):
        with open(file_name, "rb") as f:
            return pickle.load(f)

    def write_all(self, data_list):
        with open(file_name, "wb") as f:
            pickle.dump(data_list, f)

    def save(self, ticket):
        data = self.read_all()
        data.append(ticket)
        self.write_all(data)

    def edit(self, ticket):
        data = self.read_all()
        for i, t in enumerate(data):
            if t.code == ticket.code:
                data[i] = ticket
                self.write_all(data)
                return
        raise Exception("Ticket not found")

    def remove(self, code):
        data = self.read_all()
        new_data = [t for t in data if t.code != code]
        if len(data) == len(new_data):
            raise Exception("Ticket not found")
        self.write_all(new_data)
