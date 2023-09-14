# 问题汇总
## Q&A

* 在PyQt5的main.py中使用time.sleep(sec)会造成应用程序卡死
  原因: GUI的实质是一个处理事件的主线程, time.sleep运行时, GUI处于等待状态, 在windows系统下, 系统认为程序出错, 此时进行其他操作, 程序便会卡死
  解决办法: 使用QThread或Threading新开一个线程执行耗时操作