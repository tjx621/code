#! 通用的序列操作
# ? 索引
# greeting = 'hello'
# print(greeting[0])
# print(greeting[-1])
# print('hello'[1])

# fourth = input('year: ')[3]
# print(fourth)

# 打印日期
# months = [
#     'January',
#     'February',
#     'March',
#     'April',
#     'May',
#     'June',
#     'July',
#     'August',
#     'September',
#     'October',
#     'November',
#     'December'
# ]
#
# endings = ['st', 'nd', 'rd'] + 17*['th']\
#         + ['st','nd','rd'] + 7*['th']\
#         + ['st']
#
# year = input('Year: ')
# month = input('Month: ')
# day = input('Day: ')
#
# year_number = int(year)
# month_number = int(month)
# day_number = int(day)
#
# month_name = months[month_number-1]
# ordinal = day + endings[day_number-1]
#
# print(month_name + ' ' + ordinal + ',' + year_number)

# ? 切片
# tag = '<a href="http://www.python.org">Python web site</a>'
# print(tag[9:30])
# print(tag[32:-4])
#
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers[3:6]) #不包含第二个索引
# print(numbers[0:1])
# print(numbers[-3:-1])
# print(numbers[-3:]) # 终止于末尾
# print(numbers[:3]) # 从头开始
# print(numbers[:]) # 复制
# print(numbers[0:10:1]) # 默认步长
# print(numbers[0:10:2]) # 步长2
# print(numbers[::4])
# print(numbers[8:3:-1])  # 负步长 从右向左
# print(numbers[10:0:1])
# print(numbers[0:10:1])
# print(numbers[::-2])
# print(numbers[5::-2])
# print(numbers[:5:-2])

# ? 序列相加
# print([1,2,3]+[4,5,6])
# print('hello,'+'world!')
# # print([1,2,3]+'world!')  #不能拼接不同类型的序列

# ? 乘法
# print('python '*5)
# print([42]*10)

# 空列表None
# sequence = [None] * 10
# print(sequence)

# ? 成员资格in
# permissions = 'rw'
# print('w' in permissions)
# print('x' in permissions)
#
# users = ['mlh', 'foo', 'bar']
# print(input('Enter your user name: ') in users)
#
# subject = '$$$ Get rich now!!! $$$'
# print('$$$' in subject)

# len max min
# numbers = [100,34,11]
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
#
# print(max(2,3))
# print(min(1,3,4,2))


# ! 列表
#
# ? 创建列表
# print(list('hello'))
# ? 修改列表
# # 给元素赋值
# x = [1,1,1]
# x[1] = 2
# print(x)
# # 删除元素
# names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
# del names[2]
# print(names)
# # 给切片赋值
# name = list('Perl')
# print(name)
# name[2:] = list('ar') # 替换相同长度
# print(name)
#
# name = list('Perl')
# name[1:] = list('ython') # 替换不同长度
# print(name)
#
# numbers = [1,5]
# numbers[1:1] = [2,3,4] # 插入序列
# print(numbers)
#
# numbers[1:4] = [] # del numbers[1:4]
# print(numbers)

# ? 列表方法
#
# # append 在列表末尾添加
# lst = [1, 2, 3]
# lst.append(4)
# print(lst)
#
# # clear 清空列表内容
# lst = [1, 2, 3]
# lst.clear()  # lst[:]=[]
# print(lst)
#
# # copy 复制列表
# a = [1, 2, 3]
# b = a  # 常规复制：将另一个名称关联到列表
# b[1] = 4
# print(a) # [1,4,3]
#
# a = [1, 2, 3]
# b = a.copy()  # 将b关联到a的副本  # b=a[:]  b=list(a)
# b[1] = 4
# print(a) # [1,2,3]
#
# # count计算指定的元素在列表中出现了几次
# print(['to', 'be', 'or', 'not', 'to', 'be'].count('to'))
# x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
# print(x.count(1))
# print(x.count([1, 2]))
#
# # extend 用一个列表拓展另一个列表
# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)  # 修改被拓展的序列
#
# a = [1, 2, 3]
# b = [4, 5, 6]
# a[len(a):] = b  # extend
# print(a)
#
# # index 查找指定值第一次出现时的索引
# knights = ['we', 'are', 'the', 'knights', 'who', 'say', 'ni']
# print(knights.index('who'))
# print(knights[4])
# # print(knights.index('tjx'))
#
# # insert 将一个对象插入列表
# numbers = [1, 2, 3, 4, 5, 6, 7]
# numbers.insert(3, 'four')  # numbers[3:3]=['four']
# print(numbers)
#
# # pop 从列表中删除一个元素，并返回这一元素
# x = [1, 2, 3]
# print(x.pop()) # 默认删除最后一个元素
# print(x)
# print(x.pop(0)) # 指定删除元素
# print(x)
#
# # remove 删除第一个为指定值的元素
# x = ['to', 'be', 'or', 'not', 'to', 'be']
# x.remove('be')
# print(x)
#
# # reverse 反序
# x = [1, 2, 3]
# x.reverse()
# print(x)
#
# # sort 排序
# x = [4, 6, 2, 1, 7, 9]
# x.sort()
# print(x)
#
# x = [4, 6, 2, 1, 7, 9]
# y = x.sort()
# print(y)  # None sort直接修改列表，不返回任何值
#
# x = [4, 6, 2, 1, 7, 9]
# y = x.copy()
# y.sort()
# print(x)
# print(y)
#
# x = [4, 6, 2, 1, 7, 9]
# y = sorted(x)  # 获取排序后列表的副本
# print(x)
# print(y)
#
# print(sorted('python'))  # sorted可用于任何序列，但总是返回一个列表
#
# x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
# x.sort(key=len)
# print(x)
#
# x = [4, 6, 2, 1, 7, 9]
# x.sort(reverse=True)
# print(x)


