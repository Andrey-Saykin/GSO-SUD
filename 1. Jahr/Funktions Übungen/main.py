
def calculate(operation: str, *numbers: int) -> int:
    if operation == '+':
        return sum(numbers)
    elif operation == '-':
        sub = numbers[0]
        for number in numbers[1:]:
            sub -= number
        return sub
    elif operation == '*':
        total = 1
        for number in numbers:
            total *= number
        return total
    elif operation == '/':
        total = numbers[0]
        for number in numbers[1:]:
            total /= number
        return total
    else:
        print("Couldn't find operator.")

def caeser(char: str, shift: int) -> str:
    if not char.isalpha() or len(char) != 1:
        return char

    char_int = ord(char.upper())
    new_char = chr(char_int+shift)
    return new_char

def isPalindrom(string: str) -> bool:
    string = string.lower()
    return string == string[::-1]

def menu():
    repeat = True
    options = ('calculation', 'caeser', 'palindrom')
    while repeat:
        print('Choose an option.')
        for i, option in enumerate(options):
            print(f'{i} • {option}')
        choice = input('Your Choice: ')
        if choice == '0':
            operator = input('operator (+-*/): ')
            numbers = input('numbers: ')
            result = calculate(operator, *[int(num) for num in numbers.split()])
            print(result)

        elif choice == '1':
            char = input('character: ')
            try:
                shift = int(input('shift: '))
            except ValueError:
                print(ValueError)
            else:
                result = caeser(char, shift)
                print(result)

        elif choice == '2':
            string = input('word: ')
            result = isPalindrom(string)
            print(result)

        else:
            print('Given option not found.')

        answer = ''
        while answer != 'W' and answer != 'Q':
            answer = input('Do you want to continue? (W/Q)').upper()
            if answer == 'Q':
               repeat = False
            elif answer != 'W':
                print('invalid answer') 

if __name__ == '__main__':
    menu()