import random
import time
import word_list
import math
words_list = []

for i in range(0, 50):
    words_list.append(random.choice(word_list.common_word_list).lower()+' ')

words_list = ''.join(words_list)
words_list = 'hello how are you'

print(words_list)
start = time.time()
type_checker = input('Enter the words you see: ')
end = time.time()
print(len(type_checker))

user_word_list = type_checker.split(' ')

score = 0

# score checker
correct_words = []
for index in range(0, len(words_list)):
    try:
        if words_list[index] == user_word_list[index]:
            correct_words.append(user_word_list[index])
            score += 1
    except IndexError:
        break



print(f'You wrote {score} words in {end-start} seconds\n'
      f'Your score is {score} correct words out of {len(words_list)}\n'
      f'You write {round((60/(end-start))*score)} words per minute\n'
      f'''You write {round((60/(end-start))*len(''.join(correct_words)))} characters per minute''')

