import sqlite3
conn = sqlite3.connect('info.db')

cursor = conn.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS room(room_num INT PRIMARY KEY,ck_in DATE,ck_out DATE,room_type TEXT,room_price INT,room_status INT)')

cursor.execute(
    'CREATE TABLE IF NOT EXISTS user(user_id INT PRIMARY KEY,user_name TEXT,user_phone INT,user_email TEXT,user_card INT) ')
