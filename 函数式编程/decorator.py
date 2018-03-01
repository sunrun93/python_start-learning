#decorator装饰器
# def now1():
#     print("2018-3-1");
#     print(now1.__name__);#now
# now1();

#在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)#call now():
        return func(*args, **kw)
    return wrapper

@log
def now():
    print(now.__name__);#wrapper
now();