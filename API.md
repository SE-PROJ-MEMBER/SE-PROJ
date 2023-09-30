6.
### 创建订单接口



#### 请求参数：

| 参数名      | 类型   | 描述                 |
| ----------- | ------ | -------------------- |
| room_number | 整数   | 房间号               |
| user_id     | 整数   | 用户ID               |
| ck_in    | 字符串 | 入住时间 (YYYY-MM-DD)|
| ck_out   | 字符串 | 退房时间 (YYYY-MM-DD)|

#### 返回结果：

- **order_id** (整数) - 订单唯一标识符

---

**示例请求：**

```json
{
  "room_number": 101,
  "user_id": 123,
  "ck_in": "2023-10-01",
  "ck_out": "2023-10-05"
}



9-11
### `update_order(order_id, room_num, user_id, ck_in, ck_out, order_status, comment)`

**概述：** 更新订单信息。

**参数：**

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
update_order(1, 101, 1, "2023-10-01", "2023-10-10", 1, "Great room!")
```

---

### `comment_order(order_id, comment)`

**概述：** 添加订单评论。

**参数：**

- `order_id (int)`: 订单ID。
- `comment (string)`: 评论。

**返回值：**

- 如果订单状态为2（已退房），返回字符串 "Comment posted successfully."。
- 如果订单状态不为2，返回字符串 "Cannot comment on this order. Only orders with status 2 can be commented."。

**示例：**

```python
print(comment_order(1, "Great room!"))  # 输出: "Comment posted successfully."
```

---

### `get_all_users()`

**概述：** 获取所有用户信息。

**参数：** 无。

**返回值：** 返回一个包含所有用户信息的列表，每个用户的信息是一个包含`user`表中所有字段的元组。

**示例：**

```python
print(get_all_users())  # 输出: [(1, "John Doe", 1234567890, "john.doe@example.com", 1234567890123456, "password"), ...]
```

---
12～14

---

### `get_all_orders()`

**概述：** 获取所有订单信息。

**参数：** 无。

**返回值：** 返回一个包含所有订单信息的列表，每个订单的信息是一个包含`orderl`表中所有字段的元组。

**示例：**

```python
print(get_all_orders())  # 输出: [(1, 101, 1, "2023-10-01", "2023-10-10", 1, "Great room!"), ...]
```

---

### `update_room(room_num, room_type, room_price)`

**概述：** 更新房间信息。

**参数：**

- `room_num (int)`: 房间号。
- `room_type (int)`: 房间类型。
- `room_price (float)`: 房间价格。

**返回值：** 无。

**示例：**

```python
update_room(101, 2, 500.0)
```

---

### `get_room(room_num)`

**概述：** 获取特定房间的信息。

**参数：**

- `room_num (int)`: 房间号。

**返回值：** 返回一个包含特定房间信息的元组，包含`room`表中所有字段。

**示例：**

```python
print(get_room(101))  # 输出: (101, 2, 500.0)
```

---
