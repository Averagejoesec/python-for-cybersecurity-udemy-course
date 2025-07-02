# Each item will have a name, quantity, and description as a dictionary.
# All dictionaries will be saved in a master inventory list.
inventory = [
            {'name': 'apple', 'quantity': '5', 'description': 'Fruit'},
            {'name': 'hammer', 'quantity': '3', 'description': 'Tool'},
            {'name': 'couch', 'quantity': '2', 'description': 'Furniture'}
]

# A function that adds something to that list (creates the dictionary and adds to the list).
def add_inventory(name, quantity, description):
    new_item = {'name': name, 'quantity': quantity, 'description': description}
    inventory.append(new_item)


# A function that displays the inventory in a readable format (i.e. do not just print out the list or dictionary, separate them out).
def show_inventory():
    for i in inventory:
        print(i)


# A function that will change the quantity of an item (this is difficult to do and many ways to do it).
def update_quantity(name, new_quantity):
    try:
        for i in inventory:
            if i.get('name') == name:
                i['quantity'] = new_quantity
    except:
        print("Item not found.")   


# A function that removes an item from the list. Research required
def remove_item(name):
    try:
        for i in inventory:
            if i.get('name') == name:
                inventory.remove(i)
    except:
        print("Item does not exist.")


def choice_input():
    try:
        choice = input("Would you like to 'see', 'add', 'update', 'remove' the current inventory or 'exit'?\n")
        choice.lower()
    except:
        print("Please input a proper choice.")
        choice_input()
    return choice


def main():
    choice = choice_input()

    if choice =='see':
        show_inventory()
        choice_input()

    elif choice == 'add':
        item_name = input("Name of the item: ")
        item_quantity = int(input("Quantity: "))
        item_description = input("Item description (one word): ")
        if len(item_description.split(" ")) > 1:
            print("Please enter one word description.")
            choice_input()
        elif len(item_name.split(" ")) > 1:
            print("Please enter a one word item.")
            choice_input()
        else:
            add_inventory(item_name, item_quantity, item_description)
            print("Updated inventory:")
            show_inventory()

    elif choice == 'update':
        item_name = input("Name of the item: ")
        item_quantity = int(input("New quantity: "))
        update_quantity(item_name, item_quantity)
        show_inventory()
        choice_input()

    elif choice == 'remove':
        item_name = input("Name of the item: ")
        remove_item(item_name)
        show_inventory()
        choice_input()

    elif choice =='exit':
        exit()

    else:
        print("Final inventory:")
        show_inventory()
        exit()


if __name__ == "__main__":
    main()