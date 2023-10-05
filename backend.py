import sqlite3
from connect import cursor as cur
from connect import conn
import random


# 1.返回用户信息
def user_info(user_id):
    cur.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
    return cur.fetchone()


# 2.登录判断
def user_login(login_info, pwd):
    cur.execute(
        f"SELECT user_id FROM user WHERE {login_info} = ?, "(login_info,))
    id = cur.fetchone()
    if not id:
        return 'user_not_exist'
    cur.execute(f"SELECT user_pwd FROM user WHERE user_id = ?, "(id,))
    if cur.fetchone() == pwd:
        return 'login_succeed', id
    else:
        return 'pwd_incorrect'


# 3.注册
def user_register(phone, email, name, card, pwd):
    if name in cur.execute("SELECT user_name FROM user"):
        return 'user_name_exist'
    if name[:4] == 'admin':
        return 'user_name_invalid'
    id = random.randint(10000000, 99999999)
    cur.execute("INSERT INTO user VALUES(?,?,?,?,?,?)",
                (id, name, phone, email, card, pwd))
    conn.commit()
    return 'register_succeed', id


# 4.修改用户信息
def update_user(alter_item, alter_value, user_id):
    if alter_item == 'name' and alter_value[:4] == 'admin':
        return 'invalid_name'
    if alter_item == 'name' and alter_value in cur.execute("SELECT user_name FROM user"):
        return 'name_exist'
    cur.execute(
        f"UPDATE user SET {alter_item} = ? WHERE user_id = ?", (alter_value, user_id))
    conn.commit()
    return 'update_succeed'


# 5.返回房间信息
def find_room(ck_in, ck_out, type):
    cur.execute(
        '''
        SELECT * FROM room WHERE room_type=? AND room_nun NOT IN (SELECT room_num FROM orderl WHERE ck_in <= ? AND ck_out >= ? )
        ''',
        (type, ck_out, ck_in)
    )
    return cur.fetchall()


# 6.返回订单信息
def create_order(room_num, user_id, ck_in, ck_out):
    order_id = random.randint(10000000, 99999999)
    cur.execute(
        "INSERT INTO orderl VALUES(?,?,?,?,?,?,?)", (order_id, room_num, user_id, ck_in, ck_out, 0, ''))
    conn.commit()
    return 'create_order_succeed', order_id


# 7.返回价格
def get_price(type):
    cur.execute("SELECT room_price FROM room WHERE room_type = ?", (type,))
    return cur.fetchone()


# 8.返回订单信息
def get_order_info(order_id):
    cur.execute("SELECT * FROM orderl WHERE order_id = ?", (order_id,))
    return cur.fetchone()


# 9.更新订单信息
def update_order(alter_item, alter_value, order_id):
    cur.execute(
        f"UPDATE orderl SET {alter_item} = ? WHERE order_id = ?", (alter_value, order_id))
    cur.commit()
    return 'update_succeed'

# 查询订单信息的函数
def get_order_info(order_id):
    cursor.execute('''
        SELECT order_id, room_num, ck_in, ck_out, room_type, price
        FROM orders
        WHERE order_id = ?
    ''', (order_id,))

    result = cursor.fetchone()

    if result:
        return result
    else:
        return 'can"t find the matched order information'

# 用户输入订单号
order_id = int(input('please enter the order_id：'))

# 获取订单信息并返回
order_info = get_order_info(order_id)

if order_info != '未找到匹配的订单信息':
    print('order_id:', order_info[0])
    print('room_num:', order_info[1])
    print('ck_in:', order_info[2])
    print('ck_out:', order_info[3])
    print('room_type:', order_info[4])
    print('price:', order_info[5])
else:
    print(order_info)

conn.close()

