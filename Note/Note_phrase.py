# # print
# print('Age:', 42)
#
# name = 'Gumby'
# salutation = 'Mr.'
# greeting = 'Hello'
# print(greeting, salutation, name)
# print(greeting + ',', salutation, name)
#
# print("I", "am", "TJX", sep="_")  # 自定义分隔符
# print('Hello, ', end='')  # 自定义结束字符串

# import

# import somemodule
# from somemodule import somefunction
# from somemodule import somefunction,anotherfunction,...
# from somemodule import * 导入模块中的一切
# import somemodule as sm  给模块取别名
# from somemodule import somefunction as sf 给函数取别名


# 赋值
# # 序列解包
# x, y, z = 1, 2, 3
# print(x, y, z)
#
# # 交换值
# x, y = y, x
# print(x, y)
#
# values = 1, 2, 3
# print(values)
# x, y, z = values
# print(x)
#
# scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
# key, value = scoundrel.popitem()
# print(key, value)
#
# # 要解包的序列包含的元素个数必须与等号左边列出的目标个数相同
# # x,y,z = 1,2
# # x,y,z = 1,2,3,4
# 使用*收集多余的值
# a, b, *rest = [1, 2, 3, 4]
# print(rest)
#
# name = "Albus Percival Wulfric Brian Dumbledore"
# first, *middle, last = name.split() # 将带*的变量放在其他位置
# print(middle)
#
# a, *b, c = "abc"
# print(a, b, c)  # 带*的变量是一个列表

# 链式赋值
# 将多个变量关联到同一个值
# x = y = somefunction()
# 等价
# y = somefunction()
# x = y
# 不等价
# x = somefunction()
# y = somefunction()


# 增强赋值 如x+=1

# 代码块 ：

# 条件语句
# if elif else
# 条件表达式 --- x if 条件 else y ---- 条件真 x  条件假 y

# x is y / x is not y  x,y是不是同一个对象
# ==用来检查两个对象是否相等 is用来检查两个对象是否相同
# x in y / x not in y  x是不是容器y的成员

# 链式比较

# 断言 assert 让程序在错误条件出现时立即崩溃
# age = 10
# assert 0 < age < 100
# age = -1
# assert 0 < age < 100, 'The age must be realistic'
# AssertionError: The age must be realistic


# 循环语句
# for number in range(0,10):
#     print (number, end=' ')

# 迭代字典
# d = {'x':1, 'y':2, 'z':3}
# for key in d:
#     print(key, 'corresponds to', d[key])
# for key,value in d.items():
#     print(key, 'corresponds to', value)

# # 并行迭代
# names = ['anne', 'beth', 'george', 'damon']
# ages = [12, 45, 32, 102]
# # for i in range(len(names)):
# #     print(names[i], 'is', ages[i], 'years old')
# list(zip(names, ages))  # zip 将两个序列缝合起来并返回一个由元组组成的序列
# for name, age in zip(names, ages):  # 在循环中将元组解包
#     print(name, 'is', age, 'years old')
# # 用完最短的序列就停止缝合
# print(list(zip(range(5), range(10))))
#
# # 迭代时获取索引 enumerate
# # sorted() 排序后再迭代
# # reversed() 反向迭代
#
# # while True-break
#
# # 判断循环是否提前结束 for-else
# from math import sqrt
#
# for n in range(99, 81, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break
# else:
#     print("Did't find it!")
#
# # 列表推导
# print([x * x for x in range(10)])
# print([x * x for x in range(10) if x % 3 == 0])
# print([(x,y) for x in range(3) for y in range(3)])
#
# # 将首字母相同的男孩女孩进行配对
# girls = ['alice', 'bernice', 'clarice']
# boys = ['chris', 'arnold', 'bob']
# print([b+'+'+g for b in boys for g in girls if b[0]==g[0]])
#
# # 字典推导
# # for前面冒号分隔俩表达式 键-值
# squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}
# print(squares[8])

# pass
# del
# exec 将字符串作为代码执行
# eval 计算用字符串表示的python表达式的值，并返回结果
