def add_menu_item(menu, item):
    menu.append(item)
    return menu
def remove_menu_item(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(f"{item} not found in the menu.")
    return menu
def check_availability(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

if __name__ == __main__:
    initial_menu = [Pizza, Burger, Pasta, Salad]
    add_item = Tacos
    remove_item = Salad
    check_item = Pizza
    updated_menu = add_menu_item(initial_menu, add_item)
    updated_menu = remove_menu_item(updated_menu, remove_item)
    availability = check_availability(updated_menu, check_item)
    print(f"Updated menu {updated_menu}")
    print(f"Availability {availability}")

