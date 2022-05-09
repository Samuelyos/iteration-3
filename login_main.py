import sys
from PyQt6 import QtWidgets
from LoginGUI import LoginGUI

def login_main():
    app = QtWidgets.QApplication(sys.argv)
    login_window = LoginGUI()
    app.exec()

if __name__ == '__main__':
    login_main()
