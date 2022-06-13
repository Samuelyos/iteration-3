from PyQt6 import QtWidgets, uic
from Model.sqlconn_class import SQLconn
from Controller.LoginGUI import LoginGUI


class FirstTimeGUI(QtWidgets.QDialog):
    """Klasse for selve ændring af lektioner GUI"""

    def __init__(self):  #
        super(FirstTimeGUI, self).__init__()
        uic.loadUi('../View/Firsttime_GUI.ui', self)

        # Her defineres mange af de variable der bliver brugt senere i koden
        self.exitpush.clicked.connect(self.exit_pressed)
        self.databasepush.clicked.connect(self.sql_pressed)
        self.login_push.clicked.connect(self.login_pressed)
        self.databasesql = SQLconn()
        self.i = 0
        self.show()

    def login_pressed(self):
        """Lukker vinudet, og åbne Login GUI i stedet"""
        self.close()
        self.loginGUI = LoginGUI()
        self.loginGUI.show()

    def exit_pressed(self):
        """Lukker GUI vinduet"""
        self.close()


    def sql_pressed(self):
        """Loader databaser"""
        self.i += 1

        if self.i == 1:
            self.label_2.setText('Click again to confirm, then please wait\na few seconds, before proceeding to the login menu')
        else:
            self.databasesql.create_all_tables()


