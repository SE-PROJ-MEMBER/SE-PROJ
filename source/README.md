# SE-PROJ
## members
+ Li YuanHao
+ Luo JiaSheng
+ Song Chengxi
+ Zhang peiqi
+ Qian Yumo
+ Su Jun
+ Lai FeiYu
+ Liu Kuan
+ Luo ShiHuan
+ Zhu BoYa
## 分工
|   所属    |  姓名  |   任务    |  DDL  |  完成情况  | 备注  |
|---------- |:-------------:|------:|------:|------:|------:|
|  GUI  |李远昊   |   |  |   |developer   |
| GUI   |罗家晟   |   |  |   |leader|
| GUI   |张沛祺   |   |  |   |developer   |
| back-end/civil   |钱禹默   |   |  |   |civil&test   |
| civil   |罗仕桓   |   |  |   | civil  |
| GUI   |苏俊     |   |  |   |developer   |
|back-end    |赖飞羽   |   |  |   |developer   |
| back-end   |刘宽     |   |  |   |developer   |
| GUI/civil   |宋承熹   |   |  |   |civil&test   |
| civil   |朱博涯   |   |  |   |civil  |


### 测试情况---10.4
|   功能    |  开发人员  |   通过自测    | 通过测试（测试员填写）  | 备注  |文档|
|---------- |:-------------:|------:|------:|------:|------:|
| 后端1   | 赖飞羽  |  否 |  |超时   |无|
| 后端2   | 赖飞羽  | 否  |  |超时   |无|
| 后端3   | 赖飞羽  | 否  |  |超时   |无|
| 后端4   | 赖飞羽  | 否  |  |超时   |无|
| 后端5   | 赖飞羽  | 否  |  |超时   |无|
| 后端6   | 赖飞羽  | 否  |  |超时   |...|
| 后端7   | 赖飞羽  | 否  |  |   |...|
| 后端8   | 赖飞羽  | 否  |  |   |...|
| 后端9   | 刘宽    | 否  |  | 超时  |无|
| 后端10  | 刘宽    | ?  |  | 超时  |有|
| 后端11  | 刘宽    | ?  |  |超时   |有|
| 后端12  | 刘宽    | ?  |  |   |有|
| 后端13  | 刘宽    | 否  |  |超时   |...|
| 后端14  | 刘宽    | ?  |  |   |有|
| 后端15  | 刘宽    | ?  |  |   |有|
| 后端16  | 刘宽    | ?  |  |   |有|
| 后端17  | 钱禹默  |   |  |   ||
| 后端18  | 钱禹默  |   |  |   ||
| 后端19  | 钱禹默  |   |  |   ||
| 后端20  | 钱禹默  |   |  |   ||

### 时间表
10.8  第一次更新\
10.22 白皮书\
10.29 第二次更新\
11.12 第三次更新\
11.26 技术报告\
12.3  第四次更新 （软件开发完成）\
12.10 presentation + group workload profile

开发进度对应：\
10.8  后端完成,前端页面设计完成\
10.22\
11.12前端完成\
12.3 软件打包完成

### 白皮书要求
1. summary business case
2. functional requirements
3. non-functional requirements
4. use case diagram & use case description
5. context model
6. business process model
7. 15-30页

### 技术报告要求（不要放代码）
1. class diagram
2. sequence diagram
3. test cases
   + unit test
   + interface test
4. GUI design
   + do not show codes
5. 最少20页，最多45页


## 项目说明
+ 本项目为酒店管理系统，使用python开发
+ 本项目使用了内置sqlite数据库
+ 本项目预计使用pyqt库进行GUI开发
+ 本项目预计使用pyinstaller库进行打包，格式为exe
+ 实现功能：
    1. 用户注册及登录
    2. 用户预订以及入住房间
    3. 酒店方管理房间 

### presentation要求(13 min, 其中10 min presentation, 3 min Q&A)
1. introduce your team(1 min)
2. summarize your project(2 min)
3. summarize of SDLC(2 min)
4. demo(4 min)
   + screenshot
   + short videos
   + actual software
