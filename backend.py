import sqlite3
import uuid
# 1. 返回用户信息
class user_id:

    def __init__(self, username, phone, email, credit_card_numbers, password):

        self.username = username
        self.phone = phone
        self.email = email
        self.credit_card_numbers = credit_card_numbers
        self.password = password

    def get_user_id(self):

        long_name = f"{self.username} {self.phone} {self.email} {self.credit_card_numbers} {self.password}"
        short_name = f"{self.username} {self.phone} {self.email}  {self.password}"
        return long_name

    # 2.判断是否登陆成功（返回失败原因）
    def login(short_name, password):
        if not short_name or not password:
            return "用户名、邮箱或电话号码以及密码不能为空"

        for user, user_data in user_id:
            if long_name == username or long_name == user_id.get(email) or long_name == user_id.get(phone):
                if password == user_id["password"]:
                    return f"登录成功，用户ID: {user_data['user_id']}"
                else:
                    return "密码错误"

        return "用户不存在"

# 3.注册成功返回user_id,失败返回原信息
    def register(phone, email, username, credit_card_numbers, password):
        if not phone or not email or not username or not credit_card_numbers or not password:
            return "注册失败，账号和密码都必须填写"

        for user_data in user_database.values():
            if phone == user_data.get("phone") or email == user_data.get("email") or username == user_data.get(
                    "username") or credit_card_numbers == user_data.get("credit_card_numbers"):
                return "注册失败，用户名、手机号、邮箱或银行卡号已存在"

        user_id = str(uuid.uuid4())  # 生成唯一的user_id
        user_database[username] = {"phone": phone, "email": email, "username": username, "credit_card_numbers": credit_card_numbers, "password": password, "user_id": user_id}
        return f"注册成功，用户ID: {user_id}"

# 从输入获取注册信息
    input_phone = input("请输入手机号码: ")
    input_email = input("请输入邮箱: ")
    input_username = input("请输入用户名: ")
    input_bank_card = input("请输入银行卡号: ")
    input_password = input("请输入密码: ")


conn = sqlite3.connect('info.db')

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
