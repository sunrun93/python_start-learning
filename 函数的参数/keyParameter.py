#关键字参数 用**
def person(name,age,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('Michael',30) #name: Michael age: 30 other: {}
person('Bob', 35, city='Beijing') #name: Bob age: 35 other: {'city': 'Beijing'}

#可先组装一个dict,然后将dict做可变参数传进去
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city':'Beijing','job':'Engineer'}
person('Daisy',25,**extra); #name: Daisy age: 25 other: {'city': 'Beijing', 'job': 'Engineer'}