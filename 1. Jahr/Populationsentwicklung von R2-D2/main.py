from prettytable import PrettyTable

young_list: list = [10]
adult_list: list = [10]
old_list: list = [10]

years: int = 0

def years_input() -> int:
    while True:
        print('Enter how much years you want to simulate?')
        try:
            years = int(input('Years: '))
        except ValueError:
            print('Please enter numbers.')
        else:
            return years
        
def new_year() -> None:
    young_list.append(0)
    adult_list.append(0)
    old_list.append(0)
        
def reproduction() -> None:
    year = len(young_list) - 2
    young_list[year+1] += adult_list[year] * 4 + old_list[year] * 2

def aging() -> None:
    year = len(young_list) - 2
    adult_bots = young_list[year] // 2
    old_bots = adult_list[year] // 3
    
    adult_list[year+1] += adult_bots
    old_list[year+1] += old_bots

def overview() -> None:
    table = PrettyTable()
    table.field_names = ['Year', 'Young R2D2', 'Adult R2D2', 'Old R2D2']
    for year, (young, adult, old) in enumerate(zip(young_list, adult_list, old_list)):
        table.add_row([year, young, adult, old])
    print(f'Here is a table of {years} simulated years:')
    print(table)
        
def main() -> None:
    print('\nWelcome to R2D2 population simulation.')
    global years
    years = years_input()
    for _ in range(0, years, 1):
        new_year()
        print(young_list, adult_list, old_list)
        reproduction()
        print(young_list, adult_list, old_list)
        aging()
        print(young_list, adult_list, old_list)
    overview()
        
if __name__ == '__main__':
    main()