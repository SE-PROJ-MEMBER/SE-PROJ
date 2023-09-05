# SE-PROJ
## members
+ Li YuanHao
+ Luo JiaSheng
+ Song Chengxi
+ Zhang peiqi
+ Qian Yumo
+ Su Jun

## 项目说明
+ 本项目为酒店管理系统，使用python开发
+ 本项目使用了内置sqlite数据库
+ 本项目预计使用pyqt库进行GUI开发
+ 本项目预计使用pyinstaller库进行打包，格式为exe
+ 实现功能：
    1. 用户注册及登录
    2. 用户预订以及入住房间
    3. 酒店方管理房间 


## sqlite数据库说明
+ 本数据库为sqlite数据库，数据库名为info.db
+ 数据库中有三张表，分别为user，room以及order
+ 注意数据库调用关键字cursor
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