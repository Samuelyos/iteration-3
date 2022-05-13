from Model.courseleader_class import Courseleader
from Model.admin_class import Admin

class Person:
    """En klasse brugt til at indeholder de grundlæggende attributter for """

    def __init__(self, name, lastname, employeeID, role):
        self.__name = name
        self.__lastname = lastname
        self.__employeeID = employeeID
        self.initials = f"{self.__name[0]}. {self.__lastname}"
        self.role = role
        self.new_person()

    def new_person(self):
        if self.role == 'admin':
            return Admin(self.__name, self.__lastname, self.__employeeID)

        elif self.role == 'courseleader':
            return Courseleader(self.__name, self.__lastname, self.__employeeID)

