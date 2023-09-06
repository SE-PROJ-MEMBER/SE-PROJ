import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import switch_page_test


def to_info():
    global prev_index
    prev_index = UI.stackedWidget.currentIndex()
    UI.stackedWidget.setCurrentIndex(2)


def goback():
    UI.stackedWidget.setCurrentIndex(prev_index)


def to_2():
    UI.stackedWidget.setCurrentIndex(1)

def to_1():
    UI.stackedWidget.setCurrentIndex(0)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    Main = QtWidgets.QMainWindow()
    UI = switch_page_test.Ui_MainWindow()

    UI.setupUi(Main)
    UI.stackedWidget.setCurrentIndex(0)

    Main.show()

    UI.to_info_1.clicked.connect(to_info)
    UI.to_info_2.clicked.connect(to_info)
    UI.to_p1.clicked.connect(to_1)
    UI.to_p2.clicked.connect(to_2)
    UI.back_button.clicked.connect(goback)

    sys.exit(app.exec())
