# 多态
# 封装
# 继承

# class Person:
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def greet(self):
#         print("hello,world! I'm {}.".format(self.name))
#
#
# foo = Person()
# bar = Person()
# foo.set_name('Luke Skywalker')
# bar.set_name('Anakin Skywalker')
# foo.greet()
# bar.greet()
#
# print(foo.name)
#
# bar.name = 'Yoda'
# bar.greet()
#
#
# # 私有方法/属性 名称以两个下划线打头
# # 从外部不能访问__inaccessible 但在类中可以使用它
#
# class Secretive:
#
#     def __inaccessible(self):
#         print("Bet you can't see me ...")
#
#     def accessible(self):
#         print("The secret message is:")
#         self.__inaccessible()
#
#
# s = Secretive()
# # s.__inaccessible()
# s.accessible()
# # 类定义对两个下划线的名称进行转换：开头加下划线和类名
# s._Secretive__inaccessible()
#
#
# class MemberCounter:
#     members = 0
#
#     def init(self):
#         MemberCounter.members += 1
#
#
# m1 = MemberCounter()
# m1.init()
# print(MemberCounter.members)
#
# m2 = MemberCounter()
# m2.init()
# print(MemberCounter.members)
#
# print(m1.members)
# print(m2.members)
#
# m1.members = 'Two'
# print(m1.members)
# print(m2.members)
#
#
# # 继承
# class Filter:
#     def init(self):
#         self.blocked = []
#
#     def filter(self, sequence):
#         return [x for x in sequence if x not in self.blocked]
#
#
# class SPAMFilter(Filter):
#     def init(self):
#         self.blocked = ['SPAM']
#
#
# f = Filter()
# f.init()
# print(f.filter([1, 2, 3]))
#
# s = SPAMFilter()
# s.init()
# print(s.filter(['SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM']))
#
# # 判断一个类是否是另一个类的子类 issubclass()
# print(issubclass(SPAMFilter, Filter))
# print(issubclass(Filter, SPAMFilter))
#
# # 查看一个类的基类 __bases__
# print(SPAMFilter.__bases__)
# print(Filter.__bases__)
#
# # 确定对象是否是特定类的实例 isinstance()
# s = SPAMFilter()
# print(isinstance(s, SPAMFilter))
# print(isinstance(s, Filter))
# print(isinstance(s, str))
#
# # 查看对象所属的类
# print(s.__class__)
#
#
# # 多重继承
# class Calculator:
#     def calculate(self, expression):
#         self.value = eval(expression)
#
#
# class Talker:
#     def talk(self):
#         print('Hi, my value is', self.value)
#
#
# class TalkingCalculator(Calculator, Talker):
#     pass
#
#
# tc = TalkingCalculator()
# tc.calculate('1+2*3')
# tc.talk()
#
#
# # 抽象类
# from abc import ABC, abstractmethod
# class Talker(ABC):
#     @abstractmethod
#     def talk(self):
#         pass
#
# # 抽象类不能实例化
# # Talker()
#
# class Knigget(Talker):
#     def talk(self):
#         print('Ni!')
#
# k = Knigget()
# print(isinstance(k, Talker))
# k.talk()

# 构造函数
# class FooBar:
#     def __init__(self):
#         self.somevar = 42
#
#
# f = FooBar()
# print(f.somevar)
#
#
# class FooBar:
#     def __init__(self, value=42):
#         self.somevar = value
#
#
# f = FooBar('This is a constructor argument')
# print(f.somevar)


# 继承时重写普通方法
# class A:
#     def hello(self):
#         print("Hello, I'm A.")
#
#
# class B(A):
#     pass
#
#
# a = A()
# b = B()
# a.hello()
# b.hello()
#
#
# class B(A):
#     def hello(self):
#         print("Hello, I'm B.")
#
#
# b = B()
# b.hello()


# # 继承时重写构造函数
# class Bird:
#     def __init__(self):
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print('Aaaah ...')
#             self.hungry = False
#         else:
#             print('No, thanks!')
#
#
# b = Bird()
# b.eat()
# b.eat()
#
#
# class SongBird(Bird):
#     def __init__(self):
#         # 调用未关联的超类构造函数
#         # Bird.__init__(self) # 旧版本
#         super().__init__()  # 新版本
#         self.sound = 'Squawk!'
#
#     def sing(self):
#         print(self.sound)
#
#
# sb = SongBird()
# sb.sing()
# # sb.eat()  # 'SongBird' object has no attribute 'hungry'
# sb.eat()
# sb.eat()


# 元素访问
# 1. 基本的序列和映射协议
# __len__(self)
# __getitem__(self,key)
# __setitem__(self,key,value)
# __delitem__(self,key)


