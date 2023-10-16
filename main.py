from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re

from PyQt5.QtWidgets import QTableWidgetItem

import GUI_v5
import msgbox
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
g_status_info = ['reserved', 'checked in', 'checked out', 'cancelled', 'unpaid']
g_current_room_number = 0

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
            # turn_page(UI.pages.currentIndex())
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
    turn_page(0)
    clear_table(UI.tableWidget)
    clear_table(UI.room_info)
    UI.ID_IN.setText('')
    UI.Pwd_in.setText('')
    UI.Sign_in_choose.setCurrentIndex(0)
    UI.Room_type.setCurrentIndex(0)
    UI.ck_in.setDate(QtCore.QDate.currentDate())
    UI.ck_2.setDate(QtCore.QDate.currentDate())
    


def clear_table(tablename):
    '''public'''
    tablename.setRowCount(0)
    tablename.setColumnCount(0)

    

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
    if sel == '': 
        return
    login_param = UI.ID_IN.text()
    pwd_input = UI.Pwd_in.text()
    chk_result = user_login(selection, login_param, pwd_input)
    if type(chk_result) == tuple:
        # login succeed
        g_current_user_id = chk_result[-1]
        g_sign_in_status = True
        UI.user_name_dis.setText(user_info(g_current_user_id)[1])
        turn_page(1)
        
        if sel == 'Name' and login_param[:5] == 'admin':
            # check admin account
            g_admin_status = True
            turn_page(15)
        else:
            turn_page(1)
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
    if name == '' or phone == '' or email == '' or card_num == '' or pwd == '':
        UI.textBrowser_2.setText('Please fill in all the blanks')
        turn_page(4)
        return
    if name[:5] == 'admin':
        UI.textBrowser_2.setText('Invalid name')
        turn_page(4)
        return
    if len(phone) != 11 or not phone.isdigit():
        UI.textBrowser_2.setText('Invalid phone number')
        turn_page(4)
        return
    if len(card_num) != 16 or not card_num.isdigit():
        UI.textBrowser_2.setText('Invalid card number')
        turn_page(4)
        return
    if len(pwd) < 6:
        UI.textBrowser_2.setText('Password too short')
        turn_page(4)
        return
    if len(pwd) > 16:
        UI.textBrowser_2.setText('Password too long')
        turn_page(4)
        return
    if not pwd.isalnum():
        UI.textBrowser_2.setText('Password should only contain letters and numbers')
        turn_page(4)
        return
    if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
        UI.textBrowser_2.setText('Invalid email address')
        turn_page(4)
        return
    reg_status = user_register(phone, email, name, card_num, pwd)
    global g_current_user_id, g_sign_in_status
    if type(reg_status) == tuple:
        g_current_user_id = reg_status[-1]
        g_sign_in_status = True
        UI.user_name_dis.setText(user_info(g_current_user_id)[1])
        # turn_page(5)
        UI.Name_in.setText('')
        UI.phone_num_in.setText('')
        UI.email_in.setText('')
        UI.card_in.setText('')
        UI.pwd_in.setText('')
        turn_page(1)
    else:
        turn_page(4)


def msg_close_slot():
    msg.close()
    turn_page(5)


def start_search():
    
    date_format_str = "yyyy-MM-dd"
    begin = UI.ck_in.date().toString(date_format_str)
    end = UI.ck_2.date().toString(date_format_str)
    if begin <= QtCore.QDate.currentDate().toString(date_format_str):
        UI.ck_in.setDate(QtCore.QDate.currentDate())
        begin = UI.ck_in.date().toString(date_format_str)
        global g_user_selection_date
    if begin >= end:
        UI.ck_2.setDate(UI.ck_in.date().addDays(1))
        # global g_user_selection_date
    if UI.ck_in.date().addDays(13) < UI.ck_2.date():
        msg.show()
        return
    g_user_selection_date[0] = UI.ck_in.date().toString(date_format_str)
    g_user_selection_date[1] = UI.ck_2.date().toString(date_format_str)
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
    UI.room_info.setCurrentItem(None)
    start_search()
    if msg.isVisible() == False:
        show_search_result()
        turn_page(6)


def room_selection_result():
    global g_user_selection    
    if UI.room_info.currentItem() is None:
        print(2)
        return
    g_user_selection = g_search_result[UI.room_info.currentItem().row()]
    select_slot()

def select_slot():
    print(1)
    show_current_order()
    # clear_table(UI.room_info)
    turn_page(7)


def return_slot_5():
    turn_page(5)
    global g_pre_row
    g_pre_row = 0
    clear_table(UI.room_info)

def page_1_to_homepage():
    show_orders_info()
    show_persoanl_details()
    UI.tableWidget.setCurrentItem(None)
    
    
