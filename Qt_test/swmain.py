import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import swtest


def jump():
    UI.stackedWidget.setCurrentIndex(1)


def goback():
    UI.stackedWidget.setCurrentIndex(0)


def shrink_size():
    Main.showNormal()

def enlarge():
    Main.showFullScreen()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    Main = QtWidgets.QMainWindow()
    UI = swtest.Ui_MainWindow()

    UI.setupUi(Main)
    UI.stackedWidget.setCurrentIndex(0)

    Main.show()
    
    UI.next.clicked.connect(jump)
    UI.back.clicked.connect(goback)


    sys.exit(app.exec())
