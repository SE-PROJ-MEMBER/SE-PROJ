import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import untitled
from functools import partial


def calculate(ui):
    input_1 = ui.lineEdit.text()
    input_2 = ui.lineEdit_2.text()
    if input_1 and input_2:
        result = int(input_1) ** int(input_2)
        ui.textBrowser.setText(str(result))
    else:
        pass


def clear_all(ui):
    ui.lineEdit.clear()
    ui.lineEdit_2.clear()
    ui.textBrowser.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DL = QtWidgets.QDialog()
    Ui = untitled.Ui_Dialog()
    Ui.setupUi(DL)
    DL.show()

    Ui.clr_button.clicked.connect(partial(clear_all, Ui))
    Ui.pushButton.clicked.connect(partial(calculate, Ui))

    sys.exit(app.exec())
