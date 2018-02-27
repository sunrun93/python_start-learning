# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

def name_utility(l):
    def list_capitalize(s):
        return s.capitalize();
    return map(list_capitalize,l);

name = name_utility(['adam', 'LISA', 'barT']);

print(list(name));

    