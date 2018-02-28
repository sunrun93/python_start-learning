
def is_prime(n):  
    if n == 1:  
        return False  
    for i in range(2, n//2 + 1):  
        if n % i == 0:  
            return False  
    return True  
L1 = filter(is_prime, range(1, 101));
print(list(L1)); 