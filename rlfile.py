# filename:rlfile.py
from xpinyin import Pinyin

import ilfile


# 把名字简拼拆分了
def splitname(str, surname_dict):
    xs = list()
    mz = list()
    if str. __len__() == 2:
        # 长度为2必然为单姓
        xs.append(str[0:1])  # 姓氏
        mz.append(str[1:2])  # 名字
    elif str.__len__() == 3:
        # 长度为3有两种情况1.单姓名字两个字2.复姓名字一个字
        # 如smx可为：“司马x"或“沈mx”
        # 单姓
        xs.append(str[0:1])  # 姓氏
        mz.append(str[1:3])  # 名字
        if(str[0:2] in surname_dict):
            # 复姓
            xs.append(str[0:2])
            mz.append(str[2:3])
    elif str.__len__() == 4:
        # 长度为4复姓
        xs.append(str[0:2])
        mz.append(str[2:4])

    # print(xinggshi)
    # print(minggzi)

    return {"xingshi": xs, "mingzi": mz}


def mergername(xing, ming, surname, singleWord):
    # 猜解可能的姓氏
    xings = surname.get(xing)
    # print(xings)#打印可能的姓氏
    name = list()
    if xings:
        # 姓氏列表不能为空
        # 猜解可能的名字
        mingz = []
        if ming.__len__() == 1:
            # 名为一个个字的情况
            mingz = singleWord.get(ming)
        else:
            # 名为两个字的情况
            lis = list(ming)
            mingz1 = singleWord.get(lis[0])
            mingz2 = singleWord.get(lis[1])
            for i in mingz1:
                if i != xings:
                    # 让名中的字和姓不重复例如：“王王”
                    for j in mingz2:
                        if i != j:
                            # 去掉两字重复的情况
                            mingz.extend([i+j])
        for i in xings:
            for j in mingz:
                name.extend([i+j])
    else:
        # 让name列表为空
        name = list()
    return name


def exportname(xingjplist, mingjplist, surname, singleWord):
    name = list()
    # xingjplist.__len__==1作为默认
    name.extend(mergername(xingjplist[0], mingjplist[0], surname, singleWord))
    print(xingjplist)
    print(xingjplist.__len__())
    if xingjplist.__len__() == 2:
        name.extend(mergername(xingjplist[1],
                               mingjplist[1], surname, singleWord))
    return name


def mian(str):
    # 单个字
    fo1 = open("xingshihemingzi/danzi.txt", "r", encoding='UTF-8')
    # 单姓
    fo2 = open("xingshihemingzi/xingshidan.txt", "r", encoding='UTF-8')
    # 复姓
    fo3 = open("xingshihemingzi/xingshishuang.txt", "r", encoding='UTF-8')

    # 单个汉字
    singleWord = ilfile.nameSpy(fo1)
    # print(singleWord)
    # 姓氏  单姓:namespy.fo2 ;复姓:namespy.fo3
    surname = {**ilfile.nameSpy(fo2), **ilfile.nameSpy(fo3)}
    # print(surname)

    xingming = splitname(str, surname)  # 拆分简拼获取姓的简拼和名的简拼
    xinglist = xingming.get("xingshi")  # 姓氏拼音首字母
    minglist = xingming.get("mingzi")  # 名字拼音首字母
    return exportname(xinglist, minglist, surname, singleWord)
