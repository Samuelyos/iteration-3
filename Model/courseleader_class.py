from Model.person_class import Person

class Courseleader(Person):
    """Info om ansette kursusledere"""
    def __init__(self, name, lastname, employeeID):
        self.__name = name
        self.__lastname = lastname
        self.__employeeID = employeeID
        self.role = "courseleader"
        self.initials = f"{self.__name[0]}{self.__lastname[0]}"
        self.courselist = []

    def set_name(self, new_name): self.__name = new_name

    def get_name(self): return self.__name

    def set_lastname(self, new_lastname): self.__lastname = new_lastname

    def get_lastname(self): return self.__lastname

    def set_employeeID(self, new_employeeID): self.__employeeID = new_employeeID

    def get_employeeID(self): return self.__employeeID

    # metoder til at fjerne eller tilføje kurser til kursuslederens liste over kurser

    def add_course(self, new_course):
        self.courselist.append(new_course)
        return print(f'{new_course} is added to courses for {self.__name}')

    def remove_course(self, old_course):
        if old_course in self.courselist:
            self.courselist.pop(old_course)
            print(f'{old_course} is removed')
        else:
            print(f'Course is not in list')

    def __str__(self):
        return f'{self.initials}: {self.get_name()} {self.get_lastname()}'