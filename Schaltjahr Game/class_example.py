import random


class Player():
    def __init__(self, name):
           self.name = name
           self.score = 0

    def __str__(self) -> str:
        return (f'{self.name}, {self.score}')

    def show(self):
        print(f'{self.name} has achieved a score of {self.score}.')
        

class Schaltjahr():
    def __init__(self):
        self.jahr = random.randint(1900,2050)
        self.schaltjahr = True if (self.jahr % 4 == 0) and (self.jahr % 100 != 0) or (self.jahr % 400 == 0) else False


if __name__ == '__main__':

    again_str = ''

    while True:

        if again_str == 's' or again_str == '':
            print('Enter your name.')
            player = Player(input())

        while True:
            schaltjahr = Schaltjahr()

            if not schaltjahr.schaltjahr:
                print(f'{schaltjahr.jahr} is not a "Schaltjahr"')
                player.show()
                break
            else:
                print(f'{schaltjahr.jahr} is a "Schaltjahr"')
            
            player.score += 1

        print('\nDo you want to play again?')
        print('• Press "a" to play again with the same name')
        print('• Press "s" to play again with another name')
        print('• Press any other key to stop')

        again_str = input()

        if again_str != 'a' and again_str != 's':
            break



