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

## 具体功能说明（后端）
### 用户注册及登录
1. 用户注册
    + 用户注册时需要输入用户名，手机号，邮箱，银行卡号以及密码
    + 用户名，手机号，银行卡号以及密码均不能为空
    + 注册成功或失败须返回相应信息
    + 注册成功后，用户信息存入数据库user表
    + 每个用户有一个唯一的user_id，用于识别和区分不同用户
2. 用户登录
    + 用户登录时需要输入用户名和密码，或者手机号和密码，或者邮箱和密码
    + 用户登陆成功或失败，返回相应信息
    + 登录成功后，可以查看自己的个人信息
    + 登录成功后，可以修改用户名，手机号，邮箱，银行卡号以及密码
    + 登录成功后，可以查看并修改自己的订单信息
3. 管理账户
    + 设置一个管理员账户，用于管理房间
    + 管理员账户可以查看所有用户的信息
    + 管理员账户可以查看和修改所有房间的信息
    + 管理员账户可以查看和修改所有订单状态
    
### 用户预订以及入住房间
1. 用户预定
    + 用户预定时需要输入入住时间，退房时间，房间类型
    + 用户输入信息后，系统返回可预定的房间信息
    + 用户预定成功或失败，返回相应信息
    + 预定成功后，订单信息存入数据库order表
    + 每个订单有一个唯一的order_id，用于识别和区分不同订单
2. 用户入住
    + 入住成功后，订单状态改为已入住
3. 用户退房
    + 退房成功后，订单状态改为已退房
    + 退房成功后，房间状态改为空闲
    + 退房成功后，用户可以评价房间,评价信息录入order表
    
