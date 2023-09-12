# GUI实现细节

## 跨页面
### 翻页效果
* 用stackWidget堆叠窗口

## 页面内
### 窗口布局调整
* 使用grid layout, 相当于往界面上摆隐形格子, 
* margin是控件与边框之间的边距, 单位为像素
* 属性layoutRowStrech和layoutColumnStrech是拉伸因子, 意思是窗口大小发生改变的时候, 各个控件大小发生改变的比例
  这两个值的类型像是数组, 在designer输入的时候不能习惯性的带空格, e.g. "1,1,2"相当于1:1:2缩放
* layoutRowMinimum和layoutColumnMinimum是每行/列的格子高/宽的最小值, 控件按照上面的比例缩放到最小值就会停止缩放
  单位是像素, 如果不知道大小可以先让所有控件均匀排列, 然后去控件属性里的geometry查看当前大小, 根据那个调整
* spacing的那几个是格子之间的空隙大小, 单位像素

### 自适应窗口
* 使用spacer垫片, 分水平和竖直两种, 在grid layout里面spacer单独占一个格子, 放完要调整

### 动态表格
* 表格用tableWidget类,
* 插入或删除列用insertColumn和insertRow方法
* 设置列标和行标: setHorizontalHeaderItem, setVerticalHeaderItem, 参数是行数/列数和标题内容
* 直接点表格选中
* 记得给表格加上不可编辑属性: `UI.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)`

### 美化工作
* setStyleSheet方法, 单独写qss文件
