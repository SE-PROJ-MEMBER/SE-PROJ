import sqlite3
from connect import cursor as cur
from connect import conn
import random


# 1.返回用户信息pass
def user_info(user_id):
    cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
    return cur.fetchone()


# 2.登录判断pass
def user_login(login_item, login_info, pwd):
    cur.execute(
        f"SELECT user_id FROM user WHERE {login_item} = ?",(login_info,))
    id = cur.fetchone()
    if id == None:
        return 'user_not_exist'
    cur.execute(f"SELECT user_pwd FROM user WHERE user_id = ?",(id[0],))
    if cur.fetchone()[0] == pwd:
        return '200', id[0]
    else:
        return 'pwd_incorrect'


# 3.注册pass
def user_register(phone, email, name, card, pwd):
    cur.execute("SELECT user_name FROM user")
    namelist = cur.fetchall()  
    if (name,) in namelist:
        return 'user_name_exist'
    if name[:5] == 'admin':
        return 'user_name_invalid'
    id = random.randint(10000000, 99999999)
    cur.execute("INSERT INTO user VALUES(?,?,?,?,?,?)",
                (id, name, phone, email, card, pwd))
    conn.commit()
    return '200', id


# 4.修改用户信息pass
def update_user(alter_item, alter_value, user_id):
    if alter_item == 'user_name' and alter_value[:5] == 'admin':
        return 'invalid_name'
    cur.execute("SELECT user_name FROM user")
    namelist = cur.fetchall()
    if alter_item == 'user_name' and (alter_value,) in namelist:
        return 'name_exist'
    cur.execute(
        f"UPDATE user SET {alter_item} = ? WHERE user_id = ?", (alter_value, user_id))
    conn.commit()
    return '200'


# 5.返回房间信息pass
def find_room(ck_in, ck_out, type):
    cur.execute(
        '''
        SELECT * FROM room WHERE room_type=? AND room_num NOT IN (SELECT room_num FROM orderl WHERE ck_in < ? AND ck_out > ? )
        ''',
        (type, ck_out, ck_in)
    )
    return cur.fetchall()

# 6.创建订单信息pass
def create_order(room_num, user_id, ck_in, ck_out):
    order_id = random.randint(10000000, 99999999)
    cur.execute(
        "INSERT INTO orderl VALUES(?,?,?,?,?,?,?)", (order_id, room_num, user_id, ck_in, ck_out, 0, ''))
    conn.commit()
    return '200', order_id


# 7.返回价格pass
def get_price(num):
    cur.execute("SELECT room_price FROM room WHERE room_num = ?", (num,))
    return cur.fetchone()[0]


# 8.返回订单信息pass
def get_order_info(order_id):
    cur.execute("SELECT * FROM orderl WHERE order_id = ?", (order_id,))
    return cur.fetchone()


# 9.更新订单信息pass
def update_order(alter_item, alter_value, order_id):
    cur.execute(
        f"UPDATE orderl SET {alter_item} = ? WHERE order_id = ?", (alter_value, order_id))
    conn.commit()
    return '200'


# 10. 添加订单评论pass
def comment_order(order_id, comment_str):
    cur.execute(f'SELECT order_status FROM orderl WHERE order_id = {order_id}')
    status = cur.fetchone()
    if status[0] == 2:
        cur.execute(f'UPDATE orderl SET comment = ? WHERE order_id = ?', (comment_str, order_id))
        conn.commit()
        return '200'
    else:
        return 'status_error'


# 11. 获取所有用户信息pass
def get_all_users():
    cur.execute("SELECT * FROM user")
    return cur.fetchall()


# 12.返回所有订单信息pass
def get_all_orders():
    cur.execute("SELECT * FROM orderl")
    return cur.fetchall()


# 13.通过房间号修改房间信息pass
def update_room(alter_item, alter_value, room_num):
    cur.execute(
        f"UPDATE room SET {alter_item} = ? WHERE room_num = ?", (alter_value, room_num))
    conn.commit()
    return '200'


# 14.通过房间号返回房间信息pass
def get_room_info(room: int):
    cur.execute(f'SELECT * FROM room WHERE room_num = {room}')
    return cur.fetchone()


# 15. 通过用户名和密码新建用户pass
def create_user_np(name, pwd):
    new_id = random.randint(10000000, 99999999)
    # cur.execute('SELECT user_id FROM user')
    # tmp = cur.fetchall()
    # while new_id in tmp:
        # new_id = random.randint(10000000, 99999999)
    cur.execute('SELECT user_id FROM user')
    namelist = cur.fetchall()
    if (name,) in namelist:
        return 'user_name_exist'
    cur.execute('''
                INSERT INTO user VALUES (?, ?, NULL, NULL, NULL, ?)
                ''',
                (new_id, name, pwd))
    conn.commit()
    return '200'


# 16. 新建房间pass
def create_room(room_num, room_type, price):
    cur.execute('SELECT room_num FROM room')
    result = cur.fetchall()
    if (room_num,) in result:
        return 'room already existed'
    if room_num < 100 or room_num > 999:
        return 'invalid room number'
    cur.execute('''
                INSERT INTO room VALUES (?, ?, ?)
                ''',
                (room_num, room_type, price))
    conn.commit()
    return '200'

# 17.新建订单pass
def create_order_admin(item, value):
    new_id = random.randint(10000000, 99999999)
    # cur.execute('SELECT order_id FROM orderl')
    # tmp = cur.fetchall()
    # while new_id in tmp:
        # new_id = random.randint(10000000, 99999999)
    cur.execute(f'INSERT INTO orderl VALUES ({new_id}, NULL, NULL, NULL, NULL, NULL, NULL)')
    cur.execute(f'UPDATE orderl SET {item} = {value} WHERE order_id = {new_id}')
    conn.commit()
    return '200'


# 18.通过房间号删除房间（删除相应行）pass
def delete_room(room_num):
    cur.execute("""
                DELETE FROM room WHERE room_num = ?
                """,
                (room_num,)
    )
    conn.commit()
    return '200'


# 19.通过user_id删除用户（删除相应行）pass
def delete_user(user_id):
    cur.execute("""
                DELETE FROM user WHERE user_id = ?
                """,
                (user_id,)
    )
    conn.commit()
    return '200'


# 20.通过user_id返回订单信息pass
def get_orders_of_user(user_id):
    cur.execute(f'SELECT * FROM orderl WHERE user_id = {user_id}')
    info = cur.fetchall()
    if info == []:
        return 'no order'
    return info


# 21.返回所有房间信息
def get_all_rooms():
    cur.execute('SELECT * FROM room')
    return cur.fetchall()