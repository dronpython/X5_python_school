class Array:
    def __init__(self, *n):
        self.lst = []
        self.lst.extend(n)

    def index(self, value):
        if value in self.lst:
            return self.lst.index(value)
        else:
            return -1

    def append(self, value):
        return self.lst.append(value)

    def __add__(self, other):
        return Array(*self.lst, *other.lst)

    def __iter__(self):
        return iter(self.lst)

    def __len__(self):
        return self.lst.__len__()

# Tests:
# a = Array(1, 2)
# b = Array(3, 4)
# c = Array(1, 2, 3, 4)
# F = a + b + c
# print(F.lst)
# a.append(10)
# print(a.lst)
# print(len(a + b + c))
# print(a.index(3))
#
# for i in c:
#     print(i)

