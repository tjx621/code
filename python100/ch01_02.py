# 有一对兔子，从出生后的第3个月起每个月都生一对兔子。
# 小兔子长到第3个月后每个月又生一对兔子，
# 假设所有的兔子都不死，问30个月内每个月的兔子总对数为多少？

# 月份 小兔子 中兔子 大兔子
# 1 1 0 0
# 2 0 1 0
# 3 1 0 1
# 4 1 1 1
# 5 2 1 2
# 6 3 2 3
# 7 5 3 5

# 1 1 2 3 5 8 13 ...

def fib(month):
    result = [1, 1]
    for i in range(month - 2):
        result.append(result[-1] + result[-2])
    return result[-1]




print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))

print(fib(30))



