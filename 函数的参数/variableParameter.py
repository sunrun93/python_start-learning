def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1,2,3])); #14

#把函数的参数调整为可变参数
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
def calc_1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc_1(1, 2, 3));#14
print(calc_1(3));#9
print(calc_1());#0

#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1,2,3];
print(calc_1(*nums));#14

