board = [[' ' for i in range(3)] for j in range(3)]
valid_range = list(range(1, 10))
players = ['', 'Player 1', 'Player 2']
quit = False
symbol = ''
symbols = ['']
player1_pos = []
player2_pos = []

def user_input(player):
    global quit, symbol, valid_range
    inp = ''
    while valid_range:
        if not symbol:
            symbol = input('Player 1. Enter your symbol (X or O) : ')
            if symbol.upper() not in ['X', 'O']:
                print('Invalid symbol !!!')
                symbol = ''
                continue
            set_symbols()
        inp = input(f'{player}. Enter a number from {valid_range} OR Enter Q to Quit Game : ')
        if inp.isdigit() and int(inp) in valid_range:
            player *= -1
            valid_range.remove(int(inp))
            return int(inp)
        elif inp.upper() == 'Q':
            quit = True
            break
        print('Invalid input !!!')
    else:
        print('Game Over !!!!!!!!')
        exit()

def set_symbols():
    global symbols
    symbols.append(symbol.upper())
    symbols.append('O' if symbols[1] == 'X' else 'X')

def display_board():
    for i in range(3):
        print('\t     |     |     ')
        print(f'\t  {board[i][0]}  |  {board[i][1]}  |  {board[i][2]}  ')
        if i < 2:
            print('\t_____|_____|_____')
        else:
            print('\t     |     |     ')
    return ''

def update_board(inp, symbol):
    if inp < 4:
        board[0][inp - 1] = symbol
    elif inp < 7:
        board[1][inp - 4] = symbol
    else:
        board[2][inp - 7] = symbol

def check_win():
    win_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for comb in win_comb:
        if all(pos in player1_pos for pos in comb):
            print('Player 1 Wins !!!!!')
            return True
        elif all(pos in player2_pos for pos in comb):
            print('Player 2 Wins !!!!!')
            return True
    return False

def main():
    sign = 1
    while not quit and not check_win():
        display_board()
        inp = user_input(players[sign])
        if type(inp) == int:
            update_board(inp, symbols[sign])
            if sign == 1:
                player1_pos.append(inp)
            else:
                player2_pos.append(inp)

        sign *= -1
    else:
        print('Quitting !!!!!!!!!' if quit else display_board())


main()
