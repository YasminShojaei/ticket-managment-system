class PersonDa:
    def save(self, person):
        print("Ticket saved to db", person.id, person.name, person.family)
    def edit(self, person):
        pass
    def remove(self, person):
        pass
    def find_all(self):
        pass
    def find_by_id(self, id_):
        pass
    def find_by_code(self, id_, name, family):
        pass
