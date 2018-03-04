#python 通过class关键字定义类，()中表示继承哪一个类

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score));
    def print_grade(self):
        if self.score<60:
            return 'C';
        elif self.score<80:
            return 'B';
        else:
            return 'A';

#创建实例是通过类名+()实现， 实例化nancy的类
nancy = Student('Nancy',100);
nancy.print_score();
print(nancy.print_grade());

#在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数


