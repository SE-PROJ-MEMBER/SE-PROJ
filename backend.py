import sqlite3
import uuid
# 1. 返回用户信息
def get_user_info(user_id):
    conn =  sqlite3.connect('info.db')
    cursor = conn.cursor()
    try:
# 查询信息
        cursor.execute('SELECT * FROM user_info WHERE user_id = ?'), (user_id,)
        user_data = cursor.fetchone()

        if user_data:
            user_info = {
                "user_id": user_data[0],
                "user_name": user_data[1],
                "user_phone": user_data[2],
                "user_email": user_data[3],
                "user_card": user_data[4],
                "user_pwd": user_data[5],
            }
            return user_info
        else:
            return {"error": "user doesn't exist"}

    except Exception as e:
        return {"error": str(e)}
# 生成唯一的user_id
user_id = str(uuid.uuid4())
user_info = get_user_info(user_id)
if "error" in user_info:
    print(user_info["error"])
else:
    print(user_info)

# 2.判断是否登陆成功（返回失败原因）
def user_login(user_phone=None, user_email=None, user_name=None, user_pwd=None):
    if user_phone:
        cursor.execute('SELECT * FROM user_info WHERE user_phone=? AND user_pwd=?',(user_phone, user_pwd))
    elif user_email:
        cursor.execute('SELECT * FROM user_info WHERE user_email=? AND user_pwd=?', (user_email, user_pwd))
    elif user_name:
        cursor.execute('SELECT * FROM user_info WHERE user_name=? AND user_pwd=?', (user_name, user_pwd))
    else:
        return {"status": "failure", "message": "user_pwd or user_name is empty"}

    user_data = cursor.fetchone()

    if user_data:
        user_id = user_data[0]
        return {"status": "success", "message": "log in successfully", "user_id": user_id}
    else:
        return {"status": "failure", "message": "user doesn't exist or password is wrong"}

# 3.注册成功返回user_id,失败返回原信息
def user_register(user_phone, user_email, user_name, user_card, user_pwd):
    try:
        cursor.execute('SELECT * FROM user_info WHERE user_phone=? OR user_email=? OR user_name = ? OR user_card=?',(user_phone, user_email, user_name, user_card))
        existing_user = cursor.fetchone()

        if existing_user:
            return {"status": "failure","message": "fail to register"}
#生成唯一的user_id
        user_id = generate_user_id()
        cursor.execute('INSERT INTO user_info VALUES (?, ?, ?, ?, ?, ?)',(user_id, user_name, user_phone, user_email, user_card, user_pwd))
        conn.commit()

        return {"status": "success", "message": "rigister successfully", "user_id": user_id}

    except Exception as e:
        return {"status": "failure", "message": "fail to register"}

# 4.通过user_id修改用户信息
def update_user_info(user_id, new_user_phone=None, new_user_email= None, new_user_name=None, new_user_card=None, new_user_pwd=None):
    try:
#检查用户是否存在
        cursor.execute('SELECT * FROM user_info WHERE user_id=?', (user_id,))
        existing_user = cursor.fetchone()

        if not existing_user:
            return {"status": "failure","message": "user doesn't exist"}
#更新用户信息
        update_query = 'UPDATE user_info SET'
        update_valuse = []

        if new_user_phone:
            update_query += ' user_phone=?,'
            update_valuse.append(new_user_phone)
        if new_user_email:
            update_query += ' user_email=?,'
            update_valuse.append(new_email)
        if new_user_name:
            update_query += ' user_name=?,'
            update_valuse.append(new_username)
        if new_user_card:
            update_query += ' user_card=?,'
            update_valuse.append(new_bank_card)
        if new_user_pwd:
            update_query += ' user_pwd=?,'
            update_valuse.append(new_password)

        update_query = update_query.rstrip(',')

        update_query += ' WHERE user_id=?'
        update_valuse.append(user_id)
        cursor.execute(update_query,tuple(update_valuse))
        conn.commit()

        return {"status": "success","message": "user's information has been changed successfully"}
    except Exception as e:
        return {"status": "failure","message": "failed to change the information"}

# 5. 查找可预定房间
def find_available_rooms(ck_in, ck_out, room_type):
    try:
# 查询可预定的房间
        cursor.execute('''SELECT * FROM room WHERE room_type=? AND room_id NOT IN (SELECT room_id FROM reservation WHERE ck_in <= ? AND ck_out >= ?)''', (room_type, ck_out, ck_in))

        available_rooms = []
        for row in cursor.fetchall():
            room_info = {
                "room_id": row[0],
                "room_type": row[1],
                "price": row[2],
            }
            available_rooms.append(room_info)

        return {"status": "success", "rooms": available_rooms}

    except Exception as e:
        return {"status": "failure", "message": "failed to find the room can be ordered ,please check the information you enter"}

# 6.返回order_id
def create_order(room_number, user_id, ck_in, ck_out):
    conn.cursor().execute('''INSERT INTO orders (room_number, user_id, ck_in, ck_out) VALUES (?, ?, ?, ?)''', (room_number, user_id, ck_in, ck_out))
    order_id = conn.cursor().lastrowid
    conn.commit()
    conn.close()

    return order_id


# 9. 更新订单信息
def update_order(order_id, room_num, user_id, ck_in, ck_out, order_status, comment):
    cursor = conn.cursor()
    cursor.execute(
        '''
        UPDATE orderl 
        SET room_num=?, user_id=?, ck_in=?, ck_out=?, order_status=?, comment=? 
        WHERE order_id=?
        ''',
        (room_num, user_id, ck_in, ck_out, order_status, comment, order_id)
    )
    conn.commit()

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
def update_room(room_num, room_type, room_price):
    with sqlite3.connect('info.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            '''
            UPDATE room
            SET room_type=?, room_price=? 
            WHERE room_num=?
            ''',
            (room_type, room_price, room_num)
        )
        conn.commit()
        cursor.close()


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
