import mysql.connector


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


#db = SQLconn()
#db.create_all_tables()
