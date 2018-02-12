#  定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('End')
    return L

print(add_end());#['End']
print(add_end());#['End','End']
print(add_end());#['End','End','End']

def add_end_2(L=None):
    if L is None:
        L = []
        L.append('End')
        return L

print(add_end_2());#['End']
print(add_end_2());#['End']
print(add_end_2());#['End']
    
