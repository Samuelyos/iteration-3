class classroom:
    """Info om lokaler"""
    def __init__(self, building, floor, roomNr, capacity, address):
        self.__building = building
        self.__floor = floor
        self.__roomNr = roomNr
        self.__capacity = capacity
        self.__address = address
        # RoomID er en forkortet udgave af lokalets info, som den vil blive repræsenteret som attribut i andre klasser.
        self.__roomID = f'{self.__building}, {str(self.__floor)}, {self.__roomNr}'

    #Getters og setters. Set roomID er undtaget

    def get_building(self): return self.__building

    def set_building(self, new_building): self.__building = new_building

    def get_floor(self): return self.__floor

    def set_floor(self, new_floor): self.__floor = new_floor

    def get_roomNr(self): return self.__roomNr

    def set_roomNr(self, new_roomNr): self.__roomNr = new_roomNr

    def get_capacity(self): return self.__capacity

    def set_capacity(self, new_capacity): self.__capacity = new_capacity

    def get_address(self): return self.__address

    def set_address(self, new_address): self.__address = new_address

    def get_roomID(self): return self.__roomID

    # Hvordan vores objekter bliver repræsenteret som string.
    def __str__(self):
        return f"{self.__roomID}\nat {self.__address}"

lokale1 = classroom('HCØ', 2, '103A',22, 'Universitetsparken 1')

print(lokale1)