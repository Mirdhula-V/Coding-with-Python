word = input()
length_of_word = len(word)
stars = length_of_word - 4
stars = int(stars)
start_index = length_of_word - 2
start_index = int(start_index)
new_string = word[:2] + ("*" * stars) + word[start_index:]

print(new_string)