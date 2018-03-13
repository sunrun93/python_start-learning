# type() - 判断对象类型
print(
    type(123), #<class 'int'>
    type("ABC"), #<class 'str'>
    type(True), #<class 'bool'>
    type(None) #<class 'NoneType'>
);

print(
    type(123)==type(456), #True
    type('ABC')==str #True
)

import types;   #判断函数类型

def fun():
    pass;
print(
    type(fun), #<class 'function'>
    type(abs), #<class 'builtin_function_or_method'>
     type(lambda x: x), #<class 'function'>
     type((x for x in range(10))) #<class 'generator'>
); 

#isinstance() class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数

class Animal(object):
    def run(self):
        print('Animal is running...');

class Dog(Animal):
    pass;

class Cat(Animal):
    pass;

a = Animal();
d = Dog();
print(isinstance(a,Animal)); #True
print(isinstance(d,Dog)); #True
print(isinstance(d,Animal)); #True
print(isinstance(d,Dog) and isinstance(d,Animal)); #True

#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple))); #True
print(isinstance((1, 2, 3), (list, tuple))); #True

#dir()  获得一个对象的所有属性和方法
print(dir('ABC'));

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度
print('ABC'.__len__()); #3
print(len('ABC')); #3

#把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态