class Dog:
    def __init__(self, name, age, number_of_legs):
        self.name = name
        self.age = age
        self.number_of_legs = number_of_legs

    def produce_sound(self):
        print('I\'m a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.')


class Cat:
    def __init__(self, name, age, intelligence_quotient):
        self.name = name
        self.age = age
        self.intelligence_quotient = intelligence_quotient

    def produce_sound(self):
        print('I\'m an Aristocat, and I will now produce an aristocratic sound! Myau Myau.')


class Snake:
    def __init__(self, name, age, cruelty_coefficient):
        self.name = name
        self.age = age
        self.cruelty_coefficient = cruelty_coefficient

    def produce_sound(self):
        print('I\'m a Sophistisnake, and I will now produce a sophisticated sound! Honey, I\'m home.')


list_animals = []

while True:
    data = input()
    if data == 'I\'m your Huckleberry':
        break

    list_data = data.split()

    if list_data[0] == 'Dog':
        list_animals.append(Dog(list_data[1], int(list_data[2]), int(list_data[3])))
    elif list_data[0] == 'Cat':
        list_animals.append(Cat(list_data[1], int(list_data[2]), int(list_data[3])))
    elif list_data[0] == 'Snake':
        list_animals.append(Snake(list_data[1], int(list_data[2]), int(list_data[3])))
    elif list_data[0] == 'talk':
        for item in list_animals:
            if item.name == list_data[1]:
                item.produce_sound()

for item in list_animals:
    if type(item) is Dog:
        print('Dog: {}, Age: {}, Number Of Legs: {}'.format(item.name, item.age, item.number_of_legs))

for item in list_animals:
    if type(item) is Cat:
        print('Cat: {}, Age: {}, IQ: {}'.format(item.name, item.age, item.intelligence_quotient))

for item in list_animals:
    if type(item) is Snake:
        print('Snake: {}, Age: {}, Cruelty: {}'.format(item.name, item.age, item.cruelty_coefficient))

