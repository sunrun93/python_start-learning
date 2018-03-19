from enum import Enum,unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'));
mon1 = Month.Jan;
print(mon1); #Month.Jan

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
#Jan => Month.Jan , 1
#Feb => Month.Feb , 2
#Mar => Month.Mar , 3
#Apr => Month.Apr , 4
#May => Month.May , 5
#Jun => Month.Jun , 6
#Jul => Month.Jul , 7
#Aug => Month.Aug , 8
#Sep => Month.Sep , 9
#Oct => Month.Oct , 10
#Nov => Month.Nov , 11
#Dec => Month.Dec , 12

@unique #用来检查是否有重复值
class Weekday(Enum):
    Sun = 0,
    Mon = 1,
    Tue = 2,
    wed = 3,
    Thu = 4,
    Fri = 5,
    Sat = 6

for name,member in Weekday.__members__.items():
    print(name,'=>',member)

#把Student的gender属性改造为枚举类型，可以避免使用字符串
Gender = Enum('Gender', ('Male','Female'));

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')