from Hello import Hello;
h = Hello();
h.hello(); #Hello, world

h1 = Hello();
h1.hello('Nancy'); #Hello, Nancy.

print(type(Hello)); #<class 'type'>
#type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type

print(type(h1)); #<class 'Hello.Hello'>
#h1是一个实例，它的类型就是class Hello

#type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name='world'): # 先定义函数
   print('Hello, %s.' % name);

Hello1 = type('Hello', (object,), dict(hello=fn));
#依次传入三个参数：
#1.class的名称；
#2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
print(type(Hello1)); #<class 'type'>
h2 = Hello1();
print(type(h2)); #<class '__main__.Hello'>
