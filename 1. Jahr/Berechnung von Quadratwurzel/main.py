from prettytable import PrettyTable


a_laenge = 26
b_laenge = 1
mittelwert = (a_laenge + b_laenge) / 2
abweichung = a_laenge - b_laenge
list_index: int = 0

a_list: list = [a_laenge]
b_list: list = [b_laenge]
mittelwert_list: list = [mittelwert]
abweichung_list: list = [abweichung]

table = PrettyTable()
table.field_names = ['', 'Länge A', 'Länge B', 'Mittelwert', 'Abweichung']


def main() -> None:
    global list_index

    while abweichung_list[list_index] > 0.1:
        if abweichung_list[list_index] < 0.1:
            break
        if len(a_list) != 1:
            list_index += 1
        a_list.append(round(mittelwert_list[list_index], 2))
        b_list.append(round(a_list[0] / a_list[list_index+1], 2))
        mittelwert_list.append(round((a_list[list_index+1] + b_list[list_index+1]) / 2, 2))
        abweichung_list.append(round(a_list[list_index+1] - b_list[list_index+1], 2))

    for i, (la, lb, m, ab) in enumerate(zip(a_list, b_list, mittelwert_list, abweichung_list), 1):
        table.add_row([i, la, lb, m, ab])
    print(table)

if __name__ == '__main__':
    main()