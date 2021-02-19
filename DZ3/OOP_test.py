# class MoneyBox:
#     def __init__(self, count):
#         self.capacity = count
# # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#     # True, если можно добавить v монет, False иначе
#         if v < self.capacity:
#             return True
#         else:
#             return False
#
#     def add(self, v):
#         # положить v монет в копилку
#         if self.can_add(v):
#             self.capacity -= v
#         return self.capacity
#
#
# Box = MoneyBox(30)
# print(Box.add(5))
# print(Box.add(26))
# print(Box.add(15))
# print(Box.add(10))
# print(Box.add(1))

class Buffer:
    def __init__(self):# конструктор без аргументов
        self.lst = []
        self.counter = 0

    def add(self, *a):# добавить следующую часть последовательности
        for i in a:
            self.lst.append(i)
        if len(self.lst) >= 5:
            for i in range(len(self.lst) // 5):
                print(sum(self.lst[i*5:i*5+5]))
                self.counter += 1

    def get_current_part(self):
        self.lst = self.lst[self.counter * 5:self.counter * 5 + 5]
        self.counter = 0
        print(self.lst)
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены


#  a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
a = Buffer()
a.add(1, 2, 3)
a.get_current_part()
a.add(4, 5, 6, 7)
a.get_current_part()
a.add(1, 2)
a.get_current_part()
a.add(3)
a.get_current_part()
a.add(4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7)
a.get_current_part()
a.add(1)
a.get_current_part()
