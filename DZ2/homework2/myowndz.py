import random


def check_field(field):
    count = 0
    x_row = 0
    x_index = field.index('x')
    if x_index in range(4):
        x_row = 1
    elif x_index in range(4, 8):
        x_row = 2
    elif x_index in range(8, 12):
        x_row = 3
    elif x_index in range(12, 16):
        x_row = 4
    for i in range(len(field)):
        if i == x_index:
            continue
        for j in range(i + 1, len(field)):
            if j != x_index:
                if field[i] > field[j]:
                    count += 1
    if (count + x_row) % 2 == 0:
        return False
    return True


def make_field(n):  # Формирование поля
    field = [i for i in range(1, n**2)]
    field.append('x')
    random.shuffle(field)
    return field


def show_field(field, n):  # Вывод поля
    output_field = ''
    for i in range(n):
        a = field[i*n:i*n + n]
        output_field += '|'
        for j in range(n):
            output_field += f' {str(a[j]).ljust(3)} |'
        output_field += '\n'
    print(output_field)


def check_final(field):  # Проверка окончания игры
    count = 0
    for i in range(len(field) - 1):
        if field[i] + 1 == field[i + 1]:
            count += 1
    if count == 14:
        show_field(field, 4)
        print('You win!')
        return True
    return False


MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1
}

#  Проверяем поле на решаемость
count_of_moves = 0
b = make_field(4)
while check_field(b):
    b = make_field(4)
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'x']

while True:
    try:
        show_field(b, 4)
        x_index = b.index('x')
        move = input('Передвигаться по полю: w - вверх, s - вниз, a - влево, d - вправо: ')
        if move.lower() in MOVES.keys():
            new_index = x_index + MOVES[move]
            if new_index not in range(16) \
                    or x_index in [3, 7, 11] and move.lower() == 'd' \
                    or x_index in [4, 8, 12] and move.lower() == 'a':
                print('Вы вышли за рамки дозволенного, Сэр!')
                continue
            b[x_index], b[new_index] = b[new_index], b[x_index]
            count_of_moves += 1
            if b.index('x') == 15:
                if check_final(b):
                    print(f'Количество ходов: {count_of_moves}')
                    break
        else:
            print('ONLY WASD!')
    except KeyboardInterrupt:
        print('Manual exit. Bye!')
        break
