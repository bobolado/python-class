class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = []

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print("You moved to", self.current_room.name)
            self.describe_current_room()
        else:
            print("You can't go that way.")

    def describe_current_room(self):
        print(self.current_room.description)
        if self.current_room.items:
            print("You see the following items in the room:")
            for item in self.current_room.items:
                print("-", item)

    def take_item(self, item_name):
        for item in self.current_room.items:
            if item == item_name:
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print("You took", item)
                return
        print("There is no such item in the room.")

def main():
    # Define rooms
    kitchen = Room("Kitchen", "You are in a large kitchen. There is a table in the center.")
    living_room = Room("Living Room", "You are in a cozy living room. A fireplace crackles softly.")
    bedroom = Room("Bedroom", "You are in a comfortable bedroom. The bed looks inviting.")

    # Add exits between rooms
    kitchen.add_exit("north", living_room)
    living_room.add_exit("south", kitchen)
    living_room.add_exit("east", bedroom)
    bedroom.add_exit("west", living_room)

    # Add items to rooms
    kitchen.add_item("knife")
    living_room.add_item("book")
    bedroom.add_item("lamp")

    # Initialize player
    player = Player(kitchen)
    player.describe_current_room()

    # Game loop
    while True:
        command = input("What do you want to do? (Type 'help' for available commands): ").lower()

        if command == "quit":
            print("Quitting the game. Goodbye!")
            break
        elif command == "help":
            print("Available commands:")
            print("- move <direction>: Move to a different room (e.g., 'move north')")
            print("- take <item>: Take an item from the current room (e.g., 'take knife')")
            print("- inventory: View your inventory")
            print("- quit: Quit the game")
        elif command.startswith("move "):
            direction = command.split(" ")[1]
            player.move(direction)
        elif command.startswith("take "):
            item_name = command.split(" ")[1]
            player.take_item(item_name)
        elif command == "inventory":
            print("Inventory:", player.inventory)
        else:
            print("Invalid command. Type 'help' for available commands.")

if __name__ == "__main__":
    main()
