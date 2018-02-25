t=(1,2,3);
print(t);#(1,2,3)
print(len(t));#3
#t[0]=4;#TypeError: 'tuple' object does not support item assignment
t=(1);#1
print(t);
t=(1,);#(1,)
print(t);
t = ('A','B',['a','b']);
t[2][0]='X';
t[2][1]='Y';
print(t);#('A', 'B', ['X', 'Y'])
