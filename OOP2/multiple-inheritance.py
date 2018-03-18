#通过继承，子类就可以扩展父类的功能
class Animal(object):
    pass;

class Life(object):
    pass;

class Dog(Animal,Life): #Dog同时继承Animal类和Life类
    pass; #个子类就可以同时获得多个父类的所有功能。
    
#这种设计通常称之为MixIn。