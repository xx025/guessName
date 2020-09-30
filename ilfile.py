# filename:ilfile.py
from xpinyin import Pinyin


# 根据文件生成字典，将名字加入字典，拼音首字母为键
def nameSpy(fo):
    p = Pinyin()
    name_dict = dict()
    name_dict_2 = dict()
    '''建两个字典，
        第一个保存例如:zsw:张三五,张三无；zs:张三，张伞
        第二个保存：sw:张三无，司三五    也就是两个字以上的名字的字的后两个字的简拼    
    '''
    for line in fo:
        # print(line.strip(),end="")
        s = p.get_initials(line.strip(), u'').lower()
        # print(s)
        if s.__len__() > 2:
            s_2 = s[-2:]
            name_dict_2.setdefault(s_2,[]).append(line.strip())
        # 获取名字的简拼，"王五六"->"wwl"
        name_dict.setdefault(s, []).append(line.strip())
        # 更新字典,这里字典的值为列表
    return name_dict, name_dict_2


def mian(str):
    # 设置一个保存名字和名字拼音首字母的字典，例：d={"ww":"王五"}
    fo = open("xingshihemingzi/NAME.txt", "r", encoding='UTF-8')
    # 获取名单对应的字典
    name_dict, name_dict2 = nameSpy(fo)
    # print(name_dict)#输出这个字典
    fo.close()
    name_list = []
    if str in name_dict:
        name_list = name_dict[str]
    if str in name_dict2:
        name_list+=name_dict2[str]
    else:
        pass
    return name_list