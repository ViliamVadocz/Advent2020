from enum import Enum
from copy import deepcopy

class Seat(Enum):
    FLOOR = 0
    FREE = 1
    OCCUPIED = 2

def parse_seat(char):
    if char == "L":
        return Seat.FREE
    elif char == ".":
        return Seat.FLOOR
    else:
        assert char == "#"
        return Seat.OCCUPIED

# part 1
def rule1(x, y, room):
    count = 0
    for i, ii in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        try:
            if y + i < 0 or x + ii < 0:
                continue
            if room[y + i][x + ii] == Seat.OCCUPIED:
                count += 1
        except IndexError:
            pass
    if room[y][x] == Seat.OCCUPIED and count >= 4:
        return Seat.FREE
    elif room[y][x] == Seat.FREE and count == 0:
        return Seat.OCCUPIED
    else:
        return room[y][x]

# part 2
def rule2(x, y, room):
    count = 0
    for i, ii in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
        try:
            # scan in each direction until seat is not floor
            steps = 1
            while True:
                row = y + i * steps
                col = x + ii * steps
                if row < 0 or col < 0:
                    break
                if room[row][col] == Seat.FLOOR:
                    steps += 1
                else:
                    if room[row][col] == Seat.OCCUPIED:
                        count += 1
                    break
        except IndexError:
            pass
    if room[y][x] == Seat.OCCUPIED and count >= 5:
        return Seat.FREE
    elif room[y][x] == Seat.FREE and count == 0:
        return Seat.OCCUPIED
    else:
        return room[y][x]

def step(room):
    return [[rule2(x, y, room) for x in range(len(room[0]))] for y in range(len(room))]

with open("input.txt", "r") as file:
    room = [[parse_seat(char) for char in row] for row in file.read().splitlines()]

def get_symbol(seat):
    if seat == Seat.OCCUPIED:
        return "#"
    elif seat == Seat.FREE:
        return "L"
    else:
        assert seat == Seat.FLOOR
        return "."

def print_room(room):
    print("\n".join("".join(get_symbol(seat) for seat in row) for row in room))
    print()

prev = deepcopy(room)
current = step(prev)

# print_room(prev)
# print_room(current)

while prev != current:
    prev = deepcopy(current)
    current = step(current)
    # print_room(current)

print(sum(sum(seat == Seat.OCCUPIED for seat in row) for row in current))
