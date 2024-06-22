import itertools

if __name__ == "__main__":
    l, c = map(int, input().split())
    words = list(input().split())
    vowel = {'a', 'e', 'i', 'o', 'u'}
    answer = []

    for candidate in itertools.combinations(words, l):
        vowel_count = 0
        consonant_count = 0

        for i in candidate:
            if i in vowel:
                vowel_count += 1
            else:
                consonant_count += 1

        if vowel_count >= 1 and consonant_count >= 2:
            answer.append(''.join(sorted(candidate)))

    answer.sort()
    for i in answer:
        print(i)
