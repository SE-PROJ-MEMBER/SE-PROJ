import backend

# 9. 创建一个订单
order_id = 1
room_num = 102
user_id = 2
ck_in = '2023-10-01'
ck_out = '2023-10-05'
order_status = 2
comment = 'This is a comment'
backend.update_order(order_id, room_num, user_id, ck_in, ck_out, order_status, comment)

# 10. 尝试为订单添加评论
new_comment = 'This is a new comment'
comment_result = backend.comment_order(order_id, new_comment)
print(comment_result)

# 11. 获取所有用户信息
users = backend.get_all_users()
for user in users:
    print(user)
