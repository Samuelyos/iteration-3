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
        self.create_tables('../Persistence/createTablesSQL/s206026_admin.sql')
        self.create_tables('../Persistence/createTablesSQL/s206026_admincheck.sql')
        self.create_tables('../Persistence/createTablesSQL/s206026_classrooms.sql')
        self.create_tables('../Persistence/createTablesSQL/s206026_courseLeader.sql')
        self.create_tables('../Persistence/createTablesSQL/s206026_courses.sql')
        self.create_tables('../Persistence/createTablesSQL/s206026_lectures.sql')
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

db = SQLconn()
#db.create_all_tables()
db.create_employees()
