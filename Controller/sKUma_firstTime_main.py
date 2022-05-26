import sys
from PyQt6 import QtWidgets
from FirstTimeGUI import FirstTimeGUI

def sKUma_firstTime_main():
    app = QtWidgets.QApplication(sys.argv)
    firsttime_window = FirstTimeGUI()
    app.exec()

if __name__ == '__main__':
    sKUma_firstTime_main()
