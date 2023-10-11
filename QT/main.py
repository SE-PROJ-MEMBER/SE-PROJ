from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import GUI_v1_2
from backend import *


g_current_user_id = 0
g_sign_in_status = False
g_admin_status = False
g_pre_page = 0
g_pre_row = 0
g_current_order_id = 0


def turn_page(index):
    '''public'''
    UI.pages.setCurrentIndex(index)


def to_pre_page():
    '''public'''
    global g_pre_page
    UI.pages.setCurrentIndex(g_pre_page)


def set_color(row, r, g, b):
    '''public'''
    for col in range(UI.tableWidget.columnCount()):
        UI.tableWidget.item(row, col).setBackground(
            QtGui.QBrush(QtGui.QColor(r, g, b)))


def highlight_row():
    '''public'''
    g_pre_row
    set_color(g_pre_row, 255, 255, 255)
    set_color(UI.tableWidget.currentRow(), 0, 119, 237)
    g_pre_row = UI.tableWidget.currentRow()


def table_show(tablename):
    '''public'''
    global g_pre_row
    for i in range(tablename.columnCount()):
        tablename.item(g_pre_row, i).setBackground(
            QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        tablename.item(tablename.currentItem().row(), i).setBackground(
            QtGui.QBrush(QtGui.QColor(0, 119, 237)))
    g_pre_row = tablename.currentItem().row()


def addColumn(col: int, header: str, tablename):
    '''public'''
    # assert 0 <= col <= UI.tableWidget.columnCount()
    tablename.insertColumn(col)
    tablename.setHorizontalHeaderItem(col, QtWidgets.QTableWidgetItem(header))


def addMultiColumn(header_list: list | tuple, tablename):
    '''public'''
    for i in range(len(header_list)):
        addColumn(tablename.columnCount(), header_list[i])


def addRow(row: int, header: str, tablename):
    '''public'''
    # assert 0 <= row <= UI.tableWidget.rowCount()
    tablename.insertRow(row)
    tablename.setVerticalHeaderItem(row, QtWidgets.QTableWidgetItem(header))


def addMultiRow(header_list: list | tuple, tablename):
    '''public'''
    for i in range(len(header_list)):
        addRow(tablename.rowCount(), header_list[i])


def setCellText(row: int, column: int, text: str, tablename):
    '''public'''
    # assert 0 <= row <= UI.tableWidget.rowCount()
    # assert 0 <= column <= UI.tableWidget.columnCount()
    tablename.setItem(row, column, QtWidgets.QTableWidgetItem(text))


def log_out():
    '''public'''
    global g_sign_in_status, g_admin_status, g_current_user_id, g_current_order_id
    g_sign_in_status = False
    g_admin_status = False
    g_current_user_id = 0
    g_current_order_id = 0
    turn_page(1)

# page 1-7


def sign_in_slot():
    global g_sign_in_status, g_current_user_id
    selection = UI.Sign_in_choose.currentText()
    login_param = UI.ID_IN.text()
    pwd_input = UI.Pwd_in.text()
    chk_result = user_login(selection, login_param, pwd_input)
    if type(chk_result) == tuple:
        g_current_user_id = chk_result[-1]
        g_sign_in_status = True
        turn_page(1)
    else:
        UI.textBrowser.setText(chk_result)
        turn_page(2)


def create_account_slot():
    turn_page(3)
    name = UI.Name_in.text()
    phone = UI.phone_num_in.text()
    email = UI.email_in.text()
    card_num = UI.card_in.text()
    pwd = UI.pwd_in.text()
    reg_status = user_register(phone, email, name, card_num, pwd)
    global g_current_user_id, g_sign_in_status
    if type(reg_status) == tuple:
        g_current_user_id = reg_status[-1]
        g_sign_in_status = True
    else:
        turn_page(4)

# page 8-13


def show_current_user_email():
    '''billed to'''
    info = str(user_info(g_current_user_id)[3])
    turn_page(9)
    UI.order_info.setText(info)


def show_current_order():
    '''need info from page 7'''
    pass


def calculate_price():
    '''need info from page 7'''
    pass


def show_current_user_email():
    '''billed to'''
    info = str(user_info(g_current_user_id)[3])
    UI.user_name.setText(info)


def page8_to_page9():
    calculate_price()
    show_current_order()
    turn_page(9)


def show_persoanl_details():
    info = user_info(g_current_user_id)
    turn_page(11)
    info_str = f'name: {info[1]}phone: {info[3]}email: {info[4]}card: {info[5]}'
    UI.orders.setText(info_str)


def modify_user_info():
    alter_item = UI.co_to_modify.currentText()
    alter_value = UI.modify_info.text()
    alter_status = update_user(alter_item, alter_value, g_current_user_id)
    if alter_status != 'update_succeed':
        # UI.gridLayout_71.addWidget(QtWidgets.QMessageBox.warning(
        # Main, 'Error', alter_status, QtWidgets.QMessageBox.Ok))
        UI.reason.setText(alter_status)
        turn_page(21)
        return
    g_pre_page = 12
    turn_page(13)


def show_orders_info():
    table_show(UI.tableWidget)
    addMultiColumn(['room number', 'check-in', 'check-out',
                   'order status', 'comment'], UI.tableWidget)
    info = get_orders_of_user(g_current_user_id)
    order_num = len(info)
    num_list = [i+1 for i in range(order_num)]
    addMultiRow(num_list, UI.tableWidget)
    for i in range(order_num):
        setCellText(i, 0, str(info[i][1]), UI.tableWidget)
        setCellText(i, 1, str(info[i][3]), UI.tableWidget)
        setCellText(i, 2, str(info[i][4]), UI.tableWidget)
        setCellText(i, 3, str(info[i][5]), UI.tableWidget)
        setCellText(i, 4, str(info[i][6]), UI.tableWidget)


def page10_to_page11():
    show_persoanl_details()
    show_orders_info()
    turn_page(11)


def get_order_info_from_table():
    global g_current_user_id
    index_of_row = UI.tableWidget.currentItem().row()
    info = get_orders_of_user(g_current_user_id)
    g_current_user_id = info[index_of_row][0]


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    UI = GUI_v1_2.Ui_MainWindow()
    UI.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    # page 8-13
    UI.to_select_page.clicked.connect(lambda ret: turn_page(7))
    UI.to_payment_details.clicked.connect(page8_to_page9)
    UI.to_confirm_order_page.clicked.connect(lambda ret: turn_page(8))
    UI.to_payment_su_page.clicked.connect(lambda ret: turn_page(10))
    UI.to_personal_homepage.clicked.connect(page10_to_page11)
    UI.to_book_info_page_2.clicked.connect(lambda ret: turn_page(6))
    UI.if_and_to_modify.clicked.connect(lambda ret: turn_page(12))
    UI.modify_order.clicked.connect(lambda ret: turn_page(14))
    UI.to_book_info_page6.clicked.connect(lambda ret: turn_page(6))
    UI.to_personal_main_page.clicked.connect(lambda ret: turn_page(11))
    UI.to_op_su_page.clicked.connect(modify_user_info)
    UI.pushButton_2.clicked.connect(log_out)
    UI.to_pre_page.clicked.connect(lambda ret: turn_page(g_pre_page))
    UI.tableWidget.cellClicked.connect(table_show)
