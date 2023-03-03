from helper import msg, shapes

class Room():
    def __init__(self, name, living_space, shape):
        self.name: str = name
        self.living_space: bool = living_space
        self.shape: str = shape
        self.length: float = 0.0
        self.width: float = 0.0
        self.area: float = 0.0
        self.slope: bool = False

    def __str__(self) -> str:
        return self.name

    def overview(self, unit) -> None:
        """
        Creates an overview with attributes of room
        """
        print('\n',str(self).center(20, '-'))
        print(f'  • Shape: {self.shape}')
        if self.shape == shapes[1]:
            for idx, (length, width) in enumerate((self.length, self.width), start=1):
                print(f'  • {idx}. Length & Width: {length}{unit} • {width}{unit}')
        else:
            print(f'  • Length & Width: {self.length}{unit} • {self.width}{unit}')
        space = f'  • Space: {self.area}{unit}²' if not self.living_space else f'  • (Living) Space: {self.area}{unit}²'
        print(space)


def set_name() -> str:
    """
    User defines a name for room
    """
    print('\nEnter a name for the room. (Do not use the same name multiple times to differentiate between the rooms)')
    while True:
        name = input().strip()
        if name == '' or name is None:
            print(msg[3])
        else:
            return name

def set_shape() -> str:
    """
    User defines the shape of room
    """
    while True:
        print('\nSelect the shape of your room:')
        for shape in shapes:
            print(f'  • {shape} - enter {shapes.index(shape)}')
        try:
            answer = int(input())
        except ValueError:
            print(msg[1])
        else:
            try:
                return shapes[answer]
            except IndexError:
                print(msg[0])
        
def set_length(shape: str) -> float|list:
    """
    User defines the length(s) of room
    """
    if shape not in shapes:
        print('Canceled setting length for room because shape not exists.')
        return
    
    if shape == shapes[0]:
        while True:
            print('\nEnter length of the room')
            try:
                length = float(input())
            except ValueError:
                print(msg[1])
            else:
                if length == 0:
                    print(msg[2])
                else:
                    return length
    elif shape == shapes[1]:
        length_list = []
        while len(length_list) < 2:
            print(f'\nEnter {len(length_list)+1}. length of the room')
            try:
                length = float(input())
            except ValueError:
                print(msg[1])
            else:
                if length == 0:
                    print(msg[2])
                else:
                    length_list.append(length)
            if len(length_list) == 2:
                return length_list
    

def set_width(shape: str) -> float|list:
    """
    User defines width(s) of room
    """
    if shape not in shapes:
        print('Canceled setting width for room because shape not exists.')
        return
    
    if shape == shapes[0]:
        while True:
            print('\nEnter width of the room')
            try:
                width = float(input())
            except ValueError:
                print(msg[1])
            else:
                if width == 0:
                    print(msg[2])
                else:
                    return width
    elif shape == shapes[1]:
        width_list = []
        while len(width_list) < 2:
            print(f'\nEnter {len(width_list)+1}. width of the room')
            try:
                width = float(input())
            except ValueError:
                print(msg[1])
            else:
                if width == 0:
                    print(msg[2])
                else:
                    width_list.append(width)
            if len(width_list) == 2:
                return width_list
    

def set_living_space() -> bool:
    """
    User defines if room is living space or not
    """
    while True:
        print(f'\nShould this room add to total living sapce?')
        print(f' • Enter y for yes')
        print(f' • Enter any other key for no')
        answer: str = input().strip()
        if answer == 'y':
            return True
        else:
            return False