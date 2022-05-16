class Person:
    """En klasse brugt til at indeholder de grundlæggende attributter for """

    def __init__(self, name, lastname, employeeID):
        self.__name = name
        self.__lastname = lastname
        self.__employeeID = employeeID
        self.initials = f"{self.__name[0]}. {self.__lastname}"




