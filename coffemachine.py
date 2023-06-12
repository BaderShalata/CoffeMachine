coffe = {
    "espresso" : {
         "ingrd":{
             "Water": 50,
             "Coffee": 18,
         },
        "Price": 1.5,
    },
    "latte":  {
        "ingrd":{
            "Water": 200,
            "Coffee": 24,
            "Milk": 150,
        },
        "Price": 2.5,
     },
    "capuccino":{
        "ingrd":{
            "Water": 250,
            "Coffee": 24,
            "Milk": 100,
        },
        "Price": 3,
    }
}
machine = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Price": 0
}
def coin_based():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    total = (quarters * 0.25)
    dimes = float(input("How many dimes?: "))
    total += (dimes * 0.1)
    nickles = float(input("How many nickels?: "))
    total += (nickles * 0.05)
    pennies = float(input("How many pennies?: "))
    total += (pennies * 0.01)
    if total >= drink["Price"]:
        print(f"You have bought {answer}")
        change = total - drink["Price"]
        print(f"Your change is {change}")
        machine["Price"] += drink["Price"]
    else:
        print(f"Insufficient Amount, you have been refunded {total} ")


def sufficient_res(answer):
    for item in answer:
        if(answer[item] <= machine[item]):
            machine[item] = machine[item] - answer[item]
        else:
            print("Insufficient Resources")
            break
    coin_based()

while True:
    answer = input("(Espresso/Latte/Capuccino) OR report, off to exit: ").lower()
    if answer == "report":
        print(machine)
    elif answer == "off":afu
        break
    else:
        drink = coffe[answer]
        sufficient_res(drink["ingrd"])
        print(f"Machine resources now are: {machine}")
s
