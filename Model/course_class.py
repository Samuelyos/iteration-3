class Course:
    """Klasse for hele kurser"""
    all_list = []

    def __init__(self, courseName, courseLeader, faculty):
        self.__courseName = courseName
        self.__courseLeader = courseLeader
        self.__faculty = faculty

        # Subcourse er de lektionstyper der kan forekomme i et kursus, fx forelæsning, SAU, cafetime, øvelsestime etc
        self.subCourse = []
        self.all_list.append(self)

    # Følgende metoder er getters og setters som kan ændre og kalde på objekter (lektioners) attributter

    def get_courseName(self):
        return self.__courseName

    def set_courseName(self, new_courseName):
        self.__courseName = new_courseName

    def get_courseLeader(self):
        return self.__courseLeader

    def set_courseLeader(self, new_courseLeader):
        self.__courseLeader = new_courseLeader

    def get_faculty(self):
        return self.__faculty

    def set_faculty(self, new_faculty):
        self.__faculty = new_faculty

    def add_subcourse(self, new_sub):
        self.subCourse.append(new_sub)

    def remove_subcourse(self, sub_name):
        if sub_name in self.subCourse:
            self.subCourse.pop(sub_name)
        else:
            print(f"There is no subcourse with this name, please check spelling or view list of subs")

    def view_subs(self):
        """Viser alle typer moduler der kan forekomme i et kursus"""
        print("Types of lectures in this course:")
        for subs in self.subCourse:
            print(f"{self.get_courseName()} - {subs}")

    # Hvordan vores objekter bliver repræsenteret som string.
    def __str__(self):
        return f" "


syst = Course("Systemudvikling", "Hugo", "Sci")
syst.add_subcourse("prog. ex")
syst.add_subcourse("theo. ex")
syst.add_subcourse("forelæsning")
syst.view_subs()
