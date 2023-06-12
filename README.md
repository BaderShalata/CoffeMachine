# CoffeMachine
Created a CoffeMachine project using Python.
First of, I created a dictionary called "Coffe" that contains 3 "keys"(Espresso,Latte,capuccino), I created individual dictionaries for each of the keys, and another nested dictionary for (ingredients) and price.
This project has a While True loop, asks the user for Input (named - "answer"), if answer == "report", a report of machine resources is shown,
                                                                                if answer == "off", while loop breaks and program quits,
                                                                                if answer == "espresso/latte/capuccino", sufficient_res(answer) method
is called where this method calculates if there are sufficient amount of resources for the order.
in this method, the (2) method is called -> coins_based(), that accepts input for payment (obv if condition suff res is met).
after asking the user for input, the program checks if payment is less than the price (in this case it rejects and refunds the user) else it accepts the payment and updates the price in the machine dictionary (accumulated price if multiple orders).