5. challenges solution(1 min)
6. future work(1 min)

### update要求
1. 1page
2. 400-600 words
3. summary of progress
4. any diffculties/challenges
5. next step
6. 1 1% of total grade\
    2 1% of total grade\
    3 1% of total grade\
    4 2% of total grade\
    total 5%

## sqlite数据库说明
+ 本数据库为sqlite数据库，数据库名为info.db
+ 数据库中有三张表，分别为user，room以及orderl
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
### orderl表
+ orderl表中有七个字段，分别为
    + order_id INT PRIMARY KEY
    + room_num INT
    + user_id INT
    + ck_in DATE
    + ck_out DATE
    + order_status INT
    + comment TEXT
+ order_id为主键，使用随机生成的数字
+ order_status 0代表已预订，1代表已入住，2代表已退房，3代表已取消，4代表未支付

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

### 后端功能清单
1. 通过user_id返回用户的信息，包括user表中所有字段
2. 通过电话号码和密码，邮箱和密码，或者用户名和密码判断是否登录成功，登录成功返回登录成功信息以及当前用户的user_id，失败返回登录失败原因（用户不存在，密码错误）
3. 通过电话号码，邮箱，用户名，银行卡号和密码注册，注册成功返回注册成功信息并生成唯一的user_id并返回，失败返回注册失败信息，失败原因包括用户名已存在，手机号已存在，邮箱已存在；无需返回失败原因
4. 通过user_id修改用户信息，修改信息可能覆盖user表中所有字段，user_id不可修改,如果修改之后的所有个人信息与其他用户重复，则返回修改失败信息
5. 通过时间段和房型查找可预定房间，返回所有可预定房间信息，包括room表中所有字段所有相应行
6. 通过房间号，用户id，入住时间，退房时间创建订单，为订单以及唯一的order_id，订单状态为默认为0，返回order_id
7. 通过房间号返回价格
8. 通过order_id返回订单信息，包括order表中所有字段
9. 通过order_id修改订单信息，修改信息可能覆盖order表中所有字段，order_id不可修改
10. 通过order_id进行评论，仅状态为2的订单可以评论，否则返回评论失败信息
11. 返回所有用户信息，包括user表中所有字段所有行
12. 返回所有订单信息，包括orderl表中所有字段所有行
13. 通过房间号修改房间信息，修改信息可能覆盖room表中所有字段，room_num不可修改
14. 通过房间号返回房间信息，包括room表中所有字段
15. 仅通过用户名和密码新建用户，注意与3是不同接口
16. 新建房间，注意房间号不能为空
17. 新建订单（注意与5是不同接口，无需额外信息，只要求任何一个字段不为空）
18. 通过房间号删除房间（删除相应行）
19. 通过user_id删除用户（删除相应行）
20. 通过user_id查找订单，返回所有订单信息，包括order表中所有字段所有相应行
21. 返回所有房间信息，包括room表中所有字段所有行

+ 注意order_id，user_id，room_num为主键，不可重复,不可修改
+ order_id,user_id为生成的随机数字，room_num为管理员输入的三位数字
+ 开发人员为已经开发的接口提供详细说明
+ 开发人员可以自行添加接口，但必须在此说明
+ 后期可能有需求变动




## 具体功能说明（前端/页面）
1. 用户登录界面(sign_in_page1)
    + 实现登录功能，注意与后端数据交互
    + 注册按钮（跳转到房间预定界面）
    + 登录成功或失败跳到相应信息界面（2/3）
2. 登录成功界面(sign_in_su_page2)
    + 显示登陆成功
    + 可以选择跳转到房间预定界面或个人主页
    + 修改登陆状态
    + 如果为管理员账户则跳转到管理员界面
    + 显示欢迎信息
3. 登录失败界面(sign_in_fa_page3)
    + 显示登录失败
    + 显示失败原因（如密码不正确）
    + 返回按钮（跳转到登录界面1）