# ! 元组：不可修改的序列
# print((1, 2, 3))
# print(())
# print((42))
# print(3*(40+2,))
#
# print(tuple([1,2,3]))
# print(tuple('abc'))
# print(tuple((1,2,3)))
#
# x = 1,2,3
# print(x)
# print(x[1])
# print(x[0:2])


# ! 字符串

# # 替换字段名
# print('{foo} {} {bar} {}'.format(1, 2, bar=4, foo=3))
# print('{foo} {1} {bar} {0}'.format(1, 2, bar=4, foo=3))
#
# fullname = ['alfred', 'smokeTooMuch']
# print("Mr {name[1]}".format(name=fullname))
#
# import math
# tmpl = 'The {mod.__name__} module defines the value {mod.pi} for π'
# print(tmpl.format(mod=math))
#
# # 基本转换
# # str repr ascii
# print("{pi!s} {pi!r} {pi!a}".f
# ormat(pi='π'))
# print('The number is {num}'.format(num=42))
# print('The number is {num:f}'.format(num=42)) #小数
# print('The number is {num:b}'.format(num=42)) #二进制数
# # 宽度
# print('{num:10}'.format(num=3))
# print('{name:10}'.format(name='Bob'))
# # 精度
# print("Pi day is {pi:.2f}".format(pi=3.14))
# print("{pi:10.2f}".format(pi=3.14)) #
# # 千位分隔符
# print('one googol is {:,}'.format(10**100))
# # 用0填充
# print('{:010.2f}'.format(3.14))
# # 对齐 <左 ^中 >右
# print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}\n'.format(3.14))
# # 指定字符填充
# print("{:$^15}".format(" win big "))
# # =
# print("{0:10.2f}\n{1:10.2f}".format(3.14,-3.14))
# print("{0:10.2f}\n{1:=10.2f}".format(3.14,-3.14))
#
# print("{0:-.2}\n{1:-.2}".format(3.14,-3.14))
# print("{0:+.2}\n{1:+.2}".format(3.14,-3.14))
# print("{0: .2}\n{1: .2}".format(3.14,-3.14))
# # #
# print("{:b}".format(42))
# print("{:#b}".format(42)) # 二（八、十六）进制包含前缀
# print("{:#g}".format(42)) # 十进制包含小数点

