from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

state = "on"
while state != "off":
    decision = input(f"What would you like? ({menu.get_items()})\n")
    if decision == "report":
        coffee_maker.report()
        money_machine.report()
    elif decision == "off":
        state = "off"
    elif decision == "espresso" or decision == "latte" or decision == "cappuccino":
        drink = menu.find_drink(decision)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


