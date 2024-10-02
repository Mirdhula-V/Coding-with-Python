word = input()
number = int(input())
no_of_characters = len(word)
start_index = no_of_characters - 3
repeting_string = word[start_index:] * number

print(repeting_string)