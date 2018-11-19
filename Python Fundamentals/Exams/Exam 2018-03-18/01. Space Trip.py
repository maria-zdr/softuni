star = input()
distance = int(input())
budget = int(input())
fuel_consumption = float(input())
fuel_price = float(input())

result = (fuel_consumption/100) * fuel_price * distance

if (budget - result) >= 0:
    print('Off to {0} with ${1:.2f} for snacks'.format(star, budget - result))
else:
    print('Maybe another time, need ${0:.2f} more'.format(result - budget))