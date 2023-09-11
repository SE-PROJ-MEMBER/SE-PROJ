# GUI

## 跨页面
### 翻页效果
* 用stackWidget堆叠窗口
* 错误信息和提示用弹窗形式

## 页面内
### 动态表格
* 表格用tableWidget类,
* 插入或删除列用insertColumn和insertRow方法
* 设置列标和行标: setHorizontalHeaderItem, setVerticalHeaderItem, 参数是行数/列数和标题内容
* 表格内容的选择用up/down按钮调节, select按钮选中

### 美化工作
* setStyleSheet方法, 单独写qss文件

### 自适应窗口
* 选择grid layout或table layout, 配合spacer固定按钮相对位置

### 窗口大小调整

