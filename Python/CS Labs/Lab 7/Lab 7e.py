word = input()

wordLen = len(word)

if wordLen % 2 == 0:
    print(word[(wordLen//2)-1] + word[wordLen//2] )

if wordLen % 2 == 1:
    print(word[wordLen//2])