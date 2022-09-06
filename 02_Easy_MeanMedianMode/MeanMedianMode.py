def main():
    list_test = [23, 23, 23, 6, 6, 23, 17, 23, 6, 6, 23]
    print("List:", list_test)

    # Mean
    mean = sum(list_test)/len(list_test)
    print("Mean:", mean)

    # Median
    list_test.sort()
    if len(list_test) % 2 == 0:
        median_1 = list_test[len(list_test) // 2]
        median_2 = list_test[len(list_test) // 2]
        median = (median_1 + median_2) / 2
    else:
        median = list_test[len(list_test) // 2]

    print("Median:", median)

    # Mode
    frequency_dict = {}
    for i in list_test:
        frequency_dict.setdefault(i, 0)
        frequency_dict[i] += 1

    frequent = max(frequency_dict.values())
    for i, j in frequency_dict.items():
        if j == frequent:
            mode = i

    print("Mode:", mode)


if __name__ == '__main__':
    main()
