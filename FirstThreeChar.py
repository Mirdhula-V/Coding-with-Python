first_word = input()
second_word = input()

three_letters_in_first_word = first_word[:3]
three_letters_in_second_word = second_word[:3]

result = three_letters_in_first_word == three_letters_in_second_word

print(result)