import unittest

from Model.sqlconn_class import SQLconn
from Model.login_class import Login
from Test.test_Validator import *
from Test.Validator import *

# Test scenarie: Dummy data oprettes, og nogle requests bliver lavet og sendt til admincheck, nogle bliver accepteret
# og andre bliver afvist. De forskellige dummy-requests kommer til at have forskellige længder og datatyper for at teste.

class database_test(unittest.TestCase):
    def test_sql_tableCreator(self):
        self.db = SQLconn()
        self.db.create_all_tables()
        self.db.mycursor.execute("INSERT INTO `lectures` VALUES (1000,'TestLecture','AddressShort','2022-05-02','00:00','24:00',0),(1001,'TestLecture','AddressTest','2022-04-04','08:00','10:00',0);")
        self.db.mycursor.execute("SELECT * FROM lectures")
        dblecture = self.db.mycursor.fetchall()
        assert(dblecture[-1][0] == 1001)
        assert (dblecture[-2][0] == 1000)
        self.db.mydb.commit()
        print('Dummy data insertet')

    def test_employees(self):
        """Tester om brugerne er oprettet, og om at alle brugernes brugernavne lever op til formatet"""
        self.db = SQLconn()
        self.db.create_employees()
        for user in Login.all_users:
            assert(len(user.get_userID()) == 6)
        for user in Login.all_users:
            assert(type(int(user.get_userID()[3:])) == int)

    def test_requests(self):
        """Send en anmodning til admincheck, og opdater lecture ud fra den"""
        self.db = SQLconn()
        self.db.mycursor.execute("INSERT INTO admincheck (courseID, course, room, `date`, timefrom, timeuntil) VALUES (1000,'TestLecture','NewAddressShort','2022-05-02','00:00','24:00'),(1001,'TestLecture','NewAddressTest','2022-04-04','08:00','10:00');")
        self.db.mycursor.execute("SELECT * FROM admincheck")
        dbrequest = self.db.mycursor.fetchall()
        assert(dbrequest[-1][0] == 1001)
        assert(dbrequest[-2][0] == 1000)
        dbrequest1000 = dbrequest[-1]
        dbrequest1001 = dbrequest[-2]
        self.db.mycursor.execute(f"UPDATE lectures SET room = '{dbrequest1000[2]}', date = '{dbrequest1000[3]}', timefrom = '{dbrequest1000[4]}', timeuntil = '{dbrequest1000[5]}' WHERE courseID = '{dbrequest1000[0]}'")
        self.db.mycursor.execute(f"UPDATE lectures SET room = '{dbrequest1001[2]}', date = '{dbrequest1001[3]}', timefrom = '{dbrequest1001[4]}', timeuntil = '{dbrequest1001[5]}' WHERE courseID = '{dbrequest1001[0]}'")
        self.db.mycursor.execute("SELECT * FROM lectures")
        dblecture = self.db.mycursor.fetchall()
        assert(dbrequest1000[0:6] == dblecture[-1][0:6])
        assert(dbrequest1001[0:6] == dblecture[-2][0:6])

    def test_tear_down(self):
        """Slet test data"""
        self.db = SQLconn()
        self.db.mycursor.execute("delete from admincheck WHERE courseID = 1000")
        self.db.mycursor.execute("delete from admincheck WHERE courseID = 1001")
        self.db.mycursor.execute("delete from lectures WHERE courseID = 1000")
        self.db.mycursor.execute("delete from lectures WHERE courseID = 1001")
        self.db.mycursor.execute("SELECT * FROM lectures")
        dblecture = self.db.mycursor.fetchall()
        assert(dblecture[-1][-1] != 1001)
        assert(dblecture[-1][-2] != 1000)
        self.db.mycursor.execute("SELECT * FROM admincheck")
        dbrequest = self.db.mycursor.fetchall()
        assert(dbrequest[-1][-1] != 1001)
        assert(dbrequest[-1][-2] != 1000)
        print('Dummy data deleted')

if __name__ == '__main__':
    unittest.main()
