##  PYQT开发指南
### 安装PyQt
+ 通过pip3安装pyqt5和pyqt5-tools, 命令: pip install PyQt5 和 pip install pyqt5-tools
+ 把python安装目录下\Lib\site-packages\pyqt5_tools这个文件夹加到系统环境变量里
  ![Alt text](srcimg/env_var.png)
+ 找到QT Designer, 在python安装目录下\Lib\site-packages\qt5_applications\Qt\bin\designer.exe

### 设置工具
+ 在pycharm中添加designer和PyUIC工具: 
1. 找到PyCharm -> 文件 -> 设置 -> 工具 -> 外部工具
   ![Alt text](srcimg/settings.png)
2. 点左上角+号添加工具
3. 首先添加QT Designer: 
   **名称**: 可以自定义;
   实参留空
   **程序**: 把designer.exe的绝对路径填进去;
   **工作目录**: 看自己喜好, 一般用宏\$FileDir\$
   ![Alt text](srcimg/designer_setting.png)
4. 然后添加PyUIC:
   名称自己填;
   **程序**: 是pyuic5.exe的目录, 一般是python安装路径下\Scripts\pyuic5.exe
   **实参**: `$FileName$ -o $FileNameWithoutExtension$.py`, 意思是由.ui文件在文件所在目录生成一个同文件名的.py文件
   **工作目录**: 同上\$FileDir\$
   ![Alt text](srcimg/uic_setting.png)
5. 完成

### 使用QT Designer开发的基本顺序
1. 使用designer应用程序把界面(包括按钮、窗口、输入框等等)设计好, 得到一个.ui文件
2. 使用PyUIC将.ui转换为.py文件以便调用, 编写各种控件运行的逻辑
3. 新建一个main.py(名字自定, 但是一定要新建一个, 不要在刚刚生成的.py里面直接写)
4. 在新建的main.py中, 一定要引入如下包:
   ```python
   import sys
   from PyQt5 import QtCore, QtGui, QtWidgets
   import xxx.py  # 这里的xxx就是刚刚生成的.py, 如果有多个要全部import进来
   ```
5. 在main.py中编写控制控件的代码
   