# page 8-13


def show_current_user_email():
    '''billed to'''
    info = str(user_info(g_current_user_id)[3])
    turn_page(8)
    UI.order_info.setText(info)


def show_current_order():
    global g_user_selection
    global g_user_selection_date
    info = f'room number: {g_user_selection[0]}\ncheck in: {g_user_selection_date[0]}\ncheck out: {g_user_selection_date[1]}'
    UI.order_info.setText(info)


def calculate_price():
    global g_user_selection
    room_num = g_user_selection[0]
    p = get_price(room_num)
    p_final = p*calculate_date(g_user_selection_date[0], g_user_selection_date[1])
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
    clear_table(UI.room_info)
    UI.room_info.setCurrentItem(None)
    turn_page(8)


def show_persoanl_details():
    info = user_info(g_current_user_id)
    turn_page(10)
    info_str = f'name: {info[1]}\nphone: {info[2]}\nemail: {info[3]}\ncard: {info[4]}'
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
    if UI.co_to_modify.currentText() == '':
        return
    alter_value = UI.modify_info.text()
    alter_status = update_user(alter_item, alter_value, g_current_user_id)
    if alter_status != '200':
        # UI.gridLayout_71.addWidget(QtWidgets.QMessageBox.warning(
        # Main, 'Error', alter_status, QtWidgets.QMessageBox.Ok))
        UI.reason.setText(alter_status)
        turn_page(20)
        return
    global g_pre_page
    g_pre_page = 11
    turn_page(12)


def show_orders_info():
    global g_table_name,g_status_info
    g_table_name = UI.tableWidget
    table_show()
    addMultiColumn(['room number', 'check-in', 'check-out',
                   'order status', 'comment'], UI.tableWidget)
    info = get_orders_of_user(g_current_user_id)
    if info == 'no order':
        return
    order_num = len(info)
    num_list = [str(i+1) for i in range(order_num)]
    addMultiRow(num_list, UI.tableWidget)
    for i in range(order_num):
        setCellText(i, 0, str(info[i][1]), UI.tableWidget)
        setCellText(i, 1, str(info[i][3]), UI.tableWidget)
        setCellText(i, 2, str(info[i][4]), UI.tableWidget)
        setCellText(i, 3, str(g_status_info[info[i][5]]), UI.tableWidget)
        setCellText(i, 4, str(info[i][6]), UI.tableWidget)


def page10_to_page11():
    show_persoanl_details()
    show_orders_info()
    UI.tableWidget.setCurrentItem(None)
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
    

def modify_order_slot():    
    print(UI.tableWidget.currentItem())
    if UI.tableWidget.currentItem() is None:
    
        print(2)
        return
    turn_page(13)
    clear_table(UI.tableWidget)    


def return_slot_5_2():
    turn_page(5)
    clear_table(UI.tableWidget) 
    clear_table(UI.room_info)
    
    
def turn_slot_10():
    update_order('order_status', 4, g_current_order_id)
    show_orders_info()
    show_persoanl_details()
    UI.tableWidget.setCurrentItem(None)
    turn_page(10)


# page20-25
def page22_to_page23():
    global g_current_room_number
    if g_current_room_number == 0:
        return
    turn_page(22)

def to_page22():
    turn_page(21)
    show_rooms_info()


def user_deleter():
    alter_status = delete_user(uesr_id) # 这个参数需要page16提供
    if alter_status != '200':
        # UI.gridLayout_71.addWidget(QtWidgets.QMessageBox.warning(
        # Main, 'Error', alter_status, QtWidgets.QMessageBox.Ok))
        UI.reason.setText(alter_status)
        turn_page(20)
        global g_pre_page
        g_pre_page = 19
        return
    turn_page(12)


def display_error_message():
    """显示错误原因"""
    pass


def show_rooms_info():
    global g_table_name
    UI.rooms.clearContents()
    room_data = get_all_rooms()  # [(101,'A',300)]
    UI.rooms.setColumnCount(len(room_data[0]))
    UI.rooms.setRowCount(len(room_data))
    for row, room in enumerate(room_data):
        for col, value in enumerate(room):
            item = QTableWidgetItem(str(value))
            UI.rooms.setItem(row, col, item)
    g_table_name = UI.rooms
    table_show()
    UI.rooms.update()
    pass

def on_table_item_clicked(item):
    global g_pre_row, g_current_room_number, g_table_name
    g_table_name = UI.tableWidget
    table_show()
    if item is not None:
        row = item.row()
        g_current_room_number = UI.tableWidget.item(row, 0).text()


