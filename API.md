### 函数1. get_user_info(user_id)
**概述：** 获取用户信息。

**参数：**

- **user_id** (整数) - 用户唯一标识符
- **username** (字符串) - 用户名
- **phone_number** (字符串) - 电话号码
- **email** (字符串) - 邮箱
- **bank_card** (字符串) - 银行卡号

**示例：**
{
  "user_id": 123,
  "username": "JohnDoe",
  "phone_number": "123456789",
  "email": "john.doe@example.com",
  "bank_account": "987654321"
}






---



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
