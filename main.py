MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def paid_amount():
    quarters = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes?: ")) * 0.10
    nickles = float(input("how many nickles?: ")) * 0.05
    pennies = float(input("how many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def check_if_available(drink):
    if resources["water"] - MENU[drink]["ingredients"]["water"] < 0:
        print("no enough water")
        return False
    elif resources["milk"] - MENU[drink]["ingredients"]["milk"] < 0:
        print("no enough water")
        return False
    elif resources["coffee"] - MENU[drink]["ingredients"]["coffee"] < 0:
        print("no enough coffee")
        return False
    else:
        return True


def check_money_amount(drink, money_paid):
    """checks if the paid amount is enough and return the amount or return false"""

    exchange = money_paid - MENU[drink]["cost"]
    if exchange < 0:
        print("no enough money")
        return False
    else:
        return exchange


def reduce_the_resources(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]


def chosen_drink_price(drink):
    return MENU[drink]["cost"]


earned_amount = 0
machine_working = True
while machine_working:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "log":
        print(f"earned money {earned_amount} $")
        print(f"water: {resources['water']}\nmilk: {resources['milk']}\ncoffee: {resources['coffee']}")
    elif user_choice == "stop":
        break
    else:
        if check_if_available(user_choice):
            amount_to_return = check_money_amount(user_choice, paid_amount())
            if amount_to_return:
                print(f"here is your exchange {round(amount_to_return, 2)} $ ")
                print("your coffee on the way")
                reduce_the_resources(user_choice)
                earned_amount += chosen_drink_price(user_choice)

            else:
                print(f"no enough money it requires {MENU[user_choice]['cost']} $")
        else:
            print("sorry not available")
