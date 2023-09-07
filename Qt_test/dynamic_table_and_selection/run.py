import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import dy_table


def set_row_color(row: int, r, g, b):
    for i in range(UI.tableWidget.columnCount()):
        UI.tableWidget.item(row, i).setBackground(QtGui.QBrush(QtGui.QColor(r, g, b)))


row_count = 0


def down():
    global row_count
    if row_count + 1 <= UI.tableWidget.rowCount() - 1:
        row_count += 1
        set_row_color(row_count - 1, 255, 255, 255)
        set_row_color(row_count, 0, 255, 0)
    else:
        pass


def up():
    global row_count
    if row_count > 0:
        row_count -= 1
        set_row_color(row_count + 1, 255, 255, 255)
        set_row_color(row_count, 0, 255, 0)
    else:
        pass


def show_selection():
    global row_count
    result = 'Room ' + UI.tableWidget.item(row_count, 0).text()
    result += ' , type ' + UI.tableWidget.item(row_count, 1).text()
    UI.selection.setText(result)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    Main = QtWidgets.QMainWindow()
    UI = dy_table.Ui_MainWindow()

    UI.setupUi(Main)

    Main.show()
    set_row_color(0, 0, 255, 0)
    UI.select_down.clicked.connect(down)
    UI.select_up.clicked.connect(up)
    UI.select.clicked.connect(show_selection)

    sys.exit(app.exec())
