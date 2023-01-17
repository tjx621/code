# 数制转换


# 基数：如十进制的基数为10、二进制的基数为2
# 权：对于一个M进制的数来说，小数点左边各位上对应的权值从左到右分别为基数的0次方、基数的1次方、基数的2次方等，
# 对于小数点右边各位上对应的权值从右到左分别为基数的-1次方、基数的-2次方等

# 二进制、八进制、十六进制向十进制转换的方法为：按权展开相加。
# 十进制转换成二进制、八进制、十六进制的方法为：整数部分除以基数取余数（取余的方向为从后向前），小数部分乘以基数取整数（取整的方向为从前向后）。
# 二进制、八进制、十六进制相互转换的方法为：先转换成十进制再转换成其他进制；
# 或者按照其对应关系进行转换（3位二进制数对应一位八进制数，4位二进制数对应一位十六进制数）

# 将字符转换为对应的数字，可以分两类进行考虑：
# 第一类是介于'0'到'9'之间的字符，转换成相应的数字0～9时，可利用其ASCII码之间的对应关系。
# 字符'0'的ASCII码为48，'1'的ASCII码为49，'1'-'0'=1（在0～127之间字符型与整型是可以通用的）得到的差即为字符ch对应的数字。
# 第二类是介于'A'到'Z'之间的字符，字符'A'对应的数字为10，'B'对应的数字为11，其他字母以此类推。
# Python为我们提供了以下函数，用于实现数字、字母和字符之间的转换。
# int(x)：将其他类型转换成数字。
# ord(x)：将字符转换成对应的Unicode码。
# str(x)：将其他类型转换成字符串。
# chr(x)：将十进制数字转换成对应的字符。

# 将字符转换为数字
def char_to_num(ch):
    if ch >= '0' and ch <= '9':
        return int(ch)
    else:
        return ord(ch)

# 将数字转换为字符
def num_to_char(num):
    if num >= 0 and num <= 9:
        return str(num)
    else:
        return chr(num)

# 其他数制转换为十进制
def source_to_decimal(temp, source):
    decimal_num = 0
    for i in range(len(temp)): # 
        decimal_num = (decimal_num * source) + char_to_num(temp[i])
    return decimal_num

# 十进制转换为其他数制
def decimal_to_object(decimal_num, object):
    decimal = []
    while decimal_num:
        decimal.append(num_to_char(decimal_num % object))
        decimal_num //= object
    return decimal

# 由余数组成的新数制数与余数的顺序是相反的，所以在输出新数的时候我们采用的是逆序输出的方式
def output(decimal):
    f = len(decimal) - 1
    while f >= 0:
        print(decimal[f], end='')
        f -= 1
    print()


# 使用flag使程序连续运行
if __name__ == '__main__':
    MAXCHAR = 101  # 允许的最大字符串长度
    flag = 1
    while flag:
        print("转换前的数是：", end='')
        temp = input()
        print("转换前的数制是：", end='')
        source = int(input())
        print("转换后的数制是：", end='')
        object = int(input())
        print("转换后的数是：", end='')
        decimal_num = source_to_decimal(temp, source)
        decimal = decimal_to_object(decimal_num, object)
        output(decimal)
        print("继续请输入1,否则输入0：")
        flag = int(input())
