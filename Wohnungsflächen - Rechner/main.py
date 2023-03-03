from helper import ni, msg, units, shapes
from room import Room, set_name, set_living_space, set_shape, set_length, set_width

def setUnit() -> str:
    """
    User defines the used unit to show in length and width of rooms
    """
    while True:
        print('\nWhich unit do you want?')
        for unit in units:
            print(f'  • {unit}')

        answer = input()
        if answer in unit:
            return answer
        else:
            print(msg[0])

def room_number() -> int:
    """
    User defines the number of rooms
    """
    while True:
        print('\nEnter the number of rooms to add.')
        try: 
            num: int = int(input())
        except ValueError:
            print(msg[1])
        else:
            if num == 0:
                print(msg[2])
            elif num > 20:
                print('More than 20 rooms are not allowed!')
            else:
                return (num+1)

def main() -> None:
    """
    Runs the main program
    """
    rooms: list = [] 

    unit = setUnit()

    for i in range(1, room_number(), 1):
        room = Room(
            set_name(),
            set_living_space(),
            set_shape()
        )

        room.length = set_length(room.shape)
        room.width = set_width(room.shape)

        if isinstance(room.length, list) and isinstance(room.width, list):
            for length, width in room.length, room.width:
                room.area += length * width
        elif room.length is not None and room.width is not None:
            room.area = room.length * room.width

        rooms.append(room)
    
    print('')
    print('Overview'.center(30, '-'))
    
    total_space: float = 0.0
    living_space: float = 0.0

    for room in rooms:
        room.overview(unit)
        total_space += room.area
        living_space += room.area if room.living_space else 0

    print(f'\nTotal space: {total_space}{unit}²')
    print(f'Living space: {living_space}{unit}²')


if __name__ == '__main__':
    main()