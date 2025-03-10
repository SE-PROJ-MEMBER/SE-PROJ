### 函数 1: `get_user_info（）`

**概述：** 获取用户信息。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `user_id (int)`: 用户ID。
- `user_name (int)`: 用户名。
- `user_phone (int)`: 用户手机。
- `user_email (int)`: 用户邮件。
- `user_card (int)`: 用户信用卡。
- `user_pwd (int)`: 用户密码。

**返回值：** user_id。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
cursor = conn.cursor()
user_id = str(uuid.uuid4())
user_info = get_user_info(user_id)
```
### 函数 2: `user_login()`

**概述：** 判断是否登陆成功

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `user_name (int)`: 用户名。
- `user_phone (int)`: 用户手机。
- `user_email (int)`: 用户邮件。
- `user_pwd (int)`: 用户密码。


**返回值：** status ， message

**示例：**

```python
import sqlite3
    if user_data:
        user_id = user_data[0]
        return {"status": "success", "message": "log in successfully", "user_id": user_id}
    else:
        return {"status": "failure", "message": "user doesn't exist or password is wrong"}
```

---
### 函数 3: `user_register()`

**概述：** 判断是否注册成功

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `user_name (int)`: 用户名。
- `user_phone (int)`: 用户手机。
- `user_email (int)`: 用户邮件。
- `user_pwd (int)`: 用户密码。
- `user_card (int)`: 用户银行卡。

**返回值：** status , message。

**示例：**

```python
import sqlite3
if existing_user:
    return {"status": "failure", "message": "fail to register"}
user_id = generate_user_id()
cursor.execute('INSERT INTO user_info VALUES (?, ?, ?, ?, ?, ?)',
                   (user_id, user_name, user_phone, user_email, user_card, user_pwd))
conn.commit()

    return {"status": "success", "message": "rigister successfully", "user_id": user_id}

except Exception as e:
    return {"status": "failure", "message": "fail to register"}
```


### 函数 4: `update_user_info()`

**概述：** 修改用户信息

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `user_id (int)`: 用户id。
- `new_user_phone (int)`: 新用户手机。
- `new_user_email (int)`: 新用户邮件。
- `new_user_pwd (int)`: 新用户密码。
- `new_user_card (int)`: 新用户银行卡。
- `new_user_name (int)`: 新用户名。

**返回值：** status , message。

**示例：**
```python
if not existing_user:
    return {"status": "failure", "message": "user doesn't exist"}
```

### 函数 5: `find_available_rooms() `

**概述：** 查找可预定房间。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `room_type (int)`: 房间类型。
- `ck_in (date)`: 入住日期。
- `ck_out (date)`: 退房日期。
- `price (float)`: 价格。

**返回值：** status，rooms。

**示例：**

```python
import sqlite3
for row in cursor.fetchall():
        room_info = {
            "room_id": row[0],
            "room_type": row[1],
            "price": row[2],
        }
        available_rooms.append(room_info)

    return {"status": "success", "rooms": available_rooms}

except Exception as e:
    return {"status": "failure",
            "message": "failed to find the room can be ordered ,please check the information you enter"}
```

### 函数 6: `create_order() `

**概述：** 返回order_id。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `order_id (int)`: 订单ID。
- `room_num (int)`: 房间号。
- `user_id (int)`: 用户ID。
- `ck_in (date)`: 入住日期。
- `ck_out (date)`: 退房日期。



**返回值：** order_id。

**示例：**

```python
def create_order(room_num, user_id, ck_in, ck_out):
    conn.cursor().execute(
        '''
    INSERT INTO orders (room_num, user_id, ck_in, ck_out) VALUES (?, ?, ?, ?)
    ''',
        (room_num, user_id, ck_in, ck_out)
    )
    order_id = conn.cursor().lastrowid
    conn.commit()
    conn.close()

    return order_id
```

### 函数 7: `calculate_price(room_type, ck_in, ck_out) `

**概述：** 计算价格并返回。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `room_type (int)`: 房间类型。
- `ck_in (date)`: 入住日期。
- `ck_out (date)`: 退房日期。

**返回值：** price。

**示例：**

```python
if result:
    return result[0]
else:
return 'can not find the matched price'
```


### 函数 8: `get_order_info(order_id) `

**概述：** 返回订单信息。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `room_type (int)`: 房间类型。
- `ck_in (date)`: 入住日期。
- `ck_out (date)`: 退房日期。
- `room_num (int)`: 房间号
- `price (int)`: 价格
**返回值：** result。

**示例：**

```python
if result:
    return result
