def insertion_sort(list_data):
    for index in range(1, len(list_data)):
        current = list_data[index]

        while index > 0 and list_data[index - 1] < current:
            list_data[index] = list_data [index - 1]
            index -= 1

        list_data[index] = current


list_numbers = list(map(int, input().split(' ')))
n = int(input())

insertion_sort(list_numbers)
print(' '.join(map(str,list_numbers[0: n])))
