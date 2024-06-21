if __name__ == "__main__":
    words = set()
    for _ in range(int(input())):
        words.add(input())

    word_list = sorted(words, key=lambda x: (len(x), x))
    for word in word_list:
        print(word)