4. 用户注册界面(sign_up_page4)
    + 实现注册功能，注意与后端数据交互
    + 注册成功或失败跳到相应信息界面(2,5)
    + 取消按钮（跳转到登录界面1）
    + 修改登陆状态
    + 注意在此界面不能注册管理员（用户名开头admin）
5. 注册失败界面(sign_up_fa_page5)
    + 显示注册失败
    + 显示失败原因
    + 返回按钮（跳转到注册界面1）
6. 房间预定界面(book_info_page6)
    + 时间选择功能
    + 房间类型选择功能
    + 查询按钮
    + 实现查询功能，注意与后端数据交互(将数据显示到下个页面7)
    + 登出按钮（跳转到1）
7. 房间预定界面(select_page7)
    + 房间信息显示到选择框下方
    + 高亮用户点击的行
    + 点击预定按钮跳转到订单信息界面
8.  订单确认界面(confirm_order_page8)
    + 显示订单信息
    + 确认按钮
    + 实现预定功能，注意与后端数据交互(生成订单)
    + 取消按钮（跳转到7）
    + 预定后跳转到支付细节页面9
9.  支付细节页面(payment_detail_page9)
    + 显示总金额
    + 显示订单信息
    + 显示user邮箱
    + 用卡支付按钮（跳转到支付成功界面10）
    + 检查订单按钮（跳转到个人主页11）（订单状态为未支付）
10. 支付成功界面(payment_approved_page10)
    + 检查订单按钮（跳转到个人主页11）
    + 继续订房按钮（跳转到6）
11. 个人主页(personal homepage11)
    + 显示个人信息
    + 显示订单信息
    + 修改按钮（根据用户点击修改个人信息12）
    + 修改个人信息按钮（跳转到订单信息14）
    + 预定房间按钮（跳转到6）
12. 修改个人信息界面(modify_personal_page12)
    + 用户通过复选框选择修改条目
    + 实现修改功能，注意与后端数据交互
    + 取消按钮（跳转到11）
    + 确认按钮（跳转到修改成功13/失败21）（与其他用户完全相同）
    + 登出按钮（跳转到1）
13. 操作成功界面(op_su_page13)
    + 显示操作成功
    + 返回按钮（跳转到前一个页面）
14. 修改订单信息界面(modify_order_page14)
    + 返回按钮（跳转到个人主页11）
    + 取消订单按钮（跳转到13）
    + 实现评论功能
    + 评论按钮（成功跳转到13，失败跳转到15）
15. 评论失败界面(comment_fa_page15)
    + 返回按钮（跳转到14）
16. 管理员界面(admin_page16)
    + 显示所有用户信息
    + 显示所有订单信息
    + 房间按钮（跳转到房间管理界面22）
    + 选项按钮（根据用户点击modify按钮修改订单信息17，点击manager按钮跳转user信息20）
    + 登出按钮（跳转到登录界面1）
17. 修改订单信息界面(manage_order_page17)
    + 管理员通过复选框选择订单状态
    + 确认按钮（跳转到13）
    + 评论按钮（跳转到评论管理界面18）
    + 添加按钮（跳转到添加界面19）
    + 返回按钮（跳转到16）
    + 登出按钮（跳转到1）
18. 评论管理界面(comment_page18)
    + 显示当前订单评论信息
    + 删除评论按钮（跳转到13）
    + 实现删评功能，注意与后端数据交互
    + 返回按钮（跳转到17）
19. 添加订单界面(add_order_page19)
    + 与4类似，但是要求任意一字段不为空
    + 返回按钮（跳转到17）
    + 添加按钮（跳转到13）
20. 用户管理界面(manage_user_page20)
    + 删除当前用户按钮（跳转到13）
    + 实现用户删除功能，注意与后端数据交互
    + 添加用户按钮（跳转到23）
    + 返回按钮（跳转到16）
    + 登出按钮（跳转到1）