def room_deleter():
    current_row = UI.rooms.currentRow()
    room_number = UI.tableWidget.item(current_row, 0).text()
    alter_status = delete_room(room_number)
    if alter_status != '200':
        # UI.gridLayout_71.addWidget(QtWidgets.QMessageBox.warning(
        # Main, 'Error', alter_status, QtWidgets.QMessageBox.Ok))
        UI.reason.setText(alter_status)
        turn_page(20)
        global g_pre_page
        g_pre_page = 21
        return
    turn_page(12)
    pass


def modify_room():
    selected_option = UI.to_modify.currentText()
    modified_value = UI.modified_info.currentText()
    if selected_option == 'Room type':
        alter_item = 'room_type'
    elif selected_option == 'Room price':
        alter_item = 'room_price'
    else:
        return
    alter_status = update_room(alter_item, modified_value, g_current_room_number)
    if alter_status != '200':
        # UI.gridLayout_71.addWidget(QtWidgets.QMessageBox.warning(
        # Main, 'Error', alter_status, QtWidgets.QMessageBox.Ok))
        UI.reason.setText(alter_status)
        turn_page(20)
        global g_pre_page
        g_pre_page = 22
        return
    turn_page(12)
    pass


def add_room():
    room_num = UI.room_num_in_2.text()
    room_type = UI.room_type.currentText()
    price = UI.room_price_in.text()
    if room_num is not None and room_type is not None and price is not None:
        alter_status = create_room(room_num, room_type, price)
        if alter_status != '200':
            # UI.gridLayout_71.addWidget(QtWidgets.QMessageBox.warning(
            # Main, 'Error', alter_status, QtWidgets.QMessageBox.Ok))
            UI.reason.setText(alter_status)
            turn_page(20)
            global g_pre_page
            g_pre_page = 23
            return
        turn_page(12)
    return # none value error


def add_user():
    name = UI.name_in.text()
    phone = UI.phone_num_in_2.text()
    email = UI.email_in_2.text()
    card_num = UI.card_in_2.text()
    pwd = UI.pwd_in_2.text()
    if name == ''or pwd == '':
        return
    if name[:5] == 'admin':
        alter_status = create_user_np(name, pwd)
    else:
        if name == '' or phone == '' or email == '' or card_num == '' or pwd == '':
            return
        alter_status = user_register(phone, email, name, card_num, pwd)
    if alter_status != '200':
        # UI.gridLayout_71.addWidget(QtWidgets.QMessageBox.warning(
        # Main, 'Error', alter_status, QtWidgets.QMessageBox.Ok))
        UI.reason.setText(alter_status)
        turn_page(20)
        global g_pre_page
        g_pre_page = 24
        return
    turn_page(12)


# 26-27

def reset_password():
    r_name = UI.lineEdit.text()
    r_phone = UI.lineEdit_2.text()
    r_email = UI.lineEdit_3.text()
    r_card = UI.lineEdit_4.text()
    user_info = user_ser(r_name)
    if r_name == '' or r_phone == '' or r_email == '' or r_card == '':
        UI.reason.setText('Please fill in all the blanks')
        global g_pre_page
        g_pre_page = 25
        turn_page(20)
        return
    if user_info == 'user_not_exist':
        UI.reason.setText('user not exist')
        # global g_pre_page
        g_pre_page = 25
        turn_page(20)
        return
    if str(user_info[2]) != r_phone or user_info[3] != r_email or str(user_info[4]) != r_card:
        UI.reason.setText('information not match')
        # global g_pre_page
        g_pre_page = 25
        turn_page(20)
        return
    global g_current_user_id
    g_current_user_id = user_info[0]
    turn_page(26)
    
    
def reset_password2():
    new_pwd = UI.lineEdit_5.text()
    new_pwd2 = UI.lineEdit_6.text()
    if new_pwd != new_pwd2:
        UI.reason.setText('password not match')
        global g_pre_page
        g_pre_page = 26
        turn_page(20)
        return
    if len(new_pwd) < 6:
        UI.reason.setText('Password too short')
        # global g_pre_page
        g_pre_page = 26
        turn_page(20)
        return
    if len(new_pwd) > 16:
        UI.reason.setText('Password too long')
        # global g_pre_page
        g_pre_page = 26
        turn_page(20)
        return
    if not new_pwd.isalnum():
        UI.reason.setText('Password should only contain letters and numbers')
        # global g_pre_page
        g_pre_page = 26
        turn_page(20)
        return
    global g_current_user_id
    update_user('user_pwd',new_pwd,g_current_user_id)
    g_current_user_id = 0
    turn_page(0)
    
    
