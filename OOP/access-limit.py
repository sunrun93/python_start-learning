#要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__, 表示将变量标为私有变量

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s: %s' %(self.__name,self.__score))

nancy = Student('Nancy',99);
nancy.print_score();

# print(nancy.__name); 
#AttributeError: 'Student' object has no attribute '__name'
#无法从外部访问实例变量.__name和实例变量.__score

#外部代码要获取name和score,给Student类添加get_score/get_Name方法
#外部代码要修改name和score,给Student类添加set_score/set_Name方法
class Student(object):
    ......
    def get_score(self, score):
        return self.score;
    def set_score(self,score):
        if 0<=score<=100:
            self.__score = score;

daisy = Student('Daisy',90);
print(daisy.get_score());

    
