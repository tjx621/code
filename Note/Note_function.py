# # 斐波那契数
# fibs = [1, 1]
# for i in range(8):
#     fibs.append(fibs[-2] + fibs[-1])
# print(fibs)
#
# # 判断某个对象是否可调用 callable
# x = 1
# print(callable(x))
#
# import math
#
# y = math.sqrt
# print(callable(y))
#
#
# # 斐波那契数
# def fibs(num):
#     '计算斐波那契数列'
#     result = [1, 1]
#     for i in range(num - 2):
#         result.append(result[-2] + result[-1])
#     return result
#
#
# print(fibs(10))
# print(fibs.__doc__)  # 文档字符串
# print(help(fibs))  # 获取有关函数的信息
#
#
# # 位置参数
# # 修改参数
# def try_to_change(n):
#     n = 'Mr. Gumby'
#
#
# name = 'Mrs.Entity'
# try_to_change(name)
# print(name)  # 修改不了
# 等价
# name = 'Mrs.Entity'
# n = name
# n = 'Mr. Gumby'
# print(name)
#
#
# def change(n):
#     n[0] = 'Mr. Gumby'
#
# names = ['Mrs. Entity', 'Mrs. Thing']
# change(names)
# print(names)  # 可以修改
#
# names = ['Mrs. Entity', 'Mrs. Thing']
# n = names  # 两个变量指向同一个列表
# n[0] = 'Mr. Gumby'
# print(names)
#
# names = ['Mrs. Entity', 'Mrs. Thing']
# n = names[:]  # 创建副本
# print(n is names)
# print(n == names)
#
# n[0] = 'Mr. Gumby'
# print(n)
# print(names)
#
# change(names[:])
# print(names)
#
#
# # 实现功能：存储姓名并能让用户根据名字、中间名或姓找人
# def init(data):
#     data['first'] = {}
#     data['middle'] = {}
#     data['last'] = {}
#
#
# # 测试
# # storage = {}
# # init(storage)
# # print(storage)
#
# def lookup(data, label, name):
#     return data[label].get(name)
#
#
# # 测试
# # print(lookup(storage, 'middle', 'Lie'))
#
# def store(data, full_name):
#     names = full_name.split()
#     if len(names) == 2:
#         names.insert(1, '')
#     labels = 'first', 'middle', 'last'
#     for label, name in zip(labels, names):
#         people = lookup(data, label, name)
#         if people:
#             people.append(full_name)
#         else:
#             data[label][name] = [full_name]
#
#
# MyNames = {}
# init(MyNames)
# store(MyNames, 'Magnus Lie Hetland')
# print(lookup(MyNames, 'middle', 'Lie'))
#
# store(MyNames, 'Robin Hood')
# store(MyNames, 'Robin Locksley')
# print(lookup(MyNames, 'first', 'Robin'))
#
# store(MyNames, 'Mr.Gumby')
# print(lookup(MyNames, 'middle', ''))
#
#
# # 关键字参数
# def hello_1(greeting, name):
#     print('{}, {}'.format(greeting, name))
#
#
# def hello_2(name, greeting):
#     print('{}, {}'.format(name, greeting))
#
#
# hello_1(name='world', greeting='hello')
# hello_2(name='world', greeting='hello')
#
#
# # 指定默认值
# def hello_3(greeting='Hello', name='world'):
#     print('{},{}!'.format(greeting, name))
#
#
# hello_3()
# hello_3('Grrr')
# hello_3(name='Grrr')
#
#
# # 收集参数
# def print_params(*params):
#     print(params)
#
#
# print_params('Testing')
# print_params(1, 2, 3)  # 元组
#
#
# # 收集余下的参数
# def print_params_2(title, *params):
#     print(title)
#     print(params)
#
#
# print_params_2('Params:', 1, 2, 3)
# print_params_2('Nothing:')
#
#
# # 收集中间参数
# def in_the_middle(x, *y, z):
#     print(x, y, z)
#
#
# # in_the_middle(1,2,3,4,5,6,7)
# in_the_middle(1, 2, 3, 4, 5, 6, z=7)
#
#
# # 收集关键字参数
# def print_params_3(**params):
#     print(params)
#
#
# print_params_3(x=1, y=2, z=3)  # 字典
#
#
# def print_params_4(x, y, z=3, *pospar, **keypar):
#     print(x, y, z)
#     print(pospar)
#     print(keypar)
#
#
# print_params_4(1, 2, 3, 4, 5, 6, 7, foo=1, bar=2)
# print_params_4(1, 2)
#
#
# # 分配参数
# def add(x, y):
#     return x + y
#
#
# params = (1, 2)
# print(add(*params))
#
#
# # 小练习
# def story(**kwds):
#     return 'Once upon a time, there was a {job} called {name}.'.format_map(kwds)
#
#
# print(story(job='king', name='Gumby'))
# print(story(name='Sir Robin', job='brave knight'))
#
# params = {'job': 'language', 'name': 'python'}
# print(story(**params))
#
# del params['job']
# print(story(job='stroke of genius', **params))
#
#
# def power(x, y, *others):
#     if others:
#         print('Received redundant parameters:', others)
#     return pow(x, y)
#
#
# print(power(2, 3))
# print(power(3, 2))
# print(power(y=3, x=2))
#
# params = (5,) * 2
# print(power(*params))
#
# print(power(3, 3, 'Hello,world'))
#
#
# def interval(start, stop=None, step=1):
#     if stop is None:
#         start, stop = 0, start
#     result = []
#     i = start
#
#     while i < stop:
#         result.append(i)
#         i += step
#     return result
#
#
# print(interval(10))
# print(interval(1, 5))
# print(interval(3, 12, 4))
# print(power(*interval(3, 7)))
#
#
# # 递归
# # 阶乘
# def factorial(n):
#     result = n
#     for i in range(1, n):
#         result *= i
#     return result
#
#
# print(factorial(3))
#
#
# def factorial_recursion(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial_recursion(n - 1)
#
#
# print(factorial_recursion(3))
#
#
# # 幂
# def my_pow(x, n):
#     result = 1
#     for i in range(n):
#         result *= x
#     return result
#
# print(my_pow(3, 2))
#
#
# def my_pow_recursion(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * my_pow_recursion(x, n - 1)
#
#
# print(my_pow_recursion(3, 3))
#
#
# # 二分查找
# def search(sequence, number, lower, upper):
#     if lower == upper:
#         return upper
#     else:
#         middle = (lower + upper) // 2
#         if number > sequence[middle]:
#             return search(sequence, number, middle + 1, upper)
#         else:
#             return search(sequence, number, lower, middle)
#
#
# seq = [34, 67, 8, 123, 4, 100, 95]
# seq.sort()
# print(seq)
# print(search(seq, 34, 0, 6))
