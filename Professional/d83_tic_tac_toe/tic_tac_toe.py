table = list(range(1, 10))
turns = 0
WINNING_POSITIONS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def mark(spot, symbol) -> int:
    """
    Returns: - -1 if spot is already taken
    - 0 if the game can go on
    - 1 if X has won
    - 2 if O has won"""
    # Same spot overwrite prevention
    if type(table[spot]) == str:
        return -1

    table[spot] = symbol

    # Check winner
    indexes = []
    if turns % 2 == 0:
        for i, symbol in enumerate(table):
            if symbol == 'X':
                indexes.append(i)

        indexes = list(map(lambda x: x+1, indexes))
        for position in WINNING_POSITIONS:
            if all([position[i] in indexes for i in range(3)]):
                return 1

    elif turns % 2 == 1:
        for i, symbol in enumerate(table):
            if symbol == 'O':
                indexes.append(i)

        indexes = list(map(lambda x: x + 1, indexes))
        for position in WINNING_POSITIONS:
            if all([position[i] in indexes for i in range(3)]):
                return 2

    return 0


while True:
    choice = input(f'''
     {table[0]} | {table[1]} | {table[2]} 
    -----------
     {table[3]} | {table[4]} | {table[5]} 
    -----------
     {table[6]} | {table[7]} | {table[8]} 
       
    Player{turns % 2 + 1}, where? ''')

    # Input check
    try:
        choice = int(choice.strip())

    except ValueError:
        print('    FAIL\n')
        continue

    if not 0 < choice < 10:
        print('    FAIL\n')
        continue

    if turns % 2 == 0:
        response = mark(spot=choice - 1, symbol='X')

    elif turns % 2 == 1:
        response = mark(spot=choice - 1, symbol='O')

    else:
        response = -1

    if response == -1:
        print('    fail\n')
    elif response == 1:
        print('    PLAYER1 WINS')
        break
    elif response == 2:
        print('    PLAYER2 WINS')
        break

    turns += 1
