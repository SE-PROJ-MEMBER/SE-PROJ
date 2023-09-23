import sqlite3

# 通过order_id修改订单信息，修改信息可能覆盖order表中所有字段，order_id不可修改
def update_order_by_id(order_id, new_info):
    conn = sqlite3.connect('database.db')
    conn.execute('UPDATE orders SET order_info = ? WHERE order_id = ?', (new_info, order_id,))
    conn.commit()
    conn.close()

# 通过order_id进行评论，仅状态为2的订单可以评论，否则返回评论失败信息
def add_comment_by_order_id(order_id, comment):
    conn = sqlite3.connect('database.db')
    order_status = conn.execute('SELECT order_status FROM orders WHERE order_id = ?', (order_id,)).fetchone()

    if order_status[0] != 2:
        conn.close()
        return "Only orders with status 2 can be commented"

    conn.execute('UPDATE orders SET comment = ? WHERE order_id = ?', (comment, order_id,))
    conn.commit()
    conn.close()
    return "Comment added successfully"

# 返回所有用户信息，包括user表中所有字段所有行
def get_all_users():
    conn = sqlite3.connect('database.db')
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return users
