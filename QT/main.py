from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import GUI_v1_7
from backend import *
import threading
from functools import partial
from datetime import datetime


g_current_user_id = 0
g_sign_in_status = False
g_admin_status = False
g_pre_page = 0
g_pre_row = 0
g_current_order_id = 0
g_search_result = [None for i in range(100)]
g_user_selection = [None for i in range(7)]
g_user_selection_date = [None for i in range(2)]
g_table_name = None

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
    global g_pre_row
    set_color(g_pre_row, 255, 255, 255)
    set_color(UI.tableWidget.currentRow(), 0, 119, 237)
    g_pre_row = UI.tableWidget.currentRow()


def table_show():
    '''public,调用前需要先设置g_table_name'''
    global g_pre_row, g_table_name
    print(type(g_table_name))
    for i in range(g_table_name.columnCount()):
        if g_table_name.item(g_pre_row, i) == None:
            break
        g_table_name.item(g_pre_row, i).setBackground(
            QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        
        if g_table_name.currentItem() is None:
            # pass
            break
        
        g_table_name.item(g_table_name.currentItem().row(), i).setBackground(
            QtGui.QBrush(QtGui.QColor(0, 119, 237)))
    if g_table_name.currentItem() is not None:
        g_pre_row = g_table_name.currentItem().row()
    # g_pre_row = tablename.currentItem().row()
    


def addColumn(col: int, header: str, tablename):
    '''public'''
    # assert 0 <= col <= UI.tableWidget.columnCount()
    tablename.insertColumn(col)
    tablename.setHorizontalHeaderItem(col, QtWidgets.QTableWidgetItem(header))


def addMultiColumn(header_list: list | tuple, tablename):
    '''public'''
    for i in range(len(header_list)):
        addColumn(tablename.columnCount(), header_list[i],tablename)


def addRow(row: int, header: str, tablename):
    '''public'''
    # assert 0 <= row <= UI.tableWidget.rowCount()
    tablename.insertRow(row)
    tablename.setVerticalHeaderItem(row, QtWidgets.QTableWidgetItem(header))


def addMultiRow(header_list: list | tuple, tablename):
    '''public'''
    for i in range(len(header_list)):
        addRow(tablename.rowCount(), header_list[i],tablename)


def setCellText(row: int, column: int, text: str, tablename):
    '''public'''
    # assert 0 <= row <= UI.tableWidget.rowCount()
    # assert 0 <= column <= UI.tableWidget.columnCount()
    tablename.setItem(row, column, QtWidgets.QTableWidgetItem(str(text)))


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
    global g_sign_in_status, g_current_user_id, g_admin_status
    sel = UI.Sign_in_choose.currentText()
    if sel == 'Name':
        selection = 'user_name'
    if  sel == 'Phone':
        selection = 'user_phone'
    if sel == 'Email':
        selection = 'user_email'  
    login_param = UI.ID_IN.text()
    pwd_input = UI.Pwd_in.text()
    chk_result = user_login(selection, login_param, pwd_input)
    if type(chk_result) == tuple:
        # login succeed
        g_current_user_id = chk_result[-1]
        g_sign_in_status = True
        UI.user_name_dis.setText(user_info(g_current_user_id)[1])
        turn_page(5)
        
        if selection == 'name' and login_param[:5:] == 'admin':
            # check admin account
            g_admin_status = True
            turn_page(15)
        else:
            turn_page(5)
    else:
        # login error
        UI.textBrowser.setText(chk_result)
        turn_page(2)


def create_account_slot():
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
        UI.user_name_dis.setText(user_info(g_current_user_id)[1])
        turn_page(5)
        turn_page(1)
    else:
        turn_page(4)


def start_search():
    UI.ck_in.setDate(QtCore.QDate.currentDate())
    UI.ck_out.setDate(QtCore.QDate.currentDate())
    date_format_str = "yyyy-MM-dd"
    begin = UI.ck_in.date().toString(date_format_str)
    end = UI.ck_out.date().toString(date_format_str)
    global g_user_selection_date
    g_user_selection_date[0] = begin
    g_user_selection_date[1] = end
    rtype = UI.Room_type.currentText()
    global g_search_result
    g_search_result = find_room(begin, end, rtype)
    # print(g_search_result)


def show_search_result():
    global g_search_result
    addMultiColumn(['room num', 'room type', 'room price'], UI.room_info)
    result_length = len(g_search_result)
    addMultiRow([str(i + 1) for i in range(result_length)], UI.room_info)
    for i in range(result_length):
        for j in range(3):
            setCellText(i, j, g_search_result[i][j], UI.room_info)
    print(str(type(UI.room_info))+'a')
    global g_table_name
    g_table_name = UI.room_info
    table_show()
    print(str(type(UI.room_info))+'b')


def search_slot():
    start_search()
    show_search_result()
    turn_page(6)


def room_selection_result():
    global g_user_selection
    g_user_selection = g_search_result[UI.room_info.currentItem().row()]


def select_slot():
    room_selection_result()
    show_current_order()
    turn_page(7)


def return_slot_5():
    turn_page(5)
    global g_pre_row
    g_pre_row = 0
    UI.room_info.clear
    UI.room_info.clearContents()
    UI.room_info.clearFocus()
    # UI.QStandardItemModel().clear()

# page 8-13


def show_current_user_email():
    '''billed to'''
    info = str(user_info(g_current_user_id)[3])
    turn_page(8)
    UI.order_info.setText(info)


def show_current_order():
    global g_user_selection
    info = f'room number: {g_user_selection[1]}check in: {g_user_selection[3]}check out: {g_user_selection[4]}'
    UI.order_info.setText(info)


def calculate_price():
    global g_user_selection
    room_num = g_user_selection[1]
    p = get_price(room_num)
    p_final = p*calculate_date(g_user_selection[3], g_user_selection[4])
    UI.pay_total.display(p_final)


def calculate_date(st, en):
    st_ = datetime.strptime(st, "%Y-%m-%d")
    en_ = datetime.strptime(en, "%Y-%m-%d")
    delta = en_ - st_
    days = delta.days
    return days


def show_current_user_email():
    '''billed to'''
    info = str(user_info(g_current_user_id)[3])
    UI.user_name.setText(info)


def page8_to_page9():
    calculate_price()
    show_current_user_email()
    createeee_order()
    turn_page(8)


def show_persoanl_details():
    info = user_info(g_current_user_id)
    turn_page(10)
    info_str = f'name: {info[1]}phone: {info[3]}email: {info[4]}card: {info[5]}'
    UI.orders.setText(info_str)


def modify_user_info():
    if UI.co_to_modify.currentText() == 'Name':
        alter_item = 'user_name'
    if UI.co_to_modify.currentText() == 'Phone':
        alter_item = 'user_phone'
    if UI.co_to_modify.currentText() == 'Email':
        alter_item = 'user_email'
    if UI.co_to_modify.currentText() == 'Card':
        alter_item = 'user_card'
    if UI.co_to_modify.currentText() == 'Password':
        alter_item = 'user_pwd'
    alter_value = UI.modify_info.text()
    alter_status = update_user(alter_item, alter_value, g_current_user_id)
    if alter_status != 'update_succeed':
        # UI.gridLayout_71.addWidget(QtWidgets.QMessageBox.warning(
        # Main, 'Error', alter_status, QtWidgets.QMessageBox.Ok))
        UI.reason.setText(alter_status)
        turn_page(20)
        return
    g_pre_page = 11
    turn_page(12)


def show_orders_info():
    global g_table_name
    g_table_name = UI.tableWidget
    table_show()
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
    turn_page(10)


def get_order_info_from_table():
    global g_current_user_id
    index_of_row = UI.tableWidget.currentItem().row()
    info = get_orders_of_user(g_current_user_id)
    g_current_user_id = info[index_of_row][0]


def createeee_order():
    global g_current_user_id
    global g_user_selection
    global g_user_selection_date
    global g_current_order_id
    g_current_order_id = create_order(g_user_selection[0], g_current_user_id,  g_user_selection_date[0], g_user_selection_date[1])[1]
    
    
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    UI = GUI_v1_7.Ui_MainWindow()
    UI.setupUi(Main)
    UI.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    UI.room_info.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    # page 1-7
    UI.sign_in.clicked.connect(sign_in_slot)
    UI.to_sign_up_page.clicked.connect(lambda ret: turn_page(3))
    UI.to_sign_in_page.clicked.connect(lambda ret: turn_page(0))
    UI.to_sign_in_page_2.clicked.connect(lambda ret: turn_page(0))
    UI.confirm.clicked.connect(create_account_slot)
    UI.to_sign_up_page_2.clicked.connect(lambda ret: turn_page(3))
    UI.to_sign_in_page_5.clicked.connect(lambda ret: turn_page(0))
    UI.to_room_select_page.clicked.connect(search_slot)
    # UI.to_confirm_order_page.clicked.connect(select_slot)
    UI.to_book_info_page.clicked.connect(return_slot_5)
    UI.room_info.cellClicked.connect(table_show)
    
    
    # page 8-13
    UI.to_select_page.clicked.connect(lambda ret: turn_page(6))
    UI.to_payment_details.clicked.connect(page8_to_page9)
    UI.to_confirm_order_page.clicked.connect(lambda ret: turn_page(7))
    UI.to_payment_su_page.clicked.connect(lambda ret: turn_page(9))
    UI.to_personal_homepage.clicked.connect(page10_to_page11)
    UI.to_book_info_page_2.clicked.connect(lambda ret: turn_page(5))
    UI.if_and_to_modify.clicked.connect(lambda ret: turn_page(11))
    UI.modify_order.clicked.connect(lambda ret: turn_page(13))
    UI.to_book_info_page6.clicked.connect(lambda ret: turn_page(5))
    UI.to_personal_main_page.clicked.connect(lambda ret: turn_page(10))
    UI.to_op_su_page.clicked.connect(modify_user_info)
    UI.pushButton_2.clicked.connect(log_out)
    UI.to_pre_page.clicked.connect(lambda ret: turn_page(g_pre_page))
    UI.tableWidget.cellClicked.connect(table_show)    
    
    
    UI.pages.setCurrentIndex(0)
    Main.show()
    sys.exit(app.exec())
