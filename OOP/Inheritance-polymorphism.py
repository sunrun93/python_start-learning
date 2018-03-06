#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...');

class Dog(Animal):
    pass;

class Cat(Animal):
    pass;

D = Dog();
D.run();
C = Cat();
C.run();

print(isinstance(D,Dog));
print(isinstance(D,Animal));

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog());