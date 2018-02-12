#必选参数在前，默认参数在后
def power(x, n=2):  
      s=1  
      while n>0:  
            n=n-1  
            s=s*x  
      return s  

print(power(5));#25
print(power(5,2));#25
print(power(5,5));#3125

def enroll(name,gender,age=6,city='Beijing'):
    print('name:',name)
    print('gender:',gender)
    print('age:',age)
    print('city',city)

enroll('Nancy','E',25,"shanghai");
enroll('Sarah','F');
enroll('Bob','M',7);
enroll('Bob','M',city='Guangzhou');