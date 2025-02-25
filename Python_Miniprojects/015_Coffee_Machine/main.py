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

# Function to print the available resources
def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")

# Function to print available resources
def  check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_payment(drink_cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_inserted = quarters+dimes+nickles+pennies

    if total_inserted < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return None # Not enough money
    else:
        change = round(total_inserted - drink_cost, 2)
        if change > 0:
            print(f"Here is {change} in change")
        return True # Payment successful

# Function to make the drink and update resources
def make_drink(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink}. Enjoy!  ☕")

# Main function to run the coffee machine
def operate():
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino) ")

        if user_input == "off":
            print("Turning off the coffee machine. Goodbye! ")
            break
        elif user_input == "report":
            report()
        elif user_input in MENU:
            if check_resources(user_input):
                if process_payment(MENU[user_input]["cost"]):
                    make_drink(user_input)
        else:
            print("Invalid input. Please choose a valid drink.")


operate()
