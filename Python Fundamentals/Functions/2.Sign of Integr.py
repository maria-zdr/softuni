def get_sign(n):
    if n == 0:
        print('The number {} is zero.'.format(n))
    elif n > 0:
        print('The number {} is positive.'.format(n))
    else:
        print('The number {} is negative.'.format(n))


num = int(input())
get_sign(num)
