class Student(object):
      def __init__(self, name):
         self.name = name
      def __str__(self):
         return 'Student object (name: %s)' % self.name
         __repr__ = __str__
Student('Nancy'); #Student object (name: Nancy)
#不使用print,直接显示变量调用的不是__str__()，而是__repr__()

#__iter__
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1; # 初始化两个计数器a，b
    def __iter__(self):
        return self;
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
     print(n)

#__getitem__ 根据下标从类中取出元素
class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f2 = Fib1();
# 按下标访问数列的任意一项
print(f2[0],f2[1],f2[2]);# 1  1  2

#__getattr__ 写一个__getattr__()方法，动态返回一个属性
class Student1(object):

    def __init__(self):
        self.name = 'Michael'
s1 = Student1();
# print(s1.score);#AttributeError: 'Student1' object has no attribute 'score

#写一个__getattr__()方法，动态返回一个属性,即使不存在的属性，也能避免报错
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age': #可以返回一个函数
            return lambda: 25

s=Student();
print(s.score,s.age());#99
print(s.gender); #None

#__call__()方法，定义直接在实例本身上调用
class Student2(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

s2 = Student2('Nancy');
s2(); #My name is Nancy.通过对象本身即可调用

#判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
print(
    callable(Student()), #false
    callable(max), #true
    callable([1, 2, 3]), #false
    callable(Student2('Nancy')), #true
    callable(None) #false
    );









