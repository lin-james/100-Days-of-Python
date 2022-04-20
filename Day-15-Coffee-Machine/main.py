from inspect import walktree
from tabnanny import check
from prompt_toolkit import prompt
from data import MENU, resources

is_on = True
money = 0


def check_resources(drink):
    """Checks if resources are sufficient"""
    is_suff = True
    for item in drink:
        if resources[item] < drink[item]:
            print(f"Sorry there's not enough {item}")
            is_suff = False
    return is_suff


def insert_coin():
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01,
    }
    print("Please insert coins.\n")
    total = 0
    for coin in coins:
        total += coins[coin] * int(input(f"How many {coin}?: "))

    return total


def check_price(cost, coin):

    if cost <= coin:
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(ingredient):

    for item in ingredient:
        resources[item] -= ingredient[item]


while is_on:
    prompt = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    # drink prompt
    if prompt == 'latte' or prompt == 'espresso' or prompt == 'cappuccino':
        if check_resources(MENU[prompt]["ingredients"]):
            coin = insert_coin()
            if check_price(MENU[prompt]["cost"], coin):
                change = round(coin - MENU[prompt]["cost"], 2)
                if change > 0:
                    print(f"Here is ${change} dollars in change.")
                money += MENU[prompt]["cost"]

                make_coffee(MENU[prompt]["ingredients"])
    elif prompt == 'off':
        is_on = False
        print("Machine is off.")
    # report prompt
    elif prompt == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money}')
    else:
        print("🖕")
