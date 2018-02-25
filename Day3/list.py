classMate = ['A','B','C'];
otherList = [123,'ABC',True];
print(classMate);#['A', 'B', 'C']
print(otherList);#[123, 'ABC', True]
print(len(otherList));#3
print(otherList[-1]);#True
classMate.append('D')
print(classMate);#['A', 'B', 'C', 'D']
otherList.insert(2,False);
print(otherList);#[123, 'ABC', False, True]
otherList.pop(1);
print(otherList);#[123, False, True]
