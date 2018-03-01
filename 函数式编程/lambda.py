# 匿名函数
#关键字lambda表示匿名函数，冒号前面的x表示函数参数。
l = map(lambda x: x*x,[1,2,3,4,5,6,7,8,9]);
print(list(l)); #[1, 4, 9, 16, 25, 36, 49, 64, 81]

def build(x, y):
    return lambda: x * x + y * y;
print(build(4,5)()); #41

def build(x, y):
    return lambda x,y: x * x + y * y;
print(build(4,5)(4,5)); #41

#需要注意lambda是否传入参数