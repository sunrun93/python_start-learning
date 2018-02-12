print(abs(-10));
print(max(1,5,-15,8));
print(int('123')); #123
print(int(12.34)); #12
print(float("12.34"));#12.34
print(float("12"));#12.0
print(str(100));
print(str(12.34));
print(bool(1));#True
print(bool(''));#False
print(hex(1));#0x1

from abstest import my_abs
print(my_abs(-222));#调用外部函数