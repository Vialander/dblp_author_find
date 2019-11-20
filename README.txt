这是用来对dblp特定作者，展示其相关合作伙伴及合作程度的代码
排名第一的是作者本身

first.xml是精简后的dblp.xml，以便更快读取
dblp不能直接使用cElementTree读取，因为有的作者姓名中带有'&',';','-'等乱码
在使用first.xml前需要使用clean_data代码对所有姓名信息进行清洗
需要清洗的数据放在clean.txt里，清洗所得的数据在clean_out.txt里
取出清洗所得数据，放在first.xml中，即可正常运行代码。

附件里的first.xml是测试用的，正常输入作者姓名为A会得到返回值
例如：
Input the name from whom you want to know:A
Name: A    Times: 5
Name: B    Times: 3
Name: C    Times: 1

可随意对first.xml修改

喜欢的话请点个星星
如果发现有可优化的地方，还请指出（我知道我的代码还有很多欠缺的地方，一起努力！）