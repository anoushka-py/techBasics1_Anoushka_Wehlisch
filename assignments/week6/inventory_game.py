# ============================================================
# HAUNTED HOUSE ESCAPE GAME
# Assignment 6: Inventory Management System
# ============================================================

MAX_INVENTORY = 5

# Player inventory (list of dictionaries)
inventory = []

# All rooms in the game (list of dictionaries)
# Each room has a name, description, and list of items
rooms = [
    {
        "name": "Bedroom",
        "description": "A dusty bedroom with a broken mirror. It smells old.",
        "items": [
            {"name": "torch", "type": "tool", "uses": 3,
             "description": "A flickering torch. Lights up dark rooms."},
            {"name": "bandage", "type": "healing", "uses": 1,
             "description": "A old bandage. Restores a little health."}
        ]
    },
    {
        "name": "Kitchen",
        "description": "A dark kitchen. Something moved in the corner.",
        "items": [
            {"name": "apple", "type": "food", "uses": 1,
             "description": "A surprisingly fresh apple. Restores health."},
            {"name": "knife", "type": "weapon", "uses": 2,
             "description": "A sharp kitchen knife. Useful against ghosts."},
            {"name": "key", "type": "tool", "uses": 1,
             "description": "A rusty key. It might open something important..."}
        ]
    },
    {
        "name": "Living Room",
        "description": "A grand living room. The front door is here — but it is locked.",
        "items": [
            {"name": "potion", "type": "healing", "uses": 1,
             "description": "A glowing potion. Fully restores health."},
            {"name": "map", "type": "tool", "uses": 1,
             "description": "A map of the house. Shows all rooms."}
        ]
    }
]


current_room_index = 0


game_running = True


def find_item(item_name, item_list):

    for item in item_list:
        if item["name"].lower() == item_name.lower():
            return item
    return None


def show_room_items():

    room = rooms[current_room_index]

    print(f"\n--- {room['name']} ---")
    print(room["description"])

    if len(room["items"]) == 0:
        print("There are no items here.")
    else:
        print("\nItems in the room:")
        for item in room["items"]:
            print(f"  - {item['name']} ({item['type']})")


def show_inventory():

    print(f"\n--- Inventory ({len(inventory)}/{MAX_INVENTORY}) ---")


    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:

        for item in inventory:
            print(f"  - {item['name']} ({item['type']}) | Uses left: {item['uses']}")


def pick_up(item_name):

    room = rooms[current_room_index]

    if len(inventory) >= MAX_INVENTORY:
        print("Your inventory is full! Drop something first.")
        return

    item = find_item(item_name, room["items"])

    if item is None:
        print(f"There is no '{item_name}' here.")
        return


    room["items"].remove(item)
    inventory.append(item)
    print(f"You picked up the {item['name']}.")


def drop(item_name):

    room = rooms[current_room_index]


    item = find_item(item_name, inventory)

    if item is None:
        print(f"You don't have '{item_name}' in your inventory.")
        return


    inventory.remove(item)
    room["items"].append(item)
    print(f"You dropped the {item['name']}.")


def use(item_name):

    global game_running


    item = find_item(item_name, inventory)

    if item is None:
        print(f"You don't have '{item_name}' in your inventory.")
        return


    if item["uses"] <= 0:
        print(f"The {item['name']} is used up.")
        return


    if item["type"] == "healing":
        print(f"You use the {item['name']}. You feel better!")

    elif item["type"] == "food":
        print(f"You eat the {item['name']}. Yummy! Health restored.")

    elif item["type"] == "tool" and item["name"] == "torch":
        print("You hold up the torch. The room lights up~")

    elif item["type"] == "tool" and item["name"] == "key":

        if rooms[current_room_index]["name"] == "Living Room":
            print("\n*** You use the key on the front door... ***")
            print("*** The door creaks open. You RUN outside. ***")
            print("\n🎉 YOU ESCAPED THE HAUNTED HOUSE! YOU WIN! 🎉\n")
            game_running = False
        else:
            print("There is nothing to unlock here.")
            return

    elif item["type"] == "weapon":
        print(f"You swing the {item['name']} at the shadows. They retreat!")

    elif item["type"] == "tool" and item["name"] == "map":
        print("\n--- MAP ---")

        for i, room in enumerate(rooms):

            if i == current_room_index:
                print(f"  > {room['name']} (YOU ARE HERE)")
            else:
                print(f"    {room['name']}")


    item["uses"] -= 1


    if item["uses"] <= 0:
        inventory.remove(item)
        print(f"(The {item['name']} has been used up and removed.)")


