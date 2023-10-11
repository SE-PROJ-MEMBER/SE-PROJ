from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import GUI_v1_1
from backend import *


g_current_user_id = 0
g_sign_in_status = False
g_admin_status = False
g_pre_page = 0


def show_current_order():
    '''need info from page 7'''
    pass


def calculate_price():
    '''need info from page 7'''
    pass


def show_current_user_email():
    '''billed to'''
    return user_info(g_current_user_id)[3]

