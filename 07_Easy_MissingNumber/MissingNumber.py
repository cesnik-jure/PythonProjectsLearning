def main():
    import timeit

    list_of_numbers_input = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16, 100]
    result = timeit.timeit(stmt=f'findmissingnumber({list_of_numbers_input})', globals=globals(), number=1)
    print(result)


def findmissingnumber(list_of_numbers):
    start_of_list = list_of_numbers[0]
    end_of_list = list_of_numbers[-1]
    list_of_missing_numbers = []

    for number in range(start_of_list, end_of_list):
        if number not in list_of_numbers:
            list_of_missing_numbers.append(number)

    print(list_of_missing_numbers)


if __name__ == '__main__':
    main()
