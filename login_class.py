class Login:
    """Klasse der bruges til at identificere brugere af sKUma, både ift til kodeord og deres rolle (admin eller andet)"""
    all_users = []
    def __init__(self, person, password):
        self.__userID = person.get_employeeID()
        self.__role = person.role
        self.__password = password
        self.__userTag = f'{person.get_name()} {person.get_lastname()}'
        self.all_users.append(self)

    def __repr__(self):
        return f'{self.get_userID()}'

    def set_userID(self, new_userID): self.__userID = new_userID

    def get_userID(self): return self.__userID

    def set_role(self, new_role): self.__role = new_role

    def get_role(self): return self.__role

    def set_password(self, new_password): self.__password = new_password

    def get_password(self): return self.__password

    def set_userTag(self, new_userTag): self.__userTag = new_userTag

    def get_userTag(self): return self.__userTag
