word_1 = input()
word_2 = input()
word_3 = input()

if word_1 < word_2 and word_1 < word_3:
    if word_2 < word_3:
        print(word_1, word_2, word_3)

    elif word_3 < word_2:
        print(word_1, word_3, word_2)


if word_2 < word_3 and word_2 < word_1:
    if word_1 < word_3:
        print(word_2, word_1, word_3)

    elif word_3 < word_1:
        print(word_2, word_3, word_1)


if word_3 < word_2 and word_3 < word_1:
    if word_2 < word_1:
        print(word_3, word_2, word_1)

    elif word_1 < word_2:
        print(word_3, word_1, word_2)


if word_3 == word_2 == word_1:
    print("They're the same words:", word_1, word_2, word_3 )