# Python内置的sorted()函数就可以对list进行排序
L1 = sorted([9,6,7,4,8]); #[4, 6, 7, 8, 9]
print(L1);

# sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序
# 通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1

def reversed_sort(x,y):
    if x<y:
        return 1;
    if x>y:
        return -1;
    return 0;
