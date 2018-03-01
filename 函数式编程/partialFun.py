print(int('12345')); #12345
print(int('12345',base=8));#5349
print(int('12345',base=16));#74565

def intx(x):
    return int(x,base = 8);
print(intx('12345')) #5349

#偏函数functools.partial就是帮助我们创建一个偏函数的
#不需要我们自己定义int2()
print(int('10101010',base=2)); #170
import functools
int2 = functools.partial(int, base=2);
print(int2('10101010'));#170
int8 = functools.partial(int, base=8);
print(int8('12345')); #5349
#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住
max2 = functools.partial(max, 10);
print(max2(5,6,9));#10 相当于max(5,6,9,10);
print(max2(99,5,6));#99
