class Student(object):
    pass;

s = Student();
s.name='Nancy';
print(s.name);

def set_age(self,age): #定义一个函数作为实例的方法
    self.age = age;

from types import MethodType
s.set_age = MethodType(set_age,s) #给实例s绑定一个方法,只对s实例起作用
s.set_age(25);
print(s.age); #25

s2 = Student();
#s2.set_age(26); #'Student' object has no attribute 'set_age'

#若要给所有实例绑定方法，应对整个class操作
def set_score(self,score):
    self.score = score;

Student.set_score = set_score

s.set_score(99);
print(s.score); #99

s2.set_score(100);
print(s2.score); #100

#### __slots__
#### 用__slots__限制该class实例可以添加的属性
class Teacher(object):
    __slots__ = ('name','age') # 用tuple定义允许绑定的属性名称
t = Teacher();
t.name = 'David';
t.age = 27;
#t.score = 99; #'Teacher' object has no attribute 'score'
print(t.name,t.age); #David 27