21. 操作失败界面(op_fa_page21)
    + 返回按钮（跳转到前一个页面）
    + 显示操作失败原因
22. 房间管理界面(manage_room_page22)
    + 显示所有房间信息
    + 添加房间按钮（跳转到24）
    + 返回按钮（跳转到16）
    + 修改房间按钮（跳转到23）
    + 登出按钮（跳转到1）
    + 删除房间按钮
    + 实现删除房间功能，注意与后端数据交互
23. 房间信息修改按钮（modify_room_page23）
    + 与12类似
    + 用户通过复选框选择修改条目
    + 实现修改功能，注意与后端数据交互
    + 取消按钮（跳转到22）
    + 确认按钮（跳转到修改成功13/失败21）
24. 添加房间界面(add_room_page24)
    + 要求任意一字段不为空
    + 实现添加房间功能，注意与后端数据交互
    + 返回按钮（跳转到22）
    + 添加按钮（跳转到13/失败21）（不能添加已有的房间号）
25. 添加用户界面(add_user_page25)
    + 与4类似，但是要求任意一字段不为空
    + 返回按钮（跳转到20）
    + 添加按钮（跳转到13/失败21）（不能添加已有的用户）（可以添加管理员）

+ 登录状态：0代表未登录，1代表已登录，2代表管理员登录

### 前端函数说明
+ 所有函数写到main.py中
+ 对ui文件进行任何更改都应该重新生成相应的py文件，并修改版本号以及main里的调用；如果改动按钮名称，应告知相应人员；不得轻易改动页面序号
+ 函数绑定到相应按钮，绑定相应按钮的代码放到if __name__ == '__main__':下面
+ 如果存在显示信息的函数，应先显示相应信息再跳转页面
+ 关于全局变量的说明
  + g_current_user_id为当前用户的user_id，初始值为0
  + g_sign_in_status为当前登录状态，初始值为False   
  + g_admin_status为当前管理员登录状态，初始值为False
  + g_pre_page为上一个页面的index，初始值为0
  + g_pre_row无需理解
  + g_current_order_id为现在订单的order_id，初始值为0
  + g_search_result为搜索可选房间的结果，初始为空列表
  + g_user_selection为用户选择房间的结果，初始为空列表
  + g_user_selection_date为用户选择的时间
  + g_table_name为当前操作组件名
+ 关于public函数的说明
  + public函数为公共函数，用于实现一些功能，如显示信息，修改信息等，可以重用
  + turn_page()函数用于跳转页面，参数为页面index, 无返回值
  + to_pre_page()函数用于跳转到上一个页面，无参数，无返回值
  + set_color,highlight_row,,addColumn,addRow为中间函数，无需理解
  + table_show()为展示表格内容的函数，不接受参数，调用先修改g_table_name为当前组件名称，无返回值
  + addMultiColumn,addMultiRow,setCellText适用于QTableWidget，用于显示信息并且高亮显示鼠标所点击的行
  + addMultiColumn用于在QTableWidget中添加列，参数为列名列表，QTableWidget对象，无返回值
  + addMultiRow用于在QTableWidget中添加行，参数为行列表，QTableWidget对象，无返回值
    + 注意行列表中可以包含数字，用于显示行的index
    + 行列表中的内容不会占用QTableWidget的列
  + setCellText用于在QTableWidget中显示信息，参数为行序号，列序号，显示内容和QTableWidget对象，无返回值
    + 行序号和列序号用于确定显示位置
    + 此函数一次只能设置一个单元格的内容，如果需要设置多个单元格的内容，需要多次调用此函数
  + clear_table()用于清空QTableWidget中的内容，当一个QTableWidget需要多次显示，则跳出页面之前应调用此函数，无参数，无返回值
  + delay_jump函数可能导致页面不在一个线程，已弃用
+ log_out用于登出，可重置登陆状态，管理员登陆状态，当前用户id，当前订单id并跳转到登录页面无参数，无返回值
+ 如果需要实现跳转到之前页面的功能，需要利用全局变量g_pre_page