# # 创建一个无穷序列
# def check_index(key):
#     if not isinstance(key, int):
#         raise TypeError
#     if key < 0:
#         raise IndexError
#
#
# class ArithmeticSequence:
#     def __init__(self, start=0, step=1):
#         self.start = start
#         self.step = step
#         self.changed = {}
#
#     def __getitem__(self, key):
#         check_index(key)
#         try:
#             return self.changed[key]
#         except KeyError:
#             return self.start + key * self.step
#
#     def __setitem__(self, key, value):
#         check_index(key)
#         self.changed[key] = value
#
#
# s = ArithmeticSequence(1, 2)
# print(s[4])
#
# s[4] = 2
# print(s[4])
#
# print(s[5])
#
#
# # 2. 从list、dict、str派生
# class CounterList(list):
#     def __init__(self, *args):
#         super().__init__(*args)
#         self.counter = 0
#
#     def __getitem__(self, index):
#         self.counter += 1
#         return super(CounterList, self).__getitem__(index)
#
#
# c1 = CounterList(range(10))
# print(c1)
#
# c1.reverse()
# print(c1)
#
# del c1[3:6]
# print(c1)
#
# print(c1.counter)
#
# print(c1[4] + c1[2])
#
# print(c1.counter)


# 特性 通过存取方法定义的属性
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#
#     def set_size(self, size):
#         self.width, self.height = size
#
#     def get_size(self):
#         return self.width, self.height
#
#     size = property(get_size, set_size)
#
#
# r = Rectangle()
# r.width = 10
# r.height = 5
# print(r.get_size())
# r.set_size((150, 100))
# print(r.width)
# print(r.height)
#
# print(r.size)


# # 装饰器
# class MyClass:
#     @staticmethod
#     def smeth():
#         print("This is a static method")
#
#     @classmethod
#     def cmeth(cls):
#         print("This is a class method of", cls)
#
#
# MyClass.smeth()
# MyClass.cmeth()


# # 魔法方法重写Rectangle类
# # __getattr__(self, name)：在属性被访问而对象没有这样的属性时自动调用。
# # __setattr__(self, name, value)：试图给属性赋值时自动调用
# class Rectangle:
#     def __init__(self):
#         self.width = 0
#         self.height = 0
#
#     def __setattr__(self, name, value):
#         if name == 'size':
#             self.width, self.height = value
#         else:
#             self.__dict__[name] = value
#
#     def __getattr__(self, name):
#         if name == 'size':
#             return self.width, self.height
#         else:
#             raise AttributeError()



# class Fibs:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         return self.a
#
#     def __iter__(self):
#         return self
#
#
# fibs = Fibs()
#
# for f in fibs:
#     if f > 1000:
#         print(f)
#         break

# 迭代器
# it = iter([1, 2, 3])
# print(next(it))
# print(next(it))
# print(next(it))

# # 从迭代器创建序列
# class TestIterator:
#     value = 0
#
#     def __next__(self):
#         self.value += 1
#         if self.value > 10:
#             raise StopIteration
#         return self.value
#
#     def __iter__(self):
#         return self
#
#
# ti = TestIterator()
# print(list(ti))


# 生成器不是使用return返回一个值，而是可以生成多个值，每次一个。
# 每次使用yield生成一个值后，函数都将冻结，即在此停止执行，等待被重新唤醒。
# 被重新唤醒后，函数将从停止的地方开始继续执行。

def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element  #


nested = [[1, 2], [3, 4], [5]]
for num in flatten(nested):
    print(num)

print(list(flatten(nested)))


# 递归式生成器
def flatten(nested):
    try:
        #############
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        #############
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten([[[1], 2], 3, 4, [5, [6, 7]], 8])))
print(list(flatten(['foo', ['bar', ['baz']]])))


# 通用生成器

# 生成器是包含关键字yield的函数，但被调用时不会执行函数体内的代码，而是返回一个迭代器。
# 每次请求值时，都将执行生成器的代码，直到遇到yield或return。
# yield意味着应生成一个值
# return意味着生成器应停止执行（即不再生成值；仅当在生成器调用return时，才能不提供任何参数）。

# 生成器由两个单独的部分组成：生成器的函数和生成器的迭代器。
# 生成器的函数是由def语句定义的，其中包含yield。
# 生成器的迭代器是这个函数返回的结果。
def simple_generator():
    yield 1


print(simple_generator)  # <function simple_generator at 0x000001DEA1AF39A0>
print(simple_generator())  # <generator object simple_generator at 0x000001DEA18EA5E0>


# 生成器的方法
def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new

r = repeater(42)
print(next(r))
print(r.send("hello, world!"))

# 模拟生成器
def flatten(nested):
    result = []
    try:
        try:
            nested + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result