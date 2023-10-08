import sqlite3
import backend
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

test_get_user_info()

#2. 通过电话号码和密码，邮箱和密码，或者用户名和密码判断是否登录成功，
#   登录成功返回登录成功信息以及当前用户的user_id，失败返回登录失败原因（用户不存在，密码错误）
def test_user_login():

    #尝试登录
    result = backend.user_login('INT', 'TEXT', 'TEXT', 'TEXT')
    if result:
        print(f"2.登录测试结果为:{result}")
    else:
        print('2、登录测试未通过')

test_user_login()

# 3.通过电话号码，邮箱，用户名，银行卡号和密码注册，注册成功返回注册成功信息并生成唯一的user_id并返回，
# 失败返回注册失败信息，失败原因包括用户名已存在，手机号已存在，邮箱已存在；无需返回失败原因
def test_user_register():
    
    #尝试注册
    result = backend.user_register('phone', 'email', 'user01', 'card', 'pwd')
    if result:
        print(f'3、注册账号测试结果：{result}')
    else:
        print('3、登录测试未通过')

test_user_register()

# 4.通过user_id修改用户信息
def test_update_user():
    #创建测试用户
    user_id = 1
    user_name = 'test'
    user_pwd = 100
    connection = sqlite3.connect('info.db')
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO user (user_id, user_name, user_pwd)
        VALUES (?, ?, ?)
        ''',
        (user_id, user_name, user_pwd))
    
    # 读取原用户信息
    cursor.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
    original_user = cursor.fetchone()
    
    # 修改用户信息
    user_id = 1
    new_user_name = 'test_new'
    new_user_pwd = 200
    backend.update_user(user_id, new_user_name, new_user_pwd)

    # 读取更新后的用户信息
    cursor.execute("SELECT * FROM user WHERE user_id = ?", (user_id,))
    updated_user = cursor.fetchone()
    connection.close()

    # 确认用户信息是否已更新
    if updated_user is not None:
        if updated_user == original_user:
            print("4.用户信息更新未通过")
        else:
            print("4.用户信息更新通过")
    else:
        print("4.无用户信息")

test_update_user()

# 5.通过时间段和房型查找可预定房间
def test_find_available_rooms():
    #查找房间
    ck_in = '2023-10-08'
    ck_out = '2023-10-10'
    room_type = 'single'

    available_rooms = backend.find_available_rooms(ck_in, ck_out, room_type)

    if available_rooms:
        print('5.测试可预定房间查找通过')
    else:
        print('5.测试可预定房间查找未通过')

test_find_available_rooms()

# 6.通过房间号、用户id、入住时间、退房时间创建订单
def test_create_order():
    #创建订单
    room_num = 100
    user_id = 1
    ck_in = '2023-10-08'
    ck_out = '2023-10-10'
    backend.create_order(room_num, user_id, ck_in, ck_out)
    #读取订单
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT FROM orderl WHERE user_id = ?""", (user_id,))
    result = cursor.fetchone()
    conn.commit()
    conn.close()

    if result:
        print("6.测试创建订单通过")
    else:
        print("6.测试创建订单未通过")

test_create_order()

# 7.通过房型返回价格
def test_calculate_price():
    #创建测试房型
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    room_num = 100
    room_type = 'single'
    room_price = 103
    cursor.execute('INSERT INTO room(room_num, room_type, room_price) VALUES (?,?,?)', (room_num, room_type, room_price))
    conn.commit()
    #查找价格
    room_type = 'single'
    price = backend.calculate_price(room_type)
    conn.close()
    if price:
        print("7.测试通过房型返回价格通过")
    else:
        print("7.测试通过房型返回价格未通过")

test_calculate_price()

# 8.通过order_id返回订单信息
def test_get_order_info():
    #创建测试订单
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    order_id = 1
    room_num = 100
    user_id = 100
    ck_in = 100
    ck_out = 100
    order_status = 1
    comment = 'test'
    cursor.execute("""
                   INSERT INTO orderl(order_id=?, room_num=?, user_id=?, ck_in=?, ck_out=?, order_status=?, comment=?) 
                   VALUES(?,?,?,?,?,?,?)
                   """, 
                   (order_id, room_num, user_id, ck_in, ck_out, order_status, comment)
                   )
    conn.commit()
    order_id = 1
    order = backend.get_order_info(order_id)
    conn.close()
    if order:
        print("5.测试返回订单信息通过")
    else:
        print("5.测试返回订单信息未通过")

test_get_order_info()

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

test_update_order()

# 测试10.添加订单评论
def test_comment_order():
    order_id = 1
    new_comment = 'This is a new comment'
    backend.comment_order(order_id, new_comment)

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

test_comment_order()

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

verify_get_all_users()

# 12.返回所有订单信息，包括order表中所有字段所有行
def test_get_all_orders():
    #获取订单信息
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orderl")
    result = cursor.fetchall()

    #获取待测返回信息
    test_result = backend.get_all_orders()
    conn.close()

    #验证获取信息是否一致
    if result and test_result:
        if result == test_result:
            print('12、返回所有订单信息测试通过')
        else:
            print('12、返回所有订单信息测试未通过')
    else:
        print('12、返回所有订单信息测试未通过')

test_get_all_orders()

#13、通过房间号修改房间信息，修改信息可能覆盖room表中所有字段，room_num不可修改
def test_update_room():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    #创建测试房间
    room_num = 100
    room_type = 100
    room_price = 100
    cursor.execute('INSERT INTO room(room_num, room_type, room_price) VALUES (?,?,?)', (room_num, room_type, room_price))
    cursor.execute('SELECT FROM room WHERE room_num = ?', (room_num,))
    result = cursor.fetchone()
    conn.commit()
    
    #修改房间信息
    backend.update_room(room_num, room_type, room_price)

    #确认信息是否已成功修改
    cursor.execute('SELECT FROM room WHERE room_num = ?', (room_num,))
    test_result = cursor.fetchone()
    conn.commit()
    conn.close()
    if result and test_result:
        if result != test_result:
            print('13、修改房间信息测试通过')
        else:
            print('13、修改房间信息测试未通过')
    else:
            print('13、修改房间信息测试未通过')

test_update_room()

# 14.通过房间号返回房间信息，包括room表中所有字段
def test_get_room():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    #创建测试房间
    room_num = 100
    room_type = 101
    room_price = 103
    cursor.execute('INSERT INTO room(room_num, room_type, room_price) VALUES (?,?,?)', (room_num, room_type, room_price))
    cursor.execute('SELECT FROM room WHERE room_num = ?', (room_num,))
    result = cursor.fetchone()
    conn.commit()
    #返回房间信息
    test_result = backend.get_room(room_num)
    conn.close()
    #确认返回信息是否正确
    if result and test_result:
        if result == test_result:
            print('14、返回房间信息测试通过')
        else:
            print('14、返回房间信息测试未通过')
    else:
            print('14、返回房间信息测试未通过')

test_get_room()

# 15、通过用户名和密码新建用户
def test_create_user():
    #新建用户
    user_name = 'test_user'
    user_pwd = 123
    backend.create_user(user_name, user_pwd)
    #检查是否成功新建用户
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    cursor.execute('SELECT FROM user WHERE user_name = ?', (user_name,))
    result = cursor.fetchone()
    conn.close()
    if result:
        print('15、通过用户名和密码新建用户通过')
    else:
        print('15、通过用户名和密码新建用户未通过')

test_create_user()

#16、新建房间，注意房间号不能为空
def test_create_room():
    #新建房间
    room_num = 100
    room_type = 'single'
    room_price = 100
    backend.create_room(room_num, room_type, room_price)
    #检查是否成功新建房间
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    cursor.execute('SELECT FROM room WHERE room_num = ?', (room_num,))
    result = cursor.fetchone()
    conn.close()
    if result:
        print('16、新建房间测试通过')
    else:
        print('16、新建房间测试未通过')

test_create_room()

#17、新建订单
def test_create_room():
    #新建订单
    room_num = 100
    user_id = 100
    ck_in = 230101
    ck_out = 230102
    comment = 'test'
    backend.create_room(room_num, user_id, ck_in, ck_out, comment)
    #检查是否成功新建订单
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    cursor.execute('SELECT FROM orderl WHERE room_num = ?', (room_num,))
    result = cursor.fetchone()
    conn.close()
    if result:
        print('17、新建订单测试通过')
    else:
        print('17、新建订单测试未通过')

test_create_room()

#18、通过房间号删除房间
def test_delete_room():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    #创建测试房间
    room_num = 100
    room_type = 101
    room_price = 103
    cursor.execute('INSERT INTO room(room_num, room_type, room_price) VALUES (?,?,?)', (room_num, room_type, room_price))
    conn.commit()
    #删除测试房间
    backend.delete_room(room_num)
    #检查房间是否删除
    cursor.execute('SELECT FROM room WHERE room_num = ?', (room_num,))
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    if result:
        print('18、通过房间号删除房间未通过')
    else:
        print('18、通过房间号删除房间通过')

test_delete_room()

#19、通过user_id删除订单
def test_delete_order():
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()
    #创建测试订单
    order_id = 100
    room_num = 100
    user_id = 100
    ck_in = 100
    ck_out = 100
    order_status = 1
    comment = 'test'
    cursor.execute("""
                   INSERT INTO orderl(order_id=?, room_num=?, user_id=?, ck_in=?, ck_out=?, order_status=?, comment=?) 
                   VALUES(?,?,?,?,?,?,?)
                   """, 
                   (order_id, room_num, user_id, ck_in, ck_out, order_status, comment)
                   )
    conn.commit()
    #删除测试订单
    backend.delete_order(user_id)
    #检查是否成功删除
    cursor.execute('SELECT FROM orderl WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    conn.commit()
    conn.close()
    if result:
        print('19、通过user_id删除订单未通过')
    else:
        print('19、通过user_id删除订单通过')

test_delete_order()
