#迭代是通过for ... in来完成的,Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
d={'a':1,'b':2,'c':3}
for key in d:
    print(key);

for key in 'ABC':
    print(key);

#通过collections模块的Iterable类型判断,判断一个对象是可迭代对象
from collections import Iterable
print(isinstance('abc', Iterable)); #True
print(isinstance([1,2,3],Iterable)); #True
print(isinstance(123,Iterable));#False

#enumerate函数: 把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i,value in enumerate(['A','B','C']):
    print(i,value)  #0  A  1  B  2  C

#for循环中同时使用两个变量
for x,y in [(1,1),(2,2),(3,3)]:
    print(x, y)  1 1   2 2   3 3

