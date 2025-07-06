from random import choice

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

profit=0
resources = {
    "water": 500,
    "milk": 500,
    "coffee": 40,
}

def is_ingredients_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is no enough {item}")
            return False
        return True

def process_coins():
    print("Please insert your coins")
    total=int(input("How many Penny?: ")) * 0.01
    total+=int(input("How many Nickel?: ")) * 0.05
    total+=int(input("How many Dime?: ")) * 0.1
    total+=int(input("How many quarters?: ")) * 0.25
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received > drink_cost:
        change=round(money_received - drink_cost, 2)
        print(f"Here is your {change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry, You don't have enough coins. Money refunded!")
        return False

def make_coffee(order_ingredients,drink_name):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}☕️. Enjoy.")



is_on=True
while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["profit"]}")
    else:
        drink=MENU[choice]
        if is_ingredients_available(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(drink["ingredients"],choice)







