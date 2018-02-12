def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:', age,'other:', kw);

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456);

#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job);

#person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456); TypeError
person('Jack', 24, city='Beijing', job='Engineer'); #Jack 24 Beijing Engineer, 命名关键字参数必须传入参数名

def person_1(name,age,*args,city,job):
    print(name,age,args,city,job);

#person_1('Jack',24,'Beijing','developer'); #TypeError: person_1() missing 2 required keyword-only arguments: 'city' and 'job'
person_1('Jack',24,city='Beijing',job='developer'); #Jack 24 () Beijing developer

