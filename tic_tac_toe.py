import os

i, x, o = 1, 'X', 'O'
def game():
    turn = 1
    gamesPlayed = 0
    pf = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    def playField():
        print(f'\t+===+===+===+')
        print(f'\t| {pf[0][0]} | {pf[0][1]} | {pf[0][2]} |')
        print(f'\t+===+===+===+')
        print(f'\t| {pf[1][0]} | {pf[1][1]} | {pf[1][2]} |')
        print(f'\t+===+===+===+')
        print(f'\t| {pf[2][0]} | {pf[2][1]} | {pf[2][2]} |')
        print(f'\t+===+===+===+')
    def inputCoords():
        global fC, sC, stringfC, stringsC, list
        list = ['1', '2', '3']
        stringfC = (input('Type the first (x) coordinate: '))
        stringsC = (input('Type the second (y) coordinate: '))
        if((stringfC in list) and (stringsC in list)):
            fC = int(stringfC)
            sC = int(stringsC)
        else:
            print('Out of range coordinate, try again')
            inputCoords()
    def reset():
        pf[0][0], pf[0][1], pf[0][2], pf[1][0], pf[1][1], pf[1][2], pf[2][0], \
        pf[2][1], pf[0][2] = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
        os.system('pause')

    while(1):
            inputCoords()
            if(((3 >= fC) >= 1) and (3 >= sC) >= 1):
                if(pf[fC - 1][sC - 1] == ' '):
                    pf[fC - 1][sC - 1] = 'X' if(turn % 2 == 1) else 'O'
                    playField()
                    turn += 1
                else:
                    print('Spot already taken')
            else:
                print('Out of range coordinate, try again')
            
            # Tie
            if(turn > 9):
                gamesPlayed += 1
                print(f'\nIt\'s a tie!\n{gamesPlayed} game(s) played\n')
                turn = 1
                reset()

            # Horizontal X
            elif((pf[0][0] == 'X' and pf[0][1] == 'X' and pf[0][2] == 'X') or\
                (pf[1][0] == 'X' and pf[1][1] == 'X' and pf[1][2] == 'X') or\
                (pf[2][0] == 'X' and pf[2][1] == 'X' and pf[2][2] == 'X') or\
            # Vertical X
                (pf[0][0] == 'X' and pf[1][0] == 'X' and pf[2][0] == 'X') or\
                (pf[0][1] == 'X' and pf[1][1] == 'X' and pf[2][1] == 'X') or\
                (pf[0][2] == 'X' and pf[1][2] == 'X' and pf[2][2] == 'X') or\
            # Diagonal X
                (pf[0][0] == 'X' and pf[1][1] == 'X' and pf[2][2] == 'X') or\
                (pf[0][2] == 'X' and pf[1][1] == 'X' and pf[2][0] == 'X')):
                gamesPlayed += 1
                print(f'\nX wins!\n{gamesPlayed} game(s) played\n')
                turn = 1
                reset()

            # Horizontal O
            elif((pf[0][0] == 'O' and pf[0][1] == 'O' and pf[0][2] == 'O') or\
                (pf[1][0] == 'O' and pf[1][1] == 'O' and pf[1][2] == 'O') or\
                (pf[2][0] == 'O' and pf[2][1] == 'O' and pf[2][2] == 'O') or\
            # Vertical O
                (pf[0][0] == 'O' and pf[1][0] == 'O' and pf[2][0] == 'O') or\
                (pf[0][1] == 'O' and pf[1][1] == 'O' and pf[2][1] == 'O') or\
                (pf[0][2] == 'O' and pf[1][2] == 'O' and pf[2][2] == 'O') or\
            # Diagonal O
                (pf[0][0] == 'O' and pf[1][1] == 'O' and pf[2][2] == 'O') or\
                (pf[0][2] == 'O' and pf[1][1] == 'O' and pf[2][0] == 'O')):
                gamesPlayed += 1
                print(f'\nO wins!\n{gamesPlayed} game(s) played\n')
                turn = 1
                reset()

print('Welcome to Tic Tac Toe (X starts first)\n')
game()