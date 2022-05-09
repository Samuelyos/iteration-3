from PyQt6 import QtWidgets, uic
from AdminRequestGUI import AdminRequestGUI
from TeacherRequestGUI import TeacherRequestGUI
from Model.login_class import Login
from Model.courseleader_class import Courseleader
from Model.admin_class import Admin

##
hugo = Courseleader('Hugo', 'Test', 'abc123')
hugo_login = Login(hugo, 'password')

henrik = Admin('Henrik', 'Hansen', 'zyx999')
henrik_login = Login(henrik, 'password')
##

class LoginGUI(QtWidgets.QDialog):
    """Klasse for selve ændring af lektioner GUI"""

    def __init__(self):
        super(LoginGUI, self).__init__()
        uic.loadUi('../View/LoginScreen.ui', self)

        self.ExitPush.clicked.connect(self.Exit_button_pressed)
        self.LoginPush.clicked.connect(self.Login_button_pressed)
        self.currentUser = None
        self.show()

    def Login_button_pressed(self):

        self.written_username = self.usernameLabel.text()
        self.written_password = self.passwordLabel.text()

        if len(self.written_username) == 6:
            for user in Login.all_users:
                if self.written_username == user.get_userID() and self.written_password == user.get_password():
                    self.currentUser = user

                    # Hvis brugeren er administrator, åbnes tilhørende GUI
                    if self.currentUser.get_role() == 'admin':
                        self.close()
                        self.admingui = AdminRequestGUI()
                        self.admingui.show()

                    # Hvis brugeren er underviser, åbnes tilhørende GUI
                    elif self.currentUser.get_role() == 'courseleader':
                        self.close()
                        self.courseleadergui = TeacherRequestGUI()
                        self.courseleadergui.show()
                else:
                    continue
        else:
            #Følgende er tekst i en tekstbox som ændre sig ved hvert forkert login-forsøg for at give feedback
            if self.wrongLabel.text() == '':
                self.wrongLabel.setText('Wrong username or password!\nTry again')
            elif len(self.wrongLabel.text()) >= 50:
                self.wrongLabel.setText('Wrong username or password!\nTry again')
            else:
                temp_label = self.wrongLabel.text()
                temp_label = temp_label + '...'
                self.wrongLabel.setText(temp_label)


    def Exit_button_pressed(self):
        self.close()
