from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino/):​”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
# Make an object
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    options = menu.get_items()
    order_name = input(f"What would you like? {options} ").lower() # Using a class to print out menu items
    # TODO: 2. Turn off the Coffee Machine by entering “​off”​to the prompt.
    # a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the
    # machine. Your code should end execution when this happens.
    if order_name == "off":
        is_on = False

    # TODO: 3. Print report.
    # a. When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
    # Water: 100ml
    # Milk: 50ml
    # Coffee: 76g Money: $2.5
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        find_drink = menu.find_drink(order_name)
        drink = MenuItem(find_drink.name, find_drink.ingredients['water'], find_drink.ingredients['milk'],
                         find_drink.ingredients['coffee'], find_drink.cost)
        # TODO 4. Check resources sufficient?
        # a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
        # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “​Sorry there is not enough water.​”
        # c. The same should happen if another resource is depleted, e.g. milk or coffee
        if coffee_maker.is_resource_sufficient(drink) == True and money_machine.make_payment(find_drink.cost) == True:
            coffee_maker.make_coffee(drink)
