inventory = input().split()

while True:
    data = input().split()
    if data[0] == 'Fight!':
        break

    command = data[0]
    equipment = data[1].split('-')[0]

    if command == 'Buy' and equipment not in inventory:
        inventory.append(equipment)
    elif command == 'Trash' and equipment in inventory:
        inventory.remove(equipment)
    elif command == 'Repair' and equipment in inventory:
        inventory.remove(equipment)
        inventory.append(equipment)
    elif command == 'Upgrade' and equipment in inventory:
        upgrade = data[1].split('-')[1]
        ix = inventory.index(equipment)
        inventory.insert(ix + 1, equipment + ':' + upgrade )

print(' '.join(inventory))
