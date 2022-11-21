MENU = {
    "espresso": {
        "ingredients": {
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

profit = 0


def ingredient_error_display(ingredients):
    print(f"Sorry there is not enough {', '.join(ingredients)}")


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_ingredients(drink):
    ingredient_error = False
    ingredients_missing = []
    for key, value in MENU[drink]["ingredients"].items():
        if value > resources[key]:
            ingredient_error = True
            ingredients_missing.append(key)

    if ingredient_error:
        return ingredients_missing
    else:
        return True


def coin_insertion(drink):
    print(f"Insert coins! ${MENU[drink]['cost']}")
    quarters_count = int(input("How many quarters? "))
    dimes_count = int(input("How many dimes? "))
    nickles_count = int(input("How many nickles? "))
    pennies_count = int(input("How many pennies? "))

    total_money_inserted = round(0.25 * quarters_count + 0.1 * dimes_count + 0.05 * nickles_count + 0.01 * pennies_count, 2)
    if total_money_inserted < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        # returns "Error" so the program knows the money was not enough
        return "Error"
    else:
        global profit
        profit += MENU[drink]['cost']
        # returns the change
        return total_money_inserted - MENU[drink]["cost"]


def make_coffee(drink):
    for key, value in MENU[drink]["ingredients"].items():
        resources[key] -= value
    print(f"Here is your {drink}. Enjoy!")


def drink_chosen(drink):
    ingredients_state = check_ingredients(drink)

    if ingredients_state is True:
        coin_state = coin_insertion(drink)

        if coin_state != "Error":
            print(f"Here is ${coin_state} in change.")

            make_coffee(drink)
    else:
        ingredient_error_display(ingredients_state)


state = "on"
while state != "off":
    decision = input("What would you like? (espresso/latte/cappuccino): ")
    if decision == "off":
        state = "off"
    elif decision == "report":
        report()
    elif decision == "espresso" or decision == "latte" or decision == "cappuccino":
        drink_chosen(decision)
    else:
        print("Invalid!")
