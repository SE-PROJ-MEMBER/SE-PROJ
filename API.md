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

### 函数 10: `comment_order(conn, order_id, comment)`

**概述：** 添加订单评论。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `order_id (int)`: 订单ID。
- `comment (string)`: 评论。

**返回值：**

- 如果订单状态为2（已退房），返回字符串 "Comment posted successfully."。
- 如果订单状态不为2，返回字符串 "Cannot comment on this order. Only orders with status 2 can be commented."。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
print(comment_order(conn, 1, "Great room!"))  # 输出: "Comment posted successfully."
```

---

### 函数 11: `get_all_users(conn)`

**概述：** 获取所有用户信息。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。

**返回值：** 返回一个包含所有用户信息的列表，每个用户的信息是一个包含`user`表中所有字段的元组。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
print(get_all_users(conn))  # 输出: [(1, "John Doe", 1234567890, "john.doe@example.com", 1234567890123456, "password"), ...]
```

---
---

### 函数 12: `get_all_orders(conn)`

**概述：** 获取所有订单信息。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。

**返回值：** 返回一个包含所有订单信息的列表，每个订单的信息是一个包含`orderl`表中所有字段的元组。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
print(get_all_orders(conn))  # 输出: [(1, 101, 1, "2023-10-01", "2023-10-10", 1, "Great room!"), ...]
```

---

### 函数 13: `update_room(conn, room_num, room_type, room_price)`

**概述：** 更新房间信息。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `room_num (int)`: 房间编号。
- `room_type (int)`: 房间类型。
- `room_price (float)`: 房间价格。

**返回值：** 无。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
update_room(conn, 101, 2, 500.0)
```

---

### 函数 14: `get_room(conn, room_num)`

**概述：** 获取特定房间的信息。

**参数：**

- `conn (sqlite3.Connection)`: SQLite数据库的连接实例。
- `room_num (int)`: 房间编号。

**返回值：** 一个包含特定房间信息的元组，包含`room`表中所有字段。

**示例：**

```python
import sqlite3
conn = sqlite3.connect('info.db')
print(get_room(conn, 101))  # 输出: (101, 2, 500.0)
```

---


## 15. create_user(user_name, user_pwd)

此函数用于创建新的用户。

### 参数：

- `user_name`：新用户的用户名，必须为字符串类型。
- `user_pwd`：新用户的密码，必须为字符串类型。

### 返回值：

无返回值。

### 例子：

```python
create_user("JohnDoe", "password123")
```

在上述例子中，函数将在数据库中创建一个新的用户，其用户名为"JohnDoe"，密码为"password123"。

### 备注：

在此函数中，我们生成一个在1000到9999之间的随机`user_id`作为用户的唯一标识。我们在数据库中检查这个`user_id`是否唯一，如果不唯一，我们会再次生成新的`user_id`。

---

## 16. create_room(room_num, room_type=None, room_price=None)

此函数用于创建新的房间。

### 参数：

- `room_num`：新房间的房间号，必须为三位数的整数。
- `room_type`：新房间的类型，为可选参数，如果不提供则为`None`。
- `room_price`：新房间的价格，为可选参数，如果不提供则为`None`。

### 返回值：

无返回值。

### 例子：

```python
create_room(101, "Single", 100)
```

在上述例子中，函数将在数据库中创建一个新的房间，其房间号为101，类型为"Single"，价格为100。

### 备注：

在此函数中，我们检查`room_num`是否为三位数的整数，如果不是，我们会抛出一个异常。
