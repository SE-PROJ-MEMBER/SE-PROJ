import sqlite3
import uuid
# 1. 返回用户信息
def get_user_info(user_id):
    try:
        conn =sqlite3.connect('user_database.db')
        cursor = conn.cursor()

        # 查询信息
        cursor.execute('SELECT * FROM user_info WHERE user_id = ?'), (user_id,)
        user_data = cursor.fetchone()

        if user_data:
            user_info = {
                "user_id": user_data[0],
                "username": user_data[1],
                "phone": user_data[2],
                "email": user_data[3],
                "bank_card": user_data[4],
                "password": user_data[5],
            }
            return user_info
        else:
            return {"error": "用户不存在"}

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
    

# 3.注册成功返回user_id,失败返回原信息
    




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
