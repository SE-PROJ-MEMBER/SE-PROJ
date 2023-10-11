from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import GUI_v1_1
from backend import *


g_current_user_id = 0
g_sign_in_status = False
g_admin_status = False
g_pre_page = 0
g_pre_row = 0


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


def show_current_user_email():
    '''billed to'''
    info =  str(user_info(g_current_user_id)[3])
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
    return user_info(g_current_user_id)[3]
def show_persoanl_details():
    info = user_info(g_current_user_id)
    turn_page(11)
    info_str = f'name: {info[1]}phone: {info[3]}email: {info[4]}card: {info[5]}'
    UI.orders.setText(info_str)
    

def modify_user_info():
    turn_page(12)
    alter_item = UI.co_to_modify.currentText()
    alter_value = UI.modify_info.text()
    alter_status = update_user(alter_item, alter_value, g_current_user_id)
    if alter_status != 'update_succeed':
        UI.gridLayout_71.addWidget(QtWidgets.QMessageBox.warning(
            Main, 'Error', alter_status, QtWidgets.QMessageBox.Ok))



        
    
def show_orders_info():
    
        


    
    
    
    
    
    
    
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    Main = QtWidgets.QMainWindow()
    UI = GUI_v1_1.Ui_MainWindow()