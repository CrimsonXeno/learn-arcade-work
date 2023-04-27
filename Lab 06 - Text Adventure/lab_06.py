class Room:


    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    current_room = 0
    next_room = 0
    done = False

    room = Room("You are in the entrance of a house, there is a path to your west, east, and south.", None, 1, 3, 5)
    room_list.append(room)

    room = Room("You have entered the Kitchen, there is a path to the south and west.", None, None, 0, 2)
    room_list.append(room)

    room = Room("You have entered the living room, there is a path to your east.", None, 0, None, None)
    room_list.append(room)

    room = Room("You have enter the Dining Room, there is a path to your north and west.", 1, None, None, 3)
    room_list.append(room)

    room = Room("You are in the backend of the hall, there is a path in all directions.", 0, 2, 6, 4)
    room_list.append(room)

    room = Room("You are in the Bedroom,there is path to east.", None, 3, None, None)
    room_list.append(room)

    room = Room("You have gone outside to the porch, there is a path to your north.", 3, None, None, None)
    room_list.append(room)

  # print(room_list[0])
    while not done:
        print(room_list[current_room].description)
        print("\n")
        direction = input("Which path do you choose? (n e s w)").lower()
        print("\n")
        if direction.lower()[0] == 'n':
            next_room = room_list[current_room].north

        elif direction.lower()[0] == 'e':
            next_room = room_list[current_room].east

        elif direction.lower()[0] == 's':
            next_room = room_list[current_room].south

        elif direction.lower()[0] == 'w':
            next_room = room_list[current_room].west

        else:
            print("Please pick a valid direction.")
            print("\n")
            continue

        if next_room == None:
            print("You can't go that way!")
            print("\n")
            continue

        current_room = next_room

main()