def examine(item_name):

    room = rooms[current_room_index]


    item = find_item(item_name, inventory)


    if item is None:
        item = find_item(item_name, room["items"])


    if item is None:
        print(f"You don't see any '{item_name}' here.")
        return


    print(f"\n--- {item['name']} ---")
    print(f"Type: {item['type']}")
    print(f"Description: {item['description']}")
    print(f"Uses left: {item['uses']}")


def go_to_room(room_name):

    global current_room_index


    for i, room in enumerate(rooms):
        if room["name"].lower() == room_name.lower():
            current_room_index = i
            print(f"\nYou move to the {room['name']}.")
            show_room_items()
            return

    print(f"There is no room called '{room_name}'.")


def show_help():

    print("""
--- COMMANDS ---
  look              : Look around the current room
  inventory         : Show your inventory
  pickup [item]     : Pick up an item (e.g. pickup torch)
  drop [item]       : Drop an item (e.g. drop torch)
  use [item]        : Use an item (e.g. use potion)
  examine [item]    : Examine an item (e.g. examine key)
  go [room]         : Move to a room (e.g. go Kitchen)
  help              : Show this list
  quit              : Quit the game
""")


# ============================================================
# MAIN GAME LOOP
# ============================================================

def get_item_hint(item_name):

    hints = {
        "key":     "Maybe this opens a locked door somewhere...",
        "torch":   "Could be useful in a dark room. Try 'use torch'.",
        "bandage": "Looks like it could patch up a wound. Try 'use bandage'.",
        "apple":   "Looks fresh. Probably edible. Try 'use apple'.",
        "knife":   "Sharp. Might be useful against something scary...",
        "potion":  "A glowing liquid. Probably healing. Try 'use potion'.",
        "map":     "A map of the house. Try 'use map' to see the layout.",
    }

    return hints.get(item_name.lower(), "Not sure what this does yet. Try 'examine' or 'use'.")

def main():

    global game_running

    # Introduction
    print("=" * 50)
    print("   👻 HAUNTED HOUSE ESCAPE 👻")
    print("=" * 50)
    print("""
You wake up on the floor of a dusty bedroom.
The door outside is locked.
You need to find the KEY and reach the LIVING ROOM
to escape. But be careful — you are not alone...

Type 'help' to see all commands.
""")

    show_room_items()


    while game_running:

        room = rooms[current_room_index]


        print("\n" + "─" * 40)


        if len(room["items"]) > 0:
            item_names = [item["name"] for item in room["items"]]
            print(f"📦 You see: {', '.join(item_names)}")


        if len(inventory) > 0:
            inv_names = [item["name"] for item in inventory]
            print(f"🎒 Carrying: {', '.join(inv_names)}")


        other_rooms = [r["name"] for i, r in enumerate(rooms) if i != current_room_index]
        print(f"🚪 Exits: {', '.join(other_rooms)}")


        print("\nCommands: look | pickup [item] | use [item] | drop [item] | go [room] | examine [item] | help")
        print("─" * 40)

        print()
        user_input = input("> ").strip().lower()

        parts = user_input.split(" ", 1)
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        if command == "look":
            show_room_items()

        elif command == "inventory":
            show_inventory()

        elif command == "pickup":
            if argument == "":
                print("Pick up what? (e.g. pickup torch)")
            else:
                pick_up(argument)

                item = find_item(argument, inventory)
                if item:
                    print(f"💡 Hint: {get_item_hint(item['name'])}")

        elif command == "drop":
            if argument == "":
                print("Drop what? (e.g. drop torch)")
            else:
                drop(argument)

        elif command == "use":
            if argument == "":
                print("Use what? (e.g. use potion)")
            else:
                use(argument)

        elif command == "examine":
            if argument == "":
                print("Examine what? (e.g. examine key)")
            else:
                examine(argument)

        elif command == "go":
            if argument == "":
                print("Go where? (e.g. go Kitchen)")
            else:
                go_to_room(argument)

        elif command == "help":
            show_help()

        elif command == "quit":
            print("\nYou gave up and faded into the haunted house forever...")
            print("GAME OVER.\n")
            game_running = False

        else:
            print(f"Unknown command: '{command}'. Type 'help' for commands.")

# ============================================================
# ENTRY POINT
# ============================================================
if __name__ == "__main__":
    main()