from art import logo, coffee
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

#MACHINE WORKING
print(logo)

machine_on = True

while machine_on:
    prepare_order = True
    while prepare_order:
        options = menu.get_items()
        order = input(f"What would you like ? ({options}) ").lower()
        if order == "report":
            coffee_maker.report()
            money.report()
            prepare_order = False
        elif order == "off":
            machine_on = False
            prepare_order = False
        else:
            drink = menu.find_drink(order)
            ingredients_avaible = coffee_maker.is_resource_sufficient(drink)
            if not ingredients_avaible:
                prepare_order = False
            else:
                enough_money = money.make_payment(drink.cost)
                if not enough_money:
                    prepare_order = False
                else:
                    coffee_maker.make_coffee(drink)
                    print(coffee)
