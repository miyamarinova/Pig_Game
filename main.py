import random

PLAYER_1_PTS = 0
PLAYER_2_PTS = 0
TURN_PTS = 0

def dice_num():
    min_num = 1
    max_num = 6
    dice = random.randint(min_num, max_num)
    return dice

def roll_dice(player):
    global TURN_PTS
    global PLAYER_2_PTS
    global PLAYER_1_PTS
    check_for_win(player)
    roll_or_hold = input('If you want to roll, write "y" and if you want to hold the points, write "h": ')

# If Player wants to roll the dice
    if roll_or_hold == "y":
        dice = dice_num()
        TURN_PTS += dice
        check_for_one(player, dice)
        roll_dice(player)

# If Player wants to hold the turn points and add them to his/her points
    elif roll_or_hold == 'h':
        if player == '1':
            PLAYER_1_PTS += TURN_PTS
            print(f'{PLAYER_1_PTS}')
            check_for_win(player)

            print(f'Player 1 Pts: {PLAYER_1_PTS}  ||  Player 2 Pts: {PLAYER_2_PTS}')
            print('-------------------------')
            print(f"--- It's Player 2 Turn ---")
            print('-------------------------')
            player = '2'
            TURN_PTS = 0
            roll_dice(player)

        if player == '2':
            PLAYER_2_PTS += TURN_PTS
            check_for_win(player)
            print(f'Player 1 Pts: {PLAYER_1_PTS}  ||  Player 2 Pts: {PLAYER_2_PTS}')
            print('-------------------------')
            print(f"--- It's Player 1 Turn ---")
            print('-------------------------')
            player = '1'
            TURN_PTS = 0
            roll_dice(player)

def check_for_one(player, dice):
    global TURN_PTS
    if dice == 1:
        TURN_PTS = 0
        if player == '1':
            print(f'Player {player} XXX Dice is 1 XXX  || Turn Points: 0  ||  Player 1 Pts: {PLAYER_1_PTS}  ||  Player 2 Pts: {PLAYER_2_PTS}')
            player = '2'
        elif player == '2':
            print(f'Player {player} XXX Dice is 1 XXX  || Turn Points: 0  ||  Player 1 Pts: {PLAYER_1_PTS}  ||  Player 2 Pts: {PLAYER_2_PTS}')
            player = '1'
        print(f"NOW IT'S PLAYER {player} TURN")
        roll_dice(player)
    else:
        print(f'Payer {player} Dice is: {dice}  ||  Turn Points: {TURN_PTS}  ||  Player 1 Pts: {PLAYER_1_PTS}  ||  Player 2 Pts: {PLAYER_2_PTS}')
        return
def check_for_win(player):
    if PLAYER_1_PTS >= 25:
        player_1_winner()
    if PLAYER_2_PTS >= 25:
        player_2_winner()
    else:
        return
def player_1_winner():
    print("--------------------------------------------------------")
    print(f'WE HAVE A WINNER: Player 1 with {PLAYER_1_PTS} points!')
    print("--------------------------------------------------------")
    quit()

def player_2_winner():
    print("--------------------------------------------------------")
    print(f'WE HAVE A WINNER: Player 2 with {PLAYER_2_PTS} points!')
    print("--------------------------------------------------------")
    quit()



def define_player():
    player = input(f'For Player 1, insert "1", for Player 2, insert "2": ')
    if player == '1':
        print("--- It's Player 1 Turn ---")
    if player == '2':
        print("--- It's Player 2 Turn ---")
    roll_dice(player)



print('*-*-*-*-*-*-*-*-*-*-')
print('      Pig Game')
print('*-*-*-*-*-*-*-*-*-*-')
define_player()
