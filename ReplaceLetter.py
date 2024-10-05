word = input()
i = int(input())
copy_letter = input()
length_of_word = len(word)
length_of_word = int(length_of_word)
first_word = word[:i]
start_index = i+1 
start_index = int(start_index)
second_word = word[start_index:]
result = first_word + copy_letter + second_word

print(result)