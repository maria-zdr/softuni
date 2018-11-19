import operator

class BankAccount:
    def __init__(self, bank, name, balance):
        self.name = name
        self.bank = bank
        self.balance = balance


list_accounts = []

while True:
    data = input()
    if data == 'end':
        break

    list_data = data.split(' | ')
    account = BankAccount(list_data[0], list_data[1], float(list_data[2]))
    list_accounts.append(account)

l1 = sorted(list_accounts, key=lambda acc: len(acc.bank))
l2 = sorted(l1, key=lambda acc: acc.balance, reverse=True)

for item in l2:
    print('{0} -> {1:.2f} ({2})'.format(item.name, item.balance, item.bank))
