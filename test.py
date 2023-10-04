import backend
import sqlite3

# 1.测试1、返回用户信息
def test_get_user_info():
    conn = sqlite3.connect('info.db')
    cur = conn.cursor()

    #获取表中用户信息
    user_id= 1
    cur.execute("""SELECT * FROM user WHERE user_id = ?""",(user_id))
    result = cur.fetchall()

    #测试返回用户信息
    test_result = backend.get_user_info(user_id)
    conn.close()
    
    #确认返回信息是否正确
    if result and test_result:    
        if result == test_result:
            print('1.返回信息测试通过')
        else:
            print('1.返回信息测试未通过')
    else:
        print('1.返回信息测试未通过,无订单信息')

#2. 通过电话号码和密码，邮箱和密码，或者用户名和密码判断是否登录成功，
#   登录成功返回登录成功信息以及当前用户的user_id，失败返回登录失败原因（用户不存在，密码错误）
def test_user_login():

    #尝试登录
    result = backend.user_login('INT', 'TEXT', 'TEXT', 'TEXT')
    if result:
        print(f"2.登录测试结果为:{result}")
    else:
        print('2、登录测试未通过')

# 3.通过电话号码，邮箱，用户名，银行卡号和密码注册，注册成功返回注册成功信息并生成唯一的user_id并返回，
# 失败返回注册失败信息，失败原因包括用户名已存在，手机号已存在，邮箱已存在；无需返回失败原因
def test_user_register():
    
    #尝试注册
    result = backend.user_register('phone', 'email', 'user01', 'card', 'pwd')
    if result:
        print(f'3、注册账号测试结果：{result}')
    else:
        print('3、登录测试未通过')


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

# 12.返回所有订单信息，包括order表中所有字段所有行
def test_get_all_orders():
    #获取订单信息
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orderl")
    result = cursor.fetchall()

    #获取待测返回信息
    test_result = backend.get_all_orders()

    #验证获取信息是否一致
    if result and test_result:
        if result == test_result:
            print('12、返回所有订单信息测试通过')
        else:
            print('12、返回所有订单信息测试未通过')
    else:
        print('12、返回所有订单信息测试未通过')

#13、通过房间号修改房间信息，修改信息可能覆盖room表中所有字段，room_num不可修改
def test_update_room():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    #创建测试房间
    room_num = 000
    room_type = 001
    room_price = 003
    cursor.execute('INSERT INTO room(room_num, room_type, room_price) VALUES (?,?,?)', (000, 000, 000))
    cursor.execute('SELECT FROM room WHERE room_num = ?', (room_num,))
    result = cursor.fetchone()
    conn.commit()
    
    #修改房间信息
    backend.update_room(room_num, room_type, room_price)

    #确认信息是否已成功修改
    cursor.execute('SELECT FROM room WHERE room_num = ?', (room_num,))
    test_result = cursor.fetchone()
    conn.commit()
    if result and test_result:
        if result != test_result:
            print('13、修改房间信息测试通过')
        else:
            print('13、修改房间信息测试未通过')
    else:
            print('13、修改房间信息测试未通过')

#运行测试函数
test_get_user_info()
test_user_login()
test_user_register()
test_update_order()
test_comment_order()
verify_get_all_users()
test_get_all_orders()
test_update_room()
