class Student(object):
    def __init__(self,name):
        self.name = name
s = Student('Bob');

print(s.name); # Bob

class People(object):
    gender = 'male';
b = People();
print(b.gender); #male
b.gender = 'female';
print(b.gender); #female

#实例属性属于各个实例所有，互不干扰；

#类属性属于类所有，所有实例共享一个属性；

#不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。


class StudentCount(object):
    count = 0

    def __init__(self, name):
        self.name = name
        StudentCount.count += 1; #  StudentCount.count =  StudentCount.count+1

if StudentCount.count != 0:
    print('测试失败!')
else:
    bart = StudentCount('Bart')
    if StudentCount.count != 1:
        print('测试失败!')
    else:
        lisa = StudentCount('Bart')
        if StudentCount.count != 2:
            print('测试失败!')
        else:
            print('Students:', StudentCount.count)
            print('测试通过!')


