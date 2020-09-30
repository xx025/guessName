# 根据名字简拼猜解名字

**python3.7x**

**安装xpinyin：`pip install xpinyin`**

**双击main.py运行**
    
    如：你输入zs将会输出：张三...


---
就是一简单的一个小玩意，下面解释一下各个文件的用途：
```
    main.py     进行简单的输入
    ilfile.py   在你导入的名字的名字中寻找
    rlfile.py   根据你的输入，猜解姓氏简拼和名字简拼，并取汉字进行合并
    xingshihemingzi/xingshishuang.txt   8个复姓
    xingshihemingzi/xingshidan.txt      493个单姓
    xingshihemingzi/NAME.txt            你需要将自己的名单导入到这个文件
    xingshihemingzi/danzi.txt           1000左右个常用字
    NAMe.txt    如果你进行猜解的话，输出的名字比较多，将存到这个文件里

