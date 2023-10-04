import backend
import sqlite3
# 测试9.更新订单信息
def test_update_order():

    #读取原订单信息
    order_id = 1
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM orderl WHERE order_id = ?", (order_id,))
    original_order = cur.fetchone()
    conn.close()
    
    #更新订单信息
    item_list = ['room_num','user_id', 'ck_in', 'ck_out', 'order_status', 'comment' ]
    value_list = ['102','2','2023-10-1','2023-10-5','2','This is a comment']
    for i in range(5):
        backend.update_order(item_list[i], value_list[i], order_id)

    # 读取更新后订单信息
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orderl WHERE order_id = ?", (order_id,))
    updated_order = cursor.fetchone()
    connection.close()

    #确认订单信息是否已更新
    if updated_order is not None:
        if updated_order == original_order:
            print('9.订单信息未更新')
        else:
            print('9.订单信息已更新')
            for i in range[6]:
                if updated_order[i] == original_order[i]:
                    continue
                else:
                    print(f'原订单信息{original_order[i]}已更新为{updated_order[i]}')
                    continue
    else:
        print('9.无订单信息')

# 测试10.添加订单评论
def test_comment_order():
    order_id = 1
    new_comment = 'This is a new comment'
    comment_result = backend.comment_order(order_id, new_comment)

    # 读取订单评论
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM orderl WHERE order_id = ?", (order_id,))
    order = cursor.fetchone()
    connection.close()
    
    #判断订单评论是否成功修改
    if order is not None:
        if order[6] == new_comment:
            print("10.添加订单评论通过")
        else:
            print("10.添加订单评论失败，读取订单评论与输入评论不符")
    else: 
        print('10.添加订单评论失败，无订单信息')

# 测试11.返回用户信息
def verify_get_all_users():
    # 连接数据库
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()

    # 查询所有用户信息
    cursor.execute("SELECT * FROM user")
    users_from_db = cursor.fetchall()

    # 获取后端返回的用户信息
    users_from_backend = backend.get_all_users()

    # 验证用户信息是否一致
    if users_from_db == users_from_backend:
        print("11.返回所有用户信息通过")
    else:
        print("11.返回所有用户信息失败")

    # 关闭数据库连接
    connection.close()

#运行测试函数

test_update_order()
test_comment_order()
verify_get_all_users()
