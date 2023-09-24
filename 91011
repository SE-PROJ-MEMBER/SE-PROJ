import sqlite3

# 创建数据库连接
conn = sqlite3.connect('info.db')

# 9. 通过order_id修改订单信息
def update_order(order_id, update_data):
    cursor = conn.cursor()
    keys = ', '.join(f'{k}=?' for k in update_data.keys())
    values = tuple(update_data.values())
    sql = f'UPDATE order SET {keys} WHERE order_id=?'
    cursor.execute(sql, values + (order_id,))
    conn.commit()

# 10. 通过order_id进行评论
def comment_order(order_id, comment):
    cursor = conn.cursor()
    cursor.execute('SELECT order_status FROM order WHERE order_id = ?', (order_id,))
    result = cursor.fetchone()
    if result is None or result[0] != 2:
        return "Cannot comment on this order. Only orders with status 2 can be commented."
    cursor.execute("UPDATE order SET comment = ? WHERE order_id = ?", (comment, order_id))
    conn.commit()
    return "Comment posted successfully."

# 11. 返回所有用户信息
def get_all_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user")
    return cursor.fetchall()