# 9. 更新订单信息
def update_order(conn, order_id, room_num=None, user_id=None, ck_in=None, ck_out=None, order_status=None, comment=None):
    try:
        cursor = conn.cursor()
        query = 'UPDATE orderl SET '
        params = []
        
        if room_num is not None:
            query += 'room_num = ?, '
            params.append(room_num)
        
        if user_id is not None:
            query += 'user_id = ?, '
            params.append(user_id)
        
        if ck_in is not None:
            query += 'ck_in = ?, '
            params.append(ck_in)
        
        if ck_out is not None:
            query += 'ck_out = ?, '
            params.append(ck_out)
        
        if order_status is not None:
            query += 'order_status = ?, '
            params.append(order_status)
        
        if comment is not None:
            query += 'comment = ?, '
            params.append(comment)
        
        query = query.rstrip(', ')  # Remove trailing comma and space
        query += ' WHERE order_id = ?'
        params.append(order_id)

        cursor.execute(query, params)
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")


# 10. 添加订单评论
def comment_order(order_id, comment):
    cursor = conn.cursor()
    cursor.execute('SELECT order_status FROM orderl WHERE order_id = ?', (order_id,))
    result = cursor.fetchone()
    if result and result[0] == 2:
        cursor.execute('UPDATE orderl SET comment = ? WHERE order_id = ?', (comment, order_id))
        conn.commit()
        return "Comment posted successfully."
    else:
        return "Cannot comment on this order. Only orders with status 2 can be commented."


# 11. 获取所有用户信息
def get_all_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    return cursor.fetchall()


import sqlite3


# 12.返回所有订单信息
def get_all_orders():
    with sqlite3.connect('info.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orderl")
        result = cursor.fetchall()
        cursor.close()
        return result


# 13.通过房间号修改房间信息
def update_room(alter_item, alter_value, room_num):
    cur.execute(
        f"UPDATE orderl SET {alter_item} = ? WHERE room_num = ?", (alter_value, room_num))
    conn.commit()
    return 'update_succeed'


# 14.通过房间号返回房间信息
def get_room(room_num):
    with sqlite3.connect('info.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM room WHERE room_num=?', (room_num,))
        result = cursor.fetchone()
        cursor.close()
    return result


if __name__ == '__main__':
    res = get_all_orders()

    for r in res:
        print(r)

import random


# 15. 通过用户名和密码新建用户
def create_user(user_name, user_pwd):
    cursor = conn.cursor()
    while True:
        user_id = random.randint(1000, 9999)  # Generate a random user_id
        cursor.execute('SELECT * FROM user WHERE user_id = ?', (user_id,))
        if not cursor.fetchone():
            break
    cursor.execute(
        '''
        INSERT INTO user (user_id, user_name, user_pwd)
        VALUES (?, ?, ?)
        ''',
        (user_id, user_name, user_pwd)
    )
    conn.commit()
    cursor.close()


# 16. 新建房间
def create_room(room_num, room_type=None, room_price=None):
    if not 100 <= room_num <= 999:  # Ensure room_num is a three-digit number
        raise ValueError("Room number must be a three-digit number.")

    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO room (room_num, room_type, room_price)
        VALUES (?, ?, ?)
        ''',
        (room_num, room_type, room_price)
    )
    conn.commit()
    cursor.close()

# 17.新建订单
def create_room(room_num, user_id, ck_in, ck_out, comment):
    cur = conn.cursor()
    import random
    order_id = random.randint(1,1000)
    order_status = 0
    cur.execute("""
                INSERT INTO orderl(order_id, room_num, user_id, ck_in, ck_out, order_status, comment) 
                VALUES(?,?,?,?,?,?,?)
                """, 
                (order_id, room_num, user_id, ck_in, ck_out, order_status, comment)
    )
    conn.commit()
    cur.close()


# 18.通过房间号删除房间（删除相应行）
def delete_room(room_num):
    cur = conn.cursor()
    cur.execute("""
                DELETE FROM room WHERE room_num = ?
                """,
                (room_num,)
    )
    conn.commit()
    cur.close()

# 19.通过user_id删除订单（删除相应行）
def delete_order(user_id):
    cur = conn.cursor()
    cur.execute("""
                DELETE FROM orderl WHERE user_id = ?
                """,
                (user_id,)
    )
    conn.commit()
    cur.close()
