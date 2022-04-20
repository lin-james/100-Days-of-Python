from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
is_on = True

while is_on:
    prompt = input(f"What would you like? {menu.get_items()}: ").lower()
    if prompt == 'report':
        coffee_maker.report()
    elif prompt == 'off':
        is_on = False
        print("Machine is off")
    else:
        drink = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
