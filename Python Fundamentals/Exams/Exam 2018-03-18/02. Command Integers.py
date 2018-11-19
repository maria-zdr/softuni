def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


import operator

state_ints = list(map(int, input().split()))
command_ints = list(map(int, input().split()))

for item in command_ints:
    mul_or_div = operator.mul if is_even(item) else operator.floordiv
    parity = 0 if is_even(item) else 1
    state_ints = [mul_or_div(num, abs(item)) if is_even(num) == parity else num for num in state_ints]

    filter_sign = lambda num: num < 0 if item < 0 else num > 0
    state_ints = [num + item if filter_sign(num) else num for num in state_ints]

'''
for item in command_ints:
    if is_even(item):
        for i in range(0, len(state_ints)):
            if is_even(state_ints[i]):
                state_ints[i] = state_ints[i] * abs(item)
    else:
        for i in range(0, len(state_ints)):
            if not is_even(state_ints[i]):
                state_ints[i] = state_ints[i] // abs(item)

    if item > 0:
        for i in range(0, len(state_ints)):
            if state_ints[i] > 0:
                state_ints[i] = state_ints[i] + item
    elif item < 0:
        for i in range(0, len(state_ints)):
            if state_ints[i] < 0:
                state_ints[i] = state_ints[i] + item
'''

print(state_ints)