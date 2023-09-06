import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import untitled
import window


def calculate():
    input_1 = Ui.lineEdit.text()
    input_2 = Ui.lineEdit_2.text()
    if input_1 and input_2:
        result = int(input_1) ** int(input_2)
        Ui.textBrowser.setText(str(result))
    else:
        pass


def clear_all():
    Ui.lineEdit.clear()
    Ui.lineEdit_2.clear()
    Ui.textBrowser.clear()


def jump():
    DL.close()
    MW.show()


def back():
    MW.close()
    DL.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    DL = QtWidgets.QDialog()
    MW = QtWidgets.QMainWindow()

    Ui2 = window.Ui_MainWindow()
    Ui = untitled.Ui_Dialog()

    Ui2.setupUi(MW)
    Ui.setupUi(DL)

    DL.show()

    Ui.clr_button.clicked.connect(clear_all)
    Ui.pushButton.clicked.connect(calculate)
    Ui.jump_to_win.clicked.connect(jump)
    Ui2.back_button.clicked.connect(back)

    sys.exit(app.exec())
