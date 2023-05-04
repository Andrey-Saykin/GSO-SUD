
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
    options = ('calculation', 'caeser', 'palindrom')
    choice = input('Your Choice: ')
    if choice == '0':
        operator = input('operator: ')
        try:
            numbers = int(input('numbers: '))
        except ValueError:
            print(ValueError)
        else:
            calculate(operator, numbers)
    elif choice == '1':
        char = input('character: ')
        try:
            shift = int(input('shift: '))
        except ValueError:
            print(ValueError)
        else:
            caeser(char, shift)
    elif choice == '2':
        string = input('word: ')
        isPalindrom(string)
    else:
        print('Given option not found.')

if __name__ == '__main__':
    menu()