else:
    return 'can"t find the matched order information'
```

### 函数 9: `update_order(conn, order_id, room_num, user_id, ck_in, ck_out, order_status, comment)`

**概述：** 更新订单信息。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `order_id (int)`: 订单ID。
- `room_num (int)`: 房间号。
- `user_id (int)`: 用户ID。
- `ck_in (date)`: 入住日期。
- `ck_out (date)`: 退房日期。
- `order_status (int)`: 订单状态。
- `comment (string)`: 评论。

**返回值：** 无。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
update_order(conn, 1, 101, 1, "2023-10-01", "2023-10-10", 1, "Great room!")
```

---

### 函数 10: `comment_order(order_id, comment_str)`

**概述：** 添加订单评论。

**参数：**

- `order_id (int)`: 订单ID。
- `comment_str (str)`: 评论。

**返回值：**

- 如果订单状态为2（已退房），返回字符串 "200"。
- 如果订单状态不为2，返回字符串 "Failed"。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
comment_order(1, "Great room!")
```

---

### 函数 11: `get_all_users()`

**概述：** 获取所有用户信息。

**参数：**

无

**返回值：** 返回一个包含所有用户信息的列表，每个用户的信息是一个包含`user`表中所有字段的元组。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
print(get_all_users())  # 输出: [(1, "John Doe", 1234567890, "john.doe@example.com", 1234567890123456, "password"), ...]
```

---
---

### 函数 12: `get_all_orders()`

**概述：** 获取所有订单信息。

**参数：**

无

**返回值：** 返回一个包含所有订单信息的列表，每个订单的信息是一个包含`orderl`表中所有字段的元组。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
print(get_all_orders())  # 输出: [(1, 101, 1, "2023-10-01", "2023-10-10", 1, "Great room!"), ...]
```

---

### 函数 13: `update_room(alter_item, alter_value, room_num)`

**概述：** 更新房间信息。

**参数：**

- `alter_item(str)`: 要更新的项目
- `alter_value(str)`: 更新后的值
- `room_num(int)`: 房间号

**返回值：** 无。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
update_room(conn, 101, 2, 500.0)
```

---

### 函数 14: `get_room_info(room)`

**概述：** 获取特定房间的信息。

**参数：**

- `room (int)`: 房间编号。

**返回值：** 一个包含特定房间信息的元组，包含`room`表中所有字段。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
print(get_room_info(101))  # 输出: (101, 2, 500.0)
```

---


## 15. create_user_np(name, pwd)

此函数用于通过用户名和密码创建新的用户。

### 参数：

- `user_name`: 新用户的用户名，必须为字符串类型。
- `user_pwd`: 新用户的密码，必须为字符串类型。

### 返回值：

无返回值。

### 例子：

```python
create_user("JohnDoe", "password123")
```

在上述例子中，函数将在数据库中创建一个新的用户，其用户名为"JohnDoe"，密码为"password123"。

### 备注：

在此函数中，我们生成一个在10000000到99999999之间的随机`user_id`作为用户的唯一标识。我们在数据库中检查这个`user_id`是否唯一，如果不唯一，我们会再次生成新的`user_id`。

---

## 16. create_room(room_num, room_type, room_price)

此函数用于创建新的房间。

### 参数：

- `room_num`: 新房间的房间号, 必须为三位数的整数
- `room_type`: 新房间的类型
- `room_price`: 新房间的价格

### 返回值：

如果房间号已存在, 返回信息'room already existed'
如果房间号不是三位数, 返回信息'invalid room number'
如果成功创建, 返回'200'

### 例子：

```python
create_room(101, 'A', 100)
```

在上述例子中，函数将在数据库中创建一个新的房间，其房间号为101，类型为'A'，价格为100。

---

## 17. create_order(item, value)

此函数用于创建新的订单

### 参数

- `item`: 提供的信息项目
- `value`: 对应项目的值

### 返回值

成功则返回200

### 例子

```python
create_order('room_num', 103)
```

---

## 18. delete_room(room_num)

此函数用于删除房间

### 参数

- `room_num`: 要删除的房间

### 返回值

成功则返回200

### 例子

```python
delete_room(102)
```

---

## 19. delete_user(user_id)

此函数用于删除用户

### 参数

- `user_id`: 用户ID

### 返回值

成功则返回200

### 例子

```python
delete_user(12345678)
```