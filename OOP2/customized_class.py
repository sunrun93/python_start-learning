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







