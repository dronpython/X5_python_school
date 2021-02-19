# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This function is used to create a field at the very start of the game.

    :return: list with 16 randomly shuffled tiles,
        one of which is a empty space.
    """
    field = list(range(1, 16))
    field.append(EMPTY_MARK)
    while True:
        rows = {1: list(range(4)),
                2: list(range(4, 8)),
                3: list(range(8, 12)),
                4: list(range(12, 16))}
        random.shuffle(field)
        count = 0
        x_row = 0
        x_index = field.index(EMPTY_MARK)

        for key, value in rows.items():
            if x_index in value:
                x_row = key

        for i in range(len(field)):
            if i == x_index:
                continue
            for j in range(i + 1, len(field)):
                if j != x_index:
                    if field[i] > field[j]:
                        count += 1
        if (count + x_row) % 2 == 0:
            return field
    pass


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    output_field = ''
    for i in range(4):
        a = field[i * 4:i * 4 + 4]
        output_field += '|'
        for j in range(4):
            output_field += f' {str(a[j]).ljust(3)} |'
        output_field += '\n'
    print(output_field)
    pass


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    final_sate = list(range(1, 16))
    if field.index(EMPTY_MARK) == 15:
        if final_sate == field[0:15]:
            print('You win!')
            return True
    return False
    pass


def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    x_index = field.index(EMPTY_MARK)
    if key.lower() in MOVES.keys():
        new_index = x_index + MOVES[key]
        if new_index not in range(16) \
                or x_index in [3, 7, 11] and key.lower() == 'd' \
                or x_index in [4, 8, 12] and key.lower() == 'a':
            raise IndexError('Your move out of bound!')
        field[x_index], field[new_index] = field[new_index], field[x_index]
    else:
        raise IndexError('ONLY WASD!')
    return field
    pass


def handle_user_input():
    """
    Handles user input.

    List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right

    :return: <str> current move.
    """
    while True:
        user_input = input('Передвигаться по полю WASD: ')
        if user_input.lower() in MOVES.keys():
            return user_input.lower()
        print('ONLY WASD!')

    pass


def main():
    """
    The main function. It starts when the program is called.

    It also calls other functions.
    :return: None
    """
    count_of_moves = 0
    game_field = shuffle_field()
    # game_field = list(range(1, 16))
    # game_field.append('x')
    while True:
        try:
            print_field(game_field)
            user_move = handle_user_input()
            count_of_moves += 1
            try:
                game_field = perform_move(game_field, user_move)
            except IndexError:
                print('Out of bounds!')
            if game_field.index(EMPTY_MARK) == 15:
                if is_game_finished(game_field):
                    print(f'Count of moves: {count_of_moves}')
                    break
        except KeyboardInterrupt:
            print('Manual exit. Bye!')
            break

    pass


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do
    main()
