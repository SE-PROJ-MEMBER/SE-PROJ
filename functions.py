from connect import cursor as cur

def user_infor(user_id):
    cur.execute('SELECT * FROM user WHERE user_id = ?', (user_id,))
    user_list = cur.fetchall()
    return user_list