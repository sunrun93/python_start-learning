# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
from functools import reduce;
def str2float(s):
    s = s.split('.');
    def fn1(x,y):
        return x*10+y;
    def fn2(x,y):
        return x/10+y;
    def char2num(str):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[str];
    return reduce(fn1,map(char2num,s[0]))+reduce(fn2,list(map(char2num,s[1]))[::-1])/10;
    #这段代码用了split分切字符串，用了[::-1]翻转list

floatNum = str2float('123.456');
print(floatNum);
