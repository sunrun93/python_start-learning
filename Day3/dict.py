A = {'Michael': 95, 'Bob': 75, 'Tracy': 85};
print(A['Michael']);# 95
#print(A['ABC']);#KeyError: 'ABC'
A['Jenny'] = 100;
print(A);#{'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Jenny': 100}
print('Thomas' in A); #False
print(A.get('Thomas'));#None
print(A.get('ABC','NOT FIND'));#NOT FIND
A.pop('Bob');
print(A);#{'Michael': 95, 'Tracy': 85, 'Jenny': 100}

B ={'Michael': 95, 'Bob': 75, 'Tracy': 85};
print(list(B)); #['Michael', 'Bob', 'Tracy']
print(list(B)[::-1]); #['Tracy', 'Bob', 'Michael']
