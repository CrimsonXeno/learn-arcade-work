class Room:

    def __init__(self, description, north, east, south, west):

        self.description = ""
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0


def main():

    room_list = []

    room = Room("You are in the entrance hallway of the Connor's house",
                 None,
                 "1",
                 "3",
                 "5")
    room_list.append(0)

    room = Room("You have entered the Kitchen",
                None,
                None,
                "2",
                "0")
    room_list.append(1)

    room = Room("You have entered the Living Room",
                 None,
                 "0",
                 None,
                 None)
    room_list.append(5)

    room = Room("You have enter the Dining Room",
                "1",
                None,
                None,
                "3")
    room_list.append(2)

    room = Room("You are in the backend of the hall",
                "0",
                "2",
                "6",
                "4")
    room_list.append(3)

    room = Room("You are in the Bedroom",
                None,
                "3",
                None,
                None)
    room_list.append(4)

    room = Room("You have gone outside to the porch",
                "3",
                None,
                None,
                None)
    room_list.append(6)

    current_room = 0

    print(room_list)
main()