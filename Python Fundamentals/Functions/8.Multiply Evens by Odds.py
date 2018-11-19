def get_strange_multiplication(n):
    sum_even = 0
    sum_odd = 0

    while n > 0:
        ld = n % 10
        n = n // 10

        if ld % 2 == 0:
            sum_even += ld
        else:
            sum_odd += ld

    return sum_even * sum_odd


num = int(input())
print(get_strange_multiplication(abs(num)))


