def get_greater(dtype, val1, val2):
    if dtype == 'int':
        if int(val1) >= int(val2):
            result = val1
        else:
            result = val2
    else:
        if val1 >= val2:
            result = val1
        else:
            result = val2

    return result

dt = input()
v1 = input()
v2 = input()

print(get_greater(dt, v1, v2))
