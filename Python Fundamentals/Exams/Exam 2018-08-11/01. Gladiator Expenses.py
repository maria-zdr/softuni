lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0 and i % 3 == 0:
        expenses += helmet_price + sword_price + shield_price
    elif i % 2 == 0:
        expenses += helmet_price
    elif i % 3 == 0:
        expenses += sword_price

    if i % 12 == 0:
        expenses += +armor_price

print('Gladiator expenses: {0:.2f} aureus'.format(expenses))