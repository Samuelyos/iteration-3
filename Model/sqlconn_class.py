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

    def create_tables(self):
        pass