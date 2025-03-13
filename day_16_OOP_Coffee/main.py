from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()
money= MoneyMachine()
on = True
while on:
    order = input(f"What would you like to order? ({menu.get_items()}): ")

    if order == "report":
        coffee.report()
        money.report()
    elif order == "off":
        on = False
    else:
        drink = menu.find_drink(order)
        resource = coffee.is_resource_sufficient(drink)

        if resource:
            payment = money.make_payment(drink.cost)

            if payment:
                coffee.make_coffee(drink)
            





