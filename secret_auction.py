bids = {}

imp = ""
while imp != "no":
    name = input("Was ist dein name?\n")
    money = int(input("How much dollar do you want to bid?\n"))

    bids[name] = money

    imp = input("Other bider? (yes/no)\n")

highest_money = 0
highest_name = ""
dead_heat_names = []
for key, value in bids.items():
    if value > highest_money:
        highest_name = key
        highest_money = value
        dead_heat_names.clear()

    elif value == highest_money:
        dead_heat_names.append(highest_name)
        dead_heat_names.append(key)

if not dead_heat_names:
    print(f"The winner is {highest_name} with ${highest_money}")
else:
    print(f"Multiple people came up with the same bet!")
    print(f"{dead_heat_names} with {highest_money}")
