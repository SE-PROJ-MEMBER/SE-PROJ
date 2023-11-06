import sqlite3
from connect import cursor as cur
from connect import conn
import random
from encrypt import *


# 1.返回用户信息pass
def user_info(user_id):
    '''需解密'''
    cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
    return cur.fetchone()


# 2.登录判断pass
def user_login(login_item, login_info, pwd):
    '''无需解密'''
    cur.execute(
        f"SELECT user_id FROM user WHERE {login_item} = ?", (encrypt(login_info),))
    id = cur.fetchone()
    
    if id == None:
        return 'user_not_exist'
    cur.execute(f"SELECT user_pwd FROM user WHERE user_id = ?", (id[0],))
    if cur.fetchone()[0] == encrypt(pwd):
        return '200', id[0]
    else:
        return 'pwd_incorrect'


# 3.注册pass
def user_register(phone, email, name, card, pwd):
    '''无需解密'''
    if name[:5] == 'admin':
        return 'user_name_invalid'
    cur.execute("SELECT user_name FROM user")
    namelist = cur.fetchall()
    if (encrypt(name),) in namelist:
        return 'user_name_exist'
    id = random.randint(10000000, 99999999)
    cur.execute("INSERT INTO user VALUES(?,?,?,?,?,?)",
                (id, encrypt(name), encrypt(phone), encrypt(email), encrypt(card), encrypt(pwd)))
    add(pwd)
    add(card)
    add(phone)
    add(email)
    add(name)
    conn.commit()
    return '200', id


# 4.修改用户信息pass
def update_user(alter_item, alter_value, user_id):
    '''无需解密'''
    if alter_item == 'user_name' and alter_value[:5] == 'admin':
        return 'invalid_name'
    cur.execute("SELECT user_name FROM user")
    namelist = cur.fetchall()
    if alter_item == 'user_name' and (encrypt(alter_value),) in namelist:
        return 'name_exist'
    cur.execute(
        f"UPDATE user SET {alter_item} = ? WHERE user_id = ?", (encrypt(alter_value), user_id))
    conn.commit()
    return '200'


# 5.返回房间信息pass
def find_room(ck_in, ck_out, type):
    '''需解密'''
    cur.execute(
        '''
        SELECT * FROM room WHERE room_type=? AND room_num NOT IN (SELECT room_num FROM orderl WHERE ck_in < ? AND ck_out > ?  AND order_status!= 3  )
        ''',
        (encrypt(type), ck_out, ck_in)
    )

    add(type)
    return cur.fetchall()

# 6.创建订单信息pass


def create_order(room_num, user_id, ck_in, ck_out):
    '''无需解密'''
    order_id = random.randint(10000000, 99999999)
    cur.execute(
        "INSERT INTO orderl VALUES(?,?,?,?,?,?,?)", (order_id, encrypt(room_num), user_id, ck_in, ck_out, 0, ''))
    conn.commit()
    add(room_num)
    return '200', order_id


# 7.返回价格pass
def get_price(num):
    '''无需解密'''
    cur.execute("SELECT room_price FROM room WHERE room_num = ?",
                (encrypt(num),))
    price = cur.fetchone()[0]
    return int(decrypt(price))


# 8.返回订单信息pass
def get_order_info(order_id):
    '''需解密'''
    cur.execute("SELECT * FROM orderl WHERE order_id = ?", (order_id,))
    return cur.fetchone()


# 9.更新订单信息pass
def update_order(alter_item, alter_value, order_id):
    '''无需解密'''
    cur.execute(
        f"UPDATE orderl SET {alter_item} = ? WHERE order_id = ?", (encrypt(alter_value), order_id))
    conn.commit()
    add(alter_value)
    return '200'


# 10. 添加订单评论pass
def comment_order(order_id, comment_str):
    '''无需解密'''
    cur.execute(f'SELECT order_status FROM orderl WHERE order_id = {order_id}')
    status = cur.fetchone()
    if status[0] == 2:
        cur.execute(f'UPDATE orderl SET comment = ? WHERE order_id = ?',
                    (encrypt(comment_str), order_id))
        conn.commit()
        add(comment_str)
        return '200'
    else:
        return 'status_error'


