from prettytable import PrettyTable


laenge_a: int = 25
laenge_b: int = 1
mittelwert: int = 13
abweichung: int = 24

a_list: list = [25]
b_list: list = [1]
mittelwert_list: list = [13]
abweichung_list: list = [24]

table = PrettyTable()
table.field_names = ['', 'Länge A', 'Länge B', 'Mittelwert', 'Abweichung']


def main() -> None:
    for i, (la, lb, m, ab) in enumerate(zip(a_list, b_list, mittelwert_list, abweichung_list), 1):
        table.add_row([i, la, lb, m, ab])
    print(table)

if __name__ == '__main__':
    main()