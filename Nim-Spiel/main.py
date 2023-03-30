import random


matches = 31
player_matches = 0
difficulty = None
round = 1
winner = None

def setDifficulty() -> str:
    difficulties = ['Easy', 'Normal']

    if len(difficulties) == 1:
        return difficulties[0]
    
    print('On which difficulty do you want to play?')
    for diff in difficulties:
        print(' •', diff)
    while True:
        diff = input('Difficulty Mode: ')
        if diff not in difficulties:
            print('Please enter a valid option.')
        else:
            return diff
        
def takeMatches(num: int) -> None:
    global matches

    if num > matches:
        num = matches
    matches -= num
        
def printMatches() -> None:
    global matches
    print(f'\n{matches} Matches are left.')
        
def computerTurn() -> None:
    global matches
    global player_matches
    global round
    global winner

    printMatches()

    if round == 1:
        num = 2
    else:
        num = 7 - player_matches 

    takeMatches(num)
    print(f'Computer took {num} matches.')

    if matches == 0:
        winner = 'Player'

def playerTurn() -> None:
    global matches
    global player_matches
    global winner

    if matches == 0: return

    printMatches()
    print('\nHow many matches do you want to take? (1-6)')
    while True:
        try:
            player_matches = int(input('Number of Matches: '))
        except ValueError:
            print('\n! Only Numbers allowed !\n')
        else:
            if 0 >= player_matches or player_matches > 6:
                print('\n! Enter number between 1 and 6 !\n')
                continue
            
            takeMatches(player_matches)
            if matches == 0:
                winner = 'Computer'
            break


def main() -> None:
    global matches
    global round

    while matches > 0:
        computerTurn()
        playerTurn()
        round += 1

    print('\nAll matches are taken.')
    print('Winner is:', winner)

    
if __name__ == '__main__':
    main()