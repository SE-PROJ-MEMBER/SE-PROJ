import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import LOG_IN, SU, FA

def main():
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QDialog()
    window = LOG_IN.Ui_Dialog()
    
    window.setupUi(win)
    
    win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()