# # 字符串方法
#
# # center在两边填充字符串让字符串居中
# print("The Middle by Jimmy Eat World".center(39))
# print("The Middle by Jimmy Eat World".center(39,"*"))
#
# # find 查找子串  in用来检查单个字符是否包含在字符串中
# # 找到 返回第一个字符的索引
# print('with a moo-moo here, and a moo-moo there'.find('moo'))
# # 找不到 返回-1
# title = "Monty Python's Flying Circus"
# print(title.find('cc'))
# # 指定搜索起点和终点
# subject = '$$$ Get rich now!!! $$$'
# print(subject.find('$$$'))
# print(subject.find('$$$',1)) # 指定起点
# print(subject.find('$$$',0,16)) # 指定起点和终点（包含起点不包含终点）
#
# # join 合并序列的元素
# # seq = [1,2,3,4,5]
# # sep = '+'
# # print(seq.join(sep)) # 0
#
# # seq = ['1','2','3','4','5']
# # print(seq.join()) # gg
#
# dirs = '', 'usr', 'bin', 'env'
# print('/'.join(dirs))
#
# # lower 小写
# print('Trondheim Hammer Dance'.lower())
#
# name ='Gumby'
# names = ['gumby','smith','jones']
# if name.lower() in names:
#     print('Found it!')
#
# # replace 将指定子串替换为另一个字符串，并返回替换后的结果
# print('This is a test'.replace('is','eez'))
#
# # split 将字符串拆分
# print('1+2+3+4+5'.split('+'))
# print('/usr/bin/env'.split('/'))
# print('Using the default'.split())
#
# # strip将字符串开头和末尾的空白删除，并返回删除后的结果
# print('   internal whitespace is kept   '.strip())
#
# names = ['gumby', 'smith', 'jones']
# name = '   gumby'
# if name.strip() in names:
#     print('Found it!')
# # 指定删除字符
# print('*** spam * for * everyone!!! ***'.strip(' *!'))
#
# # translate 单字符替换
# table = str.maketrans('cs','kz') # 创建转换表
# print(table) # 转换表是unicode码点之间的映射
# print("this is an incredible test".translate(table))
#
# table = str.maketrans('cs','kz',' ') # 删除所有空格
# print("this is an incredible test".translate(table))
#
# # 判断字符串是否满足特定的条件 is打头
# # isspace isdigit isupper ...


# ! 字典

# ? 创建字典
# items = [('name', 'Gumby'), ('age', 42)]
# d = dict(items)
# print(d)
# print(d['name'])
#
# d = dict(age=42, name='Gumby')
# print(d)

# ? --
# # len(d)
# # d[k]
# # d[k]=v
# # del d[k]
# # k in d
#
# x = {}
# x[42] = 'Foobar'
# print(x)
#
# ? 字典方法
# # clear 删除所有字典项
# d = dict(age=42, name='Gumby')
# d.clear()
# print(d)
#
# x = {}
# y = x
# x['key'] = 'value'
# print(y)
# x = {}  # 对y没有影响
# print(y)
#
# x = {}
# y = x
# x['key'] = 'value'
# print(y)
# x.clear()  # y也被清空了
# print(y)
#
# # copy 浅复制
# x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
# y = x.copy()
# y['username'] = 'mlh' #替换副本中的值，原件不受影响
# y['machines'].remove('bar') #修改副本中的值，原件也发生变化
# # 因为原件指向的也是被修改的值
# print(y)
# print(x)
#
# # deepcopy 深复制  同时复制值及其包含的所有值
# from copy import deepcopy
# d = {}
# d['names'] = ['Alfred', 'Bertrand']
# c = d.copy()
# dc = deepcopy(d)
# d['names'].append('Clive')
# print(c)
# print(dc)
#
# # fromkeys 创建新字典，其中包含指定的键且每个键值为None
# print({}.fromkeys(['name', 'key']))
# print(dict.fromkeys(['name', 'age']))
# print(dict.fromkeys(['name', 'age'], '(unknown)'))  # 指定值
#
# # get 访问字典中不存在的项不会引发错误
# d = {}
# print(d.get('name'))  # 返回None
# print(d.get('name', 'N/A'))  # 指定返回N/A
# # 如果字典包含指定的键,get与普通字典查找相同
# d['name'] = 'Eric'
# print(d.get('name'))
#
# # items返回一个包含所有字典项的列表（key,value）
# d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
# print(d.items())
# # 返回值是字典视图类型
# it = d.items()
# print(len(it))
# print(('spam', 0) in it)
# # 字典视图不复制
# d['spam'] = 1
# print(('spam', 0) in it)
# d['spam'] = 0
# print(('spam', 0) in it)
# # 将字典项复制到列表中
# print(list(d.items()))
#
# # pop 删除项
# d = {'x': 1, 'y': 2}
# d.pop('x')
# print(d)
#
# # popitem 随机弹出一个字典项
# d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
# d.popitem()
# print(d)
#
# # setdefault 获取与指定键关联的值
# # 与get的区别 ：字典中不包含指定的键时，在字典中添加指定的键值对
# d = {}
# d.setdefault('name', 'N/A')
# print(d)
#
# # update 用一个字典中的项来更新另一个字典
# d = {
#     'title': 'Python Web Site',
#     'url': 'http://www.python.org',
#     'changed': '2022-12-17'
# }
# x = {'title': 'Python Language Website'}
# d.update(x)
# print(d)
#
# # keys 返回一个由字典中的键组成的字典视图
# print(d.keys())
# # values 返回一个由字典中的值组成的字典视图
# print(d.values())