def reset_password0():
    UI.lineEdit.setText('')
    UI.lineEdit_2.setText('')
    UI.lineEdit_3.setText('')
    UI.lineEdit_4.setText('')
    UI.lineEdit_5.setText('')
    UI.lineEdit_6.setText('')
    turn_page(25)
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    UI = GUI_v5.Ui_MainWindow()
    UI.setupUi(Main)
    msg = QtWidgets.QDialog()
    msg_UI = msgbox.Ui_Dialog()
    msg_UI.setupUi(msg)
    UI.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    UI.room_info.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    UI.ck_in.setDate(QtCore.QDate.currentDate())
    UI.ck_2.setDate(QtCore.QDate.currentDate())
    msg.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
    msg.setWindowTitle("Warning!")

    # page 1-7
    UI.commandLinkButton.clicked.connect(reset_password0)
    UI.to_homepage.clicked.connect(page_1_to_homepage)
    UI.to_book_a_room.clicked.connect(lambda ret: turn_page(5))
    UI.sign_in.clicked.connect(sign_in_slot)
    UI.to_sign_up_page.clicked.connect(lambda ret: turn_page(3))
    UI.to_sign_in_page.clicked.connect(lambda ret: turn_page(0))
    UI.to_sign_in_page_2.clicked.connect(lambda ret: turn_page(0))
    UI.confirm.clicked.connect(create_account_slot)
    UI.to_sign_up_page_2.clicked.connect(lambda ret: turn_page(3))
    UI.to_sign_in_page_5.clicked.connect(log_out)
    UI.to_room_select_page.clicked.connect(search_slot)
    UI.to_confirm_order_page.clicked.connect(room_selection_result)
    UI.to_book_info_page.clicked.connect(return_slot_5)
    UI.room_info.cellClicked.connect(table_show)

    # message box
    msg_UI.close_msg.clicked.connect(msg.close)
    
    
    # page 8-13
    UI.to_select_page.clicked.connect(lambda ret: turn_page(6))
    UI.to_payment_details.clicked.connect(page8_to_page9)
    # UI.to_confirm_order_page.clicked.connect(lambda ret: turn_page(7))
    UI.to_payment_su_page.clicked.connect(lambda ret: turn_page(9))
    UI.to_personal_homepage.clicked.connect(page10_to_page11)
    UI.to_book_info_page_2.clicked.connect(lambda ret: turn_page(5))
    UI.if_and_to_modify.clicked.connect(lambda ret: turn_page(11))
    UI.modify_order.clicked.connect(modify_order_slot)
    UI.to_book_info_page6.clicked.connect(return_slot_5_2)
    UI.to_personal_main_page.clicked.connect(lambda ret: turn_page(10))
    UI.to_op_su_page.clicked.connect(modify_user_info)
    UI.pushButton_2.clicked.connect(log_out)
    UI.to_pre_page.clicked.connect(lambda ret: turn_page(g_pre_page))
    UI.to_comfirm_order_page.clicked.connect(turn_slot_10)
    UI.tableWidget.cellClicked.connect(table_show)


    # page20-25
    UI.to_add_user_page.clicked.connect(lambda ret: turn_page(22))
    UI.delete_user_to_op_su_page.clicked.connect(lambda ret: user_deleter())
    UI.to_log_in_page_2.clicked.connect(lambda ret: turn_page(0))
    UI.to_admin_page_2.clicked.connect(lambda ret: turn_page(15))
    UI.to_pre_page_2.clicked.connect(lambda ret: to_pre_page())
    UI.to_admin_page_3.clicked.connect(lambda ret: turn_page(15))
    UI.to_room_op_page.clicked.connect(lambda ret: turn_page(22))
    UI.to_sign_in_page_6.clicked.connect(lambda ret: turn_page(0))
    UI.delete_room.clicked.connect(lambda ret: room_deleter())
    UI.to_add_room_page.clicked.connect(lambda ret: turn_page(23))
    UI.to_manage_room_page.clicked.connect(lambda ret: to_page22())
    UI.to_op_su_page_2.clicked.connect(lambda ret: modify_room())
    UI.to_manage_room_page_2.clicked.connect(lambda ret: to_page22())
    UI.to_op_su_page_3.clicked.connect(lambda ret: add_room())
    UI.to_manage_user_page.clicked.connect(lambda ret: turn_page(19))
    UI.to_op_su_page_4.clicked.connect(lambda ret: add_user())
    UI.tableWidget.itemClicked.connect(on_table_item_clicked)

    
    #26-27
    UI.pushButton_3.clicked.connect(log_out)
    UI.pushButton_4.clicked.connect(reset_password)
    UI.pushButton_5.clicked.connect(reset_password2)
    
    
    
    
    
    
    UI.pages.setCurrentIndex(0)
    Main.show()
    sys.exit(app.exec())
