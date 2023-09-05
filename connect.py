import sqlite3
conn = sqlite3.connect('info.db')

cursor = conn.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS room(room_num INT PRIMARY KEY,room_type TEXT,room_price INT)')

cursor.execute(
    'CREATE TABLE IF NOT EXISTS user(user_id INT PRIMARY KEY,user_name TEXT,user_phone INT,user_email TEXT,user_card INT,user_pwd TEXT)')

cursor.execute(
    'CREATE TABLE IF NOT EXISTS orderl(order_id INT PRIMARY KEY,room_num INT,user_id INT,ck_in DATE,ck_out DATE,order_status INT)')
