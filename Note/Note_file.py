# 1. 文件基本操作
# f = open('somefile.txt')

# r 读
# w 写
# x 从文件开头写入
# a 在末尾追加

# b 二进制模式
# t 文本模式
# + 读写模式

# r+ vs w+

# f = open('somefile.txt', 'w')
# f.write('Hello, ')
# f.write('World!')
# f.close()

# f = open('somefile.txt', 'r')
# print(f.read(4))  # 输出前4个字符
# print(f.read())   # 输出剩余字符

# f = open(r'somefile.txt')
# print(f.read(7))
# print(f.read(4))
# f.close()

# f = open(r'somefile.txt')
# print(f.read())
# f.close()

# f = open(r'somefile.txt')
# for i in range(3):
#     print(str(i) + ':' + f.readline(), end='')
# f.close()

# import pprint
# pprint.pprint(open(r'somefile.txt').readlines())

# f = open(r'somefile.txt', 'w')
# f.write('this\nis no\nhaiku')
# f.close()

# f = open(r'somefile.txt')
# lines = f.readlines()
# print(lines)
# f.close()

# lines[1] = "isn't a\n"
# f = open(r'somefile.txt', 'w')
# f.writelines(lines)
# f.close()

# 2. 迭代文件内容
def process(string):
    print('Processing:',string)
# 每次一个字符/字节
with open('somefile.txt') as f:
    char = f.read(1)
    while char:
        process(char)
        char = f.read(1)
        # 到达文件末尾时，read会返回一个空字符串

with open('somefile.txt') as f:
    while True:
        char = f.read(1)
        if not char:
            break
        process(char)

# 每次一行
with open('somefile.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break
        process(line)

# 读取所有内容
with open('somefile.txt') as f:
    for char in f.read():
        process(char)

with open('somefile.txt') as f:
    for line in f.readlines():
        process(line)

# 使用fileinput 实现延迟行迭代
import fileinput
for line in fileinput.input('somefile.txt'):
    process(line)

# 文件迭代器
with open('somefile.txt') as f:
    for line in f:
        process(line)

for line in open('somefile.txt'):
    process(line)

# 使用list(open(filename))将其转换为字符串列表，其效果与使用readlines相同。
f = open('somefile.txt', 'w')
# print写入文件，自动在提供的字符串后面添加换行符
print('First', 'line', file=f)
print('Second', 'line', file=f)
print('Third', 'and final', 'line', file=f)
f.close()

lines = list(open('somefile.txt'))
print(lines)

first, second, third = open('somefile.txt')
print(first)
print(second)
print(third)
