import random
respond = ["Is that so?", 
  "Would you mind elaborating?", 
  "Why, that's rather interesting.",
  "Please, continue."
]

name = input("What is your name?\n> ")
while True:
  answer = input("\nThank you. It's nice to meet you " + name + ". Now, I'm here to listen. I'm here for you.\n")
  while answer == "Exit":
    quit()
  while answer != "Exit":
    print(random.choice(respond))
    answer2 = input("")
    if answer2 == "Exit":
      quit()