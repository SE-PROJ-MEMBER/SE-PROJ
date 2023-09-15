import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

import spacer_design

sign_in_status = 0
prev_row = 0


def set_color(row, r, g, b):
    for col in range(UI.tableWidget.columnCount()):
        UI.tableWidget.item(row, col).setBackground(
            QtGui.QBrush(QtGui.QColor(r, g, b)))


def highlight_row():
    global prev_row
    set_color(prev_row, 255, 255, 255)
    set_color(UI.tableWidget.currentRow(), 84, 255, 159)
    prev_row = UI.tableWidget.currentRow()


def sign_in_slot():
    global sign_in_status
    if sign_in_status == 0 and UI.ID_IN.text() != '' and UI.Pwd_in.text() != '':
        # interact with db
        UI.pages.setCurrentIndex(1)
        UI.user_name_dis.setText(UI.ID_IN.text())
        sign_in_status = 1
        time.sleep(2)
        UI.pages.setCurrentIndex(5)
    else:
        UI.pages.setCurrentIndex(2)
        UI.textBrowser.setText('The Username or password cannot be empty.')


def create_account_slot():
    """ conditions and interact with db"""


def find_room(from_data, to_data, rtype):
    """ interact wth db"""


def display(results_data):
    """ need results from db"""


def search_room_slot():
    from_date = UI.ck_in.date()
    from_date_split = [from_date.year(), from_date.month(), from_date.day()]
    to_date = UI.ck_2.date()
    to_date_split = [to_date.year(), to_date.month(), to_date.day()]
    room_type = UI.Room_type.currentText()

    results_data = find_room(from_date_split, to_date_split, room_type)
    display(results_data)
    UI.pages.setCurrentIndex(6)


def select_room_slot():
    table = UI.tableWidget
    room_data = [table.item(table.currentRow(), col)
                 for col in range(table.columnCount())]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    Main = QtWidgets.QMainWindow()
    UI = spacer_design.Ui_MainWindow()

    UI.setupUi(Main)
    UI.pages.setCurrentIndex(0)
    UI.ck_in.setDate(QDate.currentDate())
    UI.ck_2.setDate(QDate.currentDate())

    UI.sign_in.clicked.connect(sign_in_slot)
    UI.to_sign_in_page.clicked.connect(lambda ret: UI.pages.setCurrentIndex(0))
    UI.to_sign_in_page_2.clicked.connect(
        lambda ret: UI.pages.setCurrentIndex(0))

    UI.to_sign_up_page.clicked.connect(
        lambda to_sign_up: UI.pages.setCurrentIndex(3))
    UI.to_sign_up_page_2.clicked.connect(
        lambda to_sign_up: UI.pages.setCurrentIndex(3))

    UI.confirm.clicked.connect(create_account_slot)

    UI.to_room_select_page.clicked.connect(search_room_slot)
    UI.to_book_info_page.clicked.connect(
        lambda ret: UI.pages.setCurrentIndex(5))

    UI.tableWidget.cellClicked.connect(highlight_row)

    UI.to_confirm_order_page.clicked.connect(select_room_slot)

    Main.show()

    sys.exit(app.exec())