# 11. 获取所有用户信息pass
def get_all_users():
    '''需解密'''
    cur.execute("SELECT * FROM user")
    return cur.fetchall()


# 12.返回所有订单信息pass
def get_all_orders():
    '''需解密'''
    cur.execute("SELECT * FROM orderl")
    return cur.fetchall()


# 13.通过房间号修改房间信息pass
def update_room(alter_item, alter_value, room_num):
    '''无需解密'''
    cur.execute(
        f"UPDATE room SET {alter_item} = ? WHERE room_num = ?", (encrypt(alter_value), encrypt(room_num)))
    conn.commit()
    add(alter_value)
    add(room_num)
    return '200'


# 14.通过房间号返回房间信息pass
def get_room_info(room):
    '''需解密'''
    cur.execute(f'SELECT * FROM room WHERE room_num = {encrypt(room)}')
    return cur.fetchone()


# 15. 通过用户名和密码新建用户pass
def create_user_np(name, pwd):
    '''无需解密'''
    new_id = random.randint(10000000, 99999999)
    cur.execute('SELECT user_name FROM user')
    namelist = cur.fetchall()
    if (encrypt(name),) in namelist:
        return 'user_name_exist'
    cur.execute('''
                INSERT INTO user VALUES (?, ?, NULL, NULL, NULL, ?)
                ''',
                (new_id, encrypt(name), encrypt(pwd)))
    conn.commit()
    add(pwd)
    add(name)
    return '200'


# 16. 新建房间pass
def create_room(room_num, room_type, price):
    '''无需解密'''
    cur.execute('SELECT room_num FROM room')
    result = cur.fetchall()
    if (encrypt(room_num),) in result:
        return 'room already existed'
    if room_num < 100 or room_num > 999:
        return 'invalid room number'
    cur.execute('''
                INSERT INTO room VALUES (?, ?, ?)
                ''',
                (encrypt(room_num), encrypt(room_type), encrypt(price)))
    conn.commit()
    add(room_num)
    add(room_type)
    add(price)
    return '200'


# 17.新建订单pass
def create_order_admin(item, value):
    '''无需解密'''
    new_id = random.randint(10000000, 99999999)
    cur.execute(
        f'INSERT INTO orderl VALUES ({new_id}, NULL, NULL, NULL, NULL, NULL, NULL)')
    cur.execute(
        f'UPDATE orderl SET {item} = {encrypt(value)} WHERE order_id = {new_id}')
    add(value)
    conn.commit()
    return '200'


# 18.通过房间号删除房间（删除相应行）pass
def delete_room(room_num):
    '''无需解密'''
    cur.execute("""
                DELETE FROM room WHERE room_num = ?
                """,
                (encrypt(room_num,))
                )
    conn.commit()
    return '200'


# 19.通过user_id删除用户（删除相应行）pass
def delete_user(user_id):
    '''无需解密'''
    cur.execute("""
                DELETE FROM user WHERE user_id = ?
                """,
                (user_id,)
                )
    conn.commit()
    return '200'


# 20.通过user_id返回订单信息pass
def get_orders_of_user(user_id):
    '''需解密'''
    cur.execute(f'SELECT * FROM orderl WHERE user_id = {user_id}')
    info = cur.fetchall()
    if info == []:
        return 'no order'
    return info


# 21.返回所有房间信息
def get_all_rooms():
    '''需解密'''
    cur.execute('SELECT * FROM room')
    return cur.fetchall()


# 22.
def user_ser(name):
    '''需解密'''
    cur.execute(
        f"SELECT * FROM user WHERE user_name = ?", (encrypt(name),))
    user_info = cur.fetchone()
    if user_info == None:
        return 'user_not_exist'
    return user_info
