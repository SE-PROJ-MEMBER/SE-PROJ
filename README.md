# SE-PROJ
## members
+ Li YuanHao
+ Luo JiaSheng
+ Song Chengxi
+ Zhang peiqi
+ Qian Yumo
+ Su Jun

## sqlite数据库说明
+ 本数据库为sqlite数据库，数据库名为info.db
+ 数据库中有三张表，分别为user，room以及order
### user表
+ user表中有六个字段，分别为    
    + user_id INT PRIMARY KEY
    + user_name TEXT
    + user_phone INT
    + user_email TEXT
    + user_card INT
    + user_pwd TEXT
+ user_id为主键，使用随机生成的数字
+ user_card为用于支付或担保的银行卡号
### room表
+ room表中有三个字段，分别为
    + room_num INT PRIMARY KEY
    + room_type TEXT
    + room_price INT
+ room_num为主键，使用三位数字，代表楼层和编号
+ room_price为按天计算的价格
### order表
+ order表中有六个字段，分别为
    + order_id INT PRIMARY KEY
    + room_num INT
    + user_id INT
    + ck_in DATE
    + ck_out DATE
    + order_status INT
+ order_id为主键，使用随机生成的数字
+ order_status 0代表已预订，1代表已入住