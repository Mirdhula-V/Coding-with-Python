word = input()
word_length = len(word)

print(word[0] + ("*" * (word_length-2)) + word[word_length-1])