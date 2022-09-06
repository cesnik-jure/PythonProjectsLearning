def main():
    words = ["tea", "eat", "bat", "ate", "arc", "car"]
    group_anagrams(words)


def group_anagrams(word_list):
    default_dict = {}

    for i in word_list:
        sorted_i = " ".join(sorted(i))
        default_dict.setdefault(sorted_i, [])
        default_dict[sorted_i].append(i)

    for i, j in default_dict.items():
        print(f"Anagram words with letters '{i}':")
        for k in j:
            print(k)


if __name__ == '__main__':
    main()
