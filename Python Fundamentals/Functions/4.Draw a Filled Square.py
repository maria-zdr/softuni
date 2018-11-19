def print_dashes(n):
    print('-' * 2 * n)


def print_middle(n):
    for i in range(0, n - 2):
        print('-' + '\\/' * (n - 1) + '-')


num = int(input())
print_dashes(num)
print_middle(num)
print_dashes(num)
