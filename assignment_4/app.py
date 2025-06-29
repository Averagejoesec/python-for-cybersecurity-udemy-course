from inventory import inventory as inv


apple = inv('apple', '5', 'fruit')
banana = inv('banana', '3', 'fruit')
kiwi = inv('kiwi', '6', 'fruit')


current_inventory = [apple, banana, kiwi]

# A function that adds something to that list (creates the dictionary and adds to the list).
def add_inventory(name, quantity, description):
    inv(name, quantity, description)
    # inv.current_inventory.append(new_item)
    return


# A function that displays the inventory in a readable format (i.e. do not just print out the list or dictionary, separate them out).
def show_inventory():
    for i in inv.current_inventory:
        print(i.name, i.quantity, i.description)


# A function that will change the quantity of an item (this is difficult to do and many ways to do it).
def update_quantity(name, new_quantity):
    try:
        for i in inv.current_inventory:
            if i.name == name:
                i.quantity = new_quantity
    except:
        print("Item not found.")   


# A function that removes an item from the list. Research required
def remove_item(name):
    try:
        for i in inv.current_inventory:
            if i.name == name:
                inv.current_inventory.remove(i)
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
        print("Current inventory:")
        show_inventory()
        main()

    elif choice == 'add':
        item_name = input("Name of the item: ")
        item_quantity = int(input("Quantity: "))
        item_description = input("Item description (one word): ")
        if len(item_description.split(" ")) > 1:
            print("Please enter one word description.")
            main()
        elif len(item_name.split(" ")) > 1:
            print("Please enter a one word item.")
            main()
        else:
            add_inventory(item_name, item_quantity, item_description)
            print("Updated inventory:")
            show_inventory()
            main()

    elif choice == 'update':
        item_name = input("Name of the item: ")
        item_quantity = int(input("New quantity: "))
        update_quantity(item_name, item_quantity)
        show_inventory()
        main()

    elif choice == 'remove':
        item_name = input("Name of the item: ")
        remove_item(item_name)
        show_inventory()
        main()

    elif choice =='exit':
        print("Final inventory:")
        show_inventory()
        exit()

    else:
        print("Final inventory:")
        show_inventory()
        exit()


if __name__ == "__main__":
    main()