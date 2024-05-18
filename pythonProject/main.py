print('welcome to TIC TAC TOE')
pos_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def display_board():
    result_board = ((f'{pos_num[0]}    |   {pos_num[1]}    |   {pos_num[2]}\n' + f'----------------------\n' +
              f'{pos_num[3]}    |   {pos_num[4]}    |   {pos_num[5]}\n') + f'----------------------\n' +
              f'{pos_num[6]}    |   {pos_num[7]}    |   {pos_num[8]}\n')
    print(result_board)

display_board()

game = True
player1_turn = True

player_1 = player_2 = []

while game:
    try:
        if player1_turn:
            n = int(input('Enter number position you want to put "X" :'))
            if n in player_2:
                print('number position already filled by player 2')
            else:
                player_1.append(n)
                pos_num[n-1] = 'X'
                display_board()
                player1_turn = False

        else:
            n = int(input('Enter number position you want to put "0" :'))
            if n in player_1:
                print('number position already filled by player 1')
            else:
                player_2.append(n)
                pos_num[n - 1] = '0'

                player1_turn = True
                display_board()
    except ValueError:
        print('Not a  valid number')
        game = False
    except IndexError:
        print('Number must be between 1 to 9')
        game = False

    if pos_num[0]==pos_num[1]==pos_num[2] or pos_num[3]==pos_num[4]==pos_num[5] or pos_num[6]==pos_num[7]==pos_num[8] or pos_num[0]==pos_num[3]==pos_num[6] or pos_num[1]==pos_num[4]==pos_num[7] or pos_num[2]==pos_num[5]==pos_num[8] or pos_num[0]==pos_num[4]==pos_num[8] or pos_num[2]==pos_num[4]==pos_num[6]:
        if player1_turn:
            print("Player 2 Won the game")
            game = False
            player1_turn = False
        else:
            print("Player 1 Won the game")
            game = False
            player1_turn = False
    if len(player_1) == 9:
        print("It is draw")
        game = False
        player1_turn = False