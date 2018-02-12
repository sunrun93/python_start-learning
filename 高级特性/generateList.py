L1 = list(range(1,11));#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L1);

#生成[1x1, 2x2, 3x3, ..., 10x10]
L2 = [];
for i in range(1,11):
    L2.append(i*i)

print(L2);#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#列表生成式则可以用一行语句代替循环生成上面的list：
L3 = [x*x for x in range(1,11)];  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(L3);

L4 = [x*4 for x in range(1,11)];  #[4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
print(L4);

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
L5 = [x*x for x in range(1,11) if x%2==0]; #[4, 16, 36, 64, 100]
print(L5);

#使用两层循环，可以生成全排列
L6 =[m+n for m in 'ABC' for n in 'XYZ']; #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print(L6);

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x':'A','y':'B','z':'C'};
print(d.items()); #dict_items([('x':'A'),('y':'B'),('z':'C')])

for k, v in d.items():
    print(k, '=', v);

L7 = [k+'='+v for k,v in d.items() ]; #['y=B', 'x=A', 'z=C'] 因为dict的存储顺序不一定
print(L7);

L8 = [s.lower() for s in ['Hello', 'World', 'IBM', 'Apple']]; #['hello', 'world', 'ibm', 'apple']
print(L8);

L9 = [s.lower() for s in ['Hello', 'World', 18, 'Apple', None] if isinstance(s,str) == True]; #['hello', 'world', 'apple']
print(L9);

L10 = [];
for s in ['Hello', 'World', 18, 'Apple', None]:
    if isinstance(s,str):
        L10.append(s.lower())
    else:
        L10.append(s)
print(L10); #['Hello', 'World', 18, 'Apple', None]
