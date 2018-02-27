print(abs(-10)); #10

print(abs); #<built-in function abs>

x = abs; #变量可以指向函数
print(x); #<built-in function abs>
print(x(-5)); #5

# abs = 10; #abs函数名也是一个变量，可重新赋值
# print(abs(-10)); #'int' object is not callable

# 既然变量可以指向函数，函数的参数能接收变量
# 那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x,y,f):
    return f(x)+f(y)

print(add(-5,20,abs)); #25

#高阶函数，让函数的参数能够接收别的函数