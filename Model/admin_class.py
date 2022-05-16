from Model.person_class import Person

class Admin(Person):
    """Info om ansette kursusledere"""
    def __init__(self, name, lastname, employeeID):
        self.__name = name
        self.__lastname = lastname
        self.__employeeID = employeeID
        self.initials = f"{self.__name[0]}. {self.__lastname}"
        self.role = "admin"

    def set_name(self, new_name): self.__name = new_name

    def get_name(self): return self.__name

    def set_lastname(self, new_lastname): self.__lastname = new_lastname

    def get_lastname(self): return self.__lastname

    def set_employeeID(self, new_employeeID): self.__employeeID = new_employeeID

    def get_employeeID(self): return self.__employeeID
