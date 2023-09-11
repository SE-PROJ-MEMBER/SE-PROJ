import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import table_clicking

prev_clicked_row = 0


def green():
    global prev_clicked_row
    for i in range(table.columnCount()):
        table.item(prev_clicked_row, i).setBackground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        table.item(table.currentItem().row(), i).setBackground(QtGui.QBrush(QtGui.QColor(172, 255, 0)))
    prev_clicked_row = table.currentItem().row()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    Main = QtWidgets.QMainWindow()
    UI = table_clicking.Ui_MainWindow()

    UI.setupUi(Main)

    Main.show()

    table = UI.tableWidget

    table.cellClicked.connect(green)

    sys.exit(app.exec())
