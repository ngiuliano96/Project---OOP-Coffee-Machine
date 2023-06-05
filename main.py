from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Set objects from classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    menu_choices = menu.get_items()
    user_choice = input(f"What would you like? {menu_choices}: ")

    if user_choice == "off":
        print("Goodbye!")
        is_on = False
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        current_order = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(current_order) and money_machine.make_payment(current_order.cost):
            coffee_maker.make_coffee(current_order)


