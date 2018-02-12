#列表元素可以按照某种算法推算出来，那可以在循环的过程中不断推算出后续的元素
#这样就不必创建完整的list，从而节省大量的空间。

L = [x * x for x in range(10)];
print(L); #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(10));
print(g); #<generator object <genexpr> at 0x000002086AEC6ED0>

print(next(g));