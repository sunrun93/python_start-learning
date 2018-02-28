from functools import reduce;
def prod_fun(l):
    def mul_fun(x,y):
        return x*y;
    return reduce(mul_fun,l);

print(prod_fun([1,2,3,4]));
