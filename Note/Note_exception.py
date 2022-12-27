# 内置异常
# raise Exception
# raise Exception('hyperdrive overload')

# 自定义异常
class Custom(Exception):
    pass


# 捕获异常：对异常进行处理 try/except
# x = int(input('Enter the first number: '))
# y = int(input('Enter the first number: '))
# print(x/y)

# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the first number: '))
#     print(x/y)
# except ZeroDivisionError:
#     print("The second number can't be zero")

# 捕获异常后，如果要重新引发它，可调用raise且不提供任何参数
# class MuffledCalculator:
#     muffled = False
#
#     def calc(self, expr):
#         try:
#             return eval(expr)
#         except ZeroDivisionError:
#             if self.muffled:
#                 print('Division by zero is illegal')
#             else:
#                 raise
#
#
# calculator = MuffledCalculator()
# print(calculator.calc('10/2'))
# # print(calculator.calc('10/0')) #关闭了抑制功能
#
# calculator.muffled = True
# print(calculator.calc('10/0'))

# try:
#     1/0
# except ZeroDivisionError:
#     raise ValueError

# try:
#     1/0
# except ZeroDivisionError:
#     raise ValueError from None

# 多个except子句
# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the first number: '))
#     print(x/y)
# except ZeroDivisionError:
#     print("The second number can't be zero")
# except TypeError:
#     print("That wasn't a number, was it?")

# 在一个元组中指定异常
# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the first number: '))
#     print(x/y)
# except (ZeroDivisionError, TypeError, NameError):
#     print("The second number can't be zero")

# 要在except子句中访问异常对象本身，可使用两个而不是一个参数
# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the first number: '))
#     print(x/y)
# except (ZeroDivisionError, TypeError) as e: # 推荐
#     print(e)  # 让程序打印发生的异常并继续运行

# 一网打尽 不推荐
# try:
#     x = int(input('Enter the first number: '))
#     y = int(input('Enter the first number: '))
#     print(x/y)
# except :
#     print("something wrong happened...")

# 在没有出现异常时执行一个代码块
# try:
#     print('A simple task')
# except:
#     print("What? Something went wrong?")
# else:
#     print('Ah ... It went as planned')

# 仅当没有引发异常时，才会跳出循环
# while True:
#     try:
#         x = int(input('Enter the first number: '))
#         y = int(input('Enter the second number: '))
#         value = x / y
#         print('x / y is', value)
#     except:
#         print('Invalid input. Please try again.')
#     else:
#         break


# while True:
#     try:
#         x = int(input('Enter the first number: '))
#         y = int(input('Enter the second number: '))
#         value = x / y
#         print('x / y is', value)
#     except Exception as e:
#         print('Invaild input:', e)
#         print('Please try again')
#     else:
#         break


# 不管try子句中发生什么异常，都将执行finally子句
# x = None  # 如果初始化x，ZeroDivisionError将导致根本没有机会给它赋值，进而导致在
# # finally子句中对其执行del时引发未捕获的异常。
# try:
#     x = 1/0
# finally:
#     print('Cleaning up ...')
#     del x

# try:
#     1 / 0
# except NameError:
#     print("Unknown variable")
# else:
#     print("That went well!")
# finally:
#     print("Cleaning up.")



# 异常和函数有着天然的联系。如果不处理函数中引发的异常，它将向上传播到调用函数的地方。
# 如果在那里也未得到处理，异常将继续传播，直至到达主程序（全局作用域）。
# 如果主程序中也没有异常处理程序，程序将终止并显示栈跟踪消息。

# def faulty():
#     raise Exception('Something is wrong')
#
# def ignore_exception():
#     faulty()
#
# def handle_exception():
#     try:
#         faulty()
#     except:
#         print('Exception handled')

# ignore_exception()
# handle_exception()


# def describe_person(person):
#     print('Description of', person['name'])
#     print('Age:', person['age'])
#     if 'occupation' in person:
#         print('Occupation:', person['occupation'])
#
# # 两次查找'occupation'键：一次检查这个键是否存在（在条件中），另一次获取这个键关联的值
# describe_person({'name':'TJX', 'age':22})
# describe_person({'name':'TJX', 'age':22, 'occupation':'camper'}) # 效率不高



# # 假设存在occupation键
# def describe_person(person):
#     print('Description of', person['name'])
#     print('Age:', person['age'])
#     try:
#         print('Occupation:', person['occupation'])
#     except KeyError:
#         pass


# # 警告
# from warnings import warn
# warn("I've got a bad feeling about this.")
#
# # 抑制警告并指定要采取的措施，如error和ignore
# from warnings import filterwarnings
# filterwarnings('ignore')
# warn("Anyone out there?")
# filterwarnings("error")
# warn('Something is very wrong!')