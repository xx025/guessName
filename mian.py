import ilfile

import rlfile
import time

print(
    '''如果你要在本地检索，请确保xingshihemingzi/NAME.txt文件中有你导入的名字
    你的输入将会被限制在2-4个英文字母（含复姓）
    程序运行结束，名字输出在本目录下NAMe.txt文件中
    ''')


def mian():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    str = input("请输入名字简拼:")
    if 2 <= str.__len__() <= 4:
        str2 = input("在本地查找请键入a;猜解请键入b:")
        if str2 == "a":
            # 用于导入本地名字文件
            name = ilfile.mian(str)
        elif str2 == "b":
            name = rlfile.mian(str)
        else:
            print("键入有误")
        if name.__len__() != 0:
            # 对过多的名字输出到文件
            if name.__len__() > 40:
                print('''\033[0;34m名字较多输出到NAMe.txt文件,请查看\033[0m''')
                fo = open("NAMe.txt", "w", encoding='UTF-8')
                for i in range(name.__len__()):
                    if i % 7 == 0:
                        fo.write("\n")
                    fo.write(name[i] + "\t")
                fo.close()
                print("")
            # 对较少的名字输出到控制台
            else:
                print('''\033[0;34m找到以下名字''')
                for i in range(1, name.__len__() + 1):
                    print("{:>5}".format(name[i - 1]), end="\t")
                    if i % 7 == 0:
                        print()
                print('''\033[0m''')
        else:
            print('''[没有找到]
        1.在您导入的名单中没找到
        2.您没有向（xingshihemingzi/NAME.txt）中导入名单
        3.您输入的姓氏简拼太过稀有未包含''')
    else:
        print('''\033[0;31m您的输入是：''' + str + '''\n\t可能有误，请检查重新输入\033[0m''')
    mian()


if __name__ == "__main__":
    mian()
