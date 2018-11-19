import math

budget = float(input())
clients = int(input())
gbs = int(input())
hosts = int(input())
uptime = float(input())

servers = math.ceil(clients / 50)
storages = math.ceil(gbs / 0.5)

expenses = (2 * 720 * servers + 0.5 * 720 * storages + 10 * hosts) * (uptime / 100)

if (budget - expenses) >= 0:
    print('Clouds Ahoy! Monthly cost: ${0:.2f} (${1:.2f} leftover)'.format(expenses,budget - expenses))
else:
    print('Stay Grounded! Monthly cost: ${0:.2f} (Need ${1:.2f} more)'.format(expenses, expenses - budget))