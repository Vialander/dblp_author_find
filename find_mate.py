import xml.etree.cElementTree as ET

main_list = []
main_dict = {}

def ReadXml(filename,type):
    tree = ET.parse(filename)
    root = tree.getroot()
    string = ""
    for object in root.findall(type):
        for author in object.findall('author'):
            string += str(author.text)
            string += "#"
        string += "\n"
    return string

def WriteTxt(filename,contents):
    fh = open(filename,'w',encoding='utf-8')
    fh.write(contents)
    fh.close()

def ReadTxt(filename):
    fr = open(filename)
    for line in fr.readlines():
        main_list.append(list(line.strip('\n').split(',')))
    return main_list

def Trans_List(in_list):
    out_list=[]
    test = str(in_list[0])
    str_get=''
    for t in test:
        if t != '[' and t != ']' and t != '\'':
            if t != '#':
                str_get += t
            else:
                out_list.append(str_get)
                str_get = ''
    return out_list

def Find(test_list,author_name):
    tmp_list = []
    for tl in test_list:
        tmp_list = Trans_List(tl)
        if author_name in tmp_list:
            for tml in tmp_list:
                if (tml not in main_dict.keys()):  # 如果所找到的作者名不在主需求页面中
                    main_dict[tml] = 1  # 初始化该项作者
                else:  # 如果找到的话
                    main_dict[tml] = main_dict.get(tml,0) + 1  # 数字加一
    return main_dict

def PrintResult(the_dict):
    temp_dic = the_dict
    for k in sorted(temp_dic,key=temp_dic.__getitem__,reverse=True):
        print("Name:",k,"   Times:",temp_dic[k])

name_get = input("Input the name from whom you want to know:")
TB = ['article','inproceedings','proceedings','book','incollection','phdthesis','mastersthesis','www']
str_get = ReadXml('first.xml',TB[0])+ReadXml('first.xml',TB[1])+ReadXml('first.xml',TB[2])+ReadXml('first.xml',TB[3])+ReadXml('first.xml',TB[4])+ReadXml('first.xml',TB[5])+ReadXml('first.xml',TB[6])+ReadXml('first.xml',TB[7])
WriteTxt('test.txt',str_get)
PrintResult(Find(ReadTxt('test.txt'),name_get))
