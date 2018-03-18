#为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩

class Student(object):
    def get_score(self):
        return self._score;
    def set_score(self,value):
        if not isinstance(value,int):
             raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s1 = Student();
#s1.set_score(111.33);  #raise ValueError('score must be an integer!')
s1.set_score(60);
print(s1.get_score());#60

#Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student1(object):
    #把一个getter方法变成属性，只需要加上@property就可以了
    @property
    def score(self):
        return self._score;

    #@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s2 = Student1();
s2.score = 60;
print(s2.score);#60 将内部方法转化成属性调用

#不止一个property
class Student2(object):
    @property
    def birth(self):
        return self._birth;
    
    @birth.setter
    def birth(self,value):
        self._birth = value;
    
    @property
    def age(self):
        return 2018-self._birth;

s2 = Student2();
s2.birth=1993;
print(s2.age);#25

#利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
class Screen(object):
    @property
    def width(self):
        return self._width;

    @width.setter
    def width(self,value):
        self._width = value;

    @property
    def height(self):
        return self._height;

    @height.setter
    def height(self,value):
        self._height = value;
        
    @property
    def resolution(self):
        return self._width*self._height;

ss = Screen()
ss.width = 1024
ss.height = 768
print('resolution =', ss.resolution)
if ss.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
    



