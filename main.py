import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(f"{random.choice(names)} is going to buy the meal today!")