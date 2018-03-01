def lazy_sum(*args):
    def sum():
        ax = 0;
        for n in args:
            ax = ax+n;
        return ax;
    return sum; #将函数返回,闭包

f=lazy_sum(1,2,3,4);

print(f()); #调用函数f时，才真正计算求和的结果

f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1==f2); #False 每次调用都会返回一个新的函数，即使传入相同的参数

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i;
        fs.append(f);
    return fs
f1,f2,f3 = count();
print(f1(),f2(),f3()); #9 9 9

#返回函数不要引用任何循环变量，或者后续会发生变化的变量。
def count1():
    fs = [];
    for i in range(1,4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs

f1,f2,f3 = count1();
print(f1(),f2(),f3()); #1 4 9
