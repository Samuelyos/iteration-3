import mysql.connector
from Model.person_class import Person
from Model.courseleader_class import Courseleader
from Model.admin_class import Admin
from Model.login_class import Login


class SQLconn:
    """Klasse for metoder der kan oprette forbindelse til databasen og bruge dml"""

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="mysql-db.caprover.diplomportal.dk",
            user="s206026",
            password="oViFSGqnHflEFAA0ETNw1",
            database="s206026")
        self.mycursor = self.mydb.cursor()

    def create_tables(self, filename):
        """Opretter alle de nødvendige tabeller for at eksekvere Use Case, via eksterne SQL - scripts"""
        # Læs og gem SQL script fra kommando til kommando, ved at splitte ved semikolon
        temptable = open(filename, 'r')
        sqlFile = temptable.read()
        temptable.close()
        sqlCommands = sqlFile.split(';')

        # Loop der eksekvere hver kommando, for at oprette en given tabel
        for command in sqlCommands:
            self.mycursor.execute(command)

    def create_all_tables(self):
        """Bruger den tidligere metode til at oprette alle tabellerne"""
        self.create_tables('../Persistence/ERdiagram/s206026_admin.sql')
        self.create_tables('../Persistence/ERdiagram/s206026_admincheck.sql')
        self.create_tables('../Persistence/ERdiagram/s206026_classrooms.sql')
        self.create_tables('../Persistence/ERdiagram/s206026_courseLeader.sql')
        self.create_tables('../Persistence/ERdiagram/s206026_courses.sql')
        self.create_tables('../Persistence/ERdiagram/s206026_lectures.sql')
        self.create_tables('../Persistence/ERdiagram/s206026_Persons.sql')
        self.create_tables('../Persistence/ERdiagram/s206026_Login.sql')
        self.create_tables('../Persistence/ERdiagram/s206026_admin_has_admincheck.sql')

        print('All tables created')

    def create_employees(self):
        """Indlæser Persons table og skaber klasser der automatisk fordeler dem i klasser"""

        self.mycursor.execute("SELECT * FROM Persons")
        all_employees = self.mycursor.fetchall()
        employee_list = []

        # Loop der skaber instances ud fra databasen
        for i in all_employees:
            employee_list.append(Person(i[0], i[1], i[2], i[3]))

        for i in employee_list:
            if i.get_role() == "courseleader":
                Login((Courseleader(i.get_name(), i.get_lastname(), i.get_employeeID())), "password")
            if i.get_role() == "admin":
                Login((Admin(i.get_name(), i.get_lastname(), i.get_employeeID())), "password")



#db = SQLconn()
#db.create_all_tables()
#db.create_employees()

#INSERT INTO `admincheck` VALUES (100,'Pathology.SAU','Ejner Aud.','2022-05-02','00:00','00:00',NULL,154),(100,'Pathology.SAU','Ejner Aud.','2022-05-02','00:00','00:00',NULL,155),(100,'Pathology.SAU','Ejner Aud.','2022-05-02','00:00','00:00',NULL,156),(100,'Pathology.SAU','Ejner Aud.','2022-05-02','00:00','00:00',NULL,158),(100,'Pathology.SAU','Ejner Aud.','2022-05-02','00:00','00:00',NULL,160),(100,'Pathology.SAU','Ejner Aud.','2022-05-02','00:00','00:00',NULL,162),(100,'Pathology.SAU','Ejner Aud.','2022-05-02','00:00','00:00',NULL,164),(103,'SSKS','DTUB-X2.70','2022-05-02','16:00','18:00',NULL,165);
