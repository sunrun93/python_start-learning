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
