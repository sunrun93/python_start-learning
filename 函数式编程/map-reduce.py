from functools import reduce;

# map函数接收两个参数，一个是函数，一个是序列
# map将传入的函数依次作用到序列的每一个元素，并将结果作为list返回
def f(x):
    return x*x;

L = map(f, [1,2,3,4,5,6,7,8,9]);
print(list(L)); #[1, 4, 9, 16, 25, 36, 49, 64, 81]

#把这个list所有数字转为字符串
S = map(str,[1,2,3,4,5,6,7,8,9]);
print(list(S)); 
#['1', '2', '3', '4', '5', '6', '7', '8', '9']

# reduce函数接收两个参数，一个函数，一个序列
# reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

def add(x,y):
    return x+y;
L1 = reduce(add, [1,2,3,4,5,6,7,8,9]); # 45
print(L1);

# 把序列[1, 3, 5, 7, 9]变换成整数13579 
def fn(x,y):
    return 10*x+y;
L2 = reduce(fn,[1, 3, 5, 7, 9]); # 13579 
print(L2);

#-------------------------------------------------------------------
#char2num 将单个字符类型转成数值型
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];

print(char2num("9")); # 9
# 通过map将string类型的数字逐个转成number类型，并返回一个list
L3 = map(char2num,'12345');
print(list(L3)); # [1, 2, 3, 4, 5]
print(reduce(fn,map(char2num,'12345'))); # 12345
#--------------------------------------------------------------------

# string to number
def str2num(s):
    def fun(x,y):
        return 10*x+y;
    def char2num1(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];
    return reduce(fun,map(char2num1,s));

print(str2num('344345')); #344345
    