def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-99)); #99
print(my_abs(-99,12));#TypeError: my_abs() takes 1 positional argument but 2 were given,参数个数不对，可以检查出来
#print(my_abs('a')); 
def nop():
    pass #暂时用pass占位，相当于TODO，缺少Pass运行会报错