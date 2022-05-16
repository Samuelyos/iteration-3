class Person:
    """En klasse brugt til at indeholder de grundlæggende attributter for """

    def __init__(self, name, lastname, employeeID, role):
        self.__name = name
        self.__lastname = lastname
        self.__employeeID = employeeID
        self.__role = role
        self.initials = f"{self.__name[0]}. {self.__lastname}"

    def __repr__(self):
        return f"{self.__employeeID}"

    def get_role(self):
        return self.__role

    def set_role(self, new_role):
        self.__role = new_role

    def set_name(self, new_name): self.__name = new_name

    def get_name(self): return self.__name

    def set_lastname(self, new_lastname): self.__lastname = new_lastname

    def get_lastname(self): return self.__lastname

    def set_employeeID(self, new_employeeID): self.__employeeID = new_employeeID

    def get_employeeID(self): return self.__employeeID
