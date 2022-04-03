# Robot barista test 1.9
# Variables 

price = 1.00
menu = "Black Coffee, Espresso, Cappucino, and Latte"
yes_list = ["yes",
    "yea",
    "yup",
    "yeah",
    "ye"
]
# The Code

print("Hello! Welcome to Python Coffee!")

name = input("What is your name?\n")

if name.capitalize() == "Ben" or name.capitalize() =="Tom":
  evil_status = input("Are you evil?\n") 
  for evil_status in yes_list:
    if evil_status.lower() == evil_status:
        print("YOU AREN'T WELCOME HERE! LEAVE NOW!")
        quit()
    else:
        print("Oh, so you're not evil. Come on in.")
else:
  print(f"Hello {name.capitalize()}, thank you for coming today!\n")

print(f"{name.capitalize()}, What would you like to order today? Here is what we are serving today.\n{menu}")

order = input("")

quantity = float(input("How many coffees would you like?\n"))

total = price * quantity

print(f"Okay your total will be ${str(total)}")

print("We'll have those ready soon.")