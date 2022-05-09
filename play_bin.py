from tkinter import *
from word_generator import WordGenerator
import time


def text_calculator():
    return len(user_text.get('1.0', END))


def stopwatch(is_on):
    global start_time
    global finish_time
    global current_indx
    if current_indx == 0 and is_on == True:
        timer_label.config(text='{:10.2f}'.format(time.time() - start_time))
        timer_label.after(1, stopwatch)
    else:
        finish_time = time.time()
        timer_label.config(text='{:10.2f}'.format(finish_time - start_time))


def correct_word_counter():
    global chars_typed
    global word_generator
    global word_score
    word_score = 0
    print(chars_typed)
    if len(chars_typed) > 0:
        generated_word_list = word_generator.split()
        chars_typed_list = chars_typed.split()
        # print(generated_word_list)
        # print(chars_typed_list)
        for i, word in enumerate(chars_typed_list):
            if word == generated_word_list[i]:
                word_score += 1
    correct_word_label.config(text=f'Correct words: {word_score}')


def character_score():
    global char_score
    global total_char_count
    character_score_label.config(text=f'You wrote {char_score}/{total_char_count - 1} characters correctly')


def word_scorer():
    global word_score
    global word_generator
    generated_count = len(word_generator.split())
    word_score_label.config(text=f'You wrote {word_score}/{generated_count} words correctly')


def cpm_calculator():
    global start_time
    global finish_time
    global char_score
    print(f'You write {round(60 / (finish_time - start_time) * char_score)} characters per minute')


def wpm_calculator():
    global start_time
    global finish_time
    global word_score
    print(f'You write {round(60 / (finish_time - start_time) * word_score)} words per minute')


def key_press(event):
    global current_indx
    global total_char_count
    global start_time
    global char_score
    global chars_typed
    global exact_char
    exact_char = event.char
    user_text.config(state=NORMAL)
    game_char = user_text.get(f'1.{current_indx - 1}', f'1.{current_indx}')
    if current_indx == total_char_count:
        character_score()
        word_scorer()
        cpm_calculator()
        wpm_calculator()
        print('Game Over')
        user_text.config(state=DISABLED)
        return

    if current_indx == 1:
        start_time = time.time()
        stopwatch()

    if event.char.encode('utf-8') != b'\x08':
        chars_typed += event.char

    if event.char.encode('utf-8') == b'\x08' and current_indx != 1 and current_indx < total_char_count:
        if user_text.get(f'1.{current_indx - 2}', f'1.{current_indx - 1}') == chars_typed[-1]:
            char_score -= 1
            chars_typed = chars_typed[:-1]
        current_indx -= 1
        user_text.tag_remove('correct', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_remove('incorrect', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_add('delete', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_config('delete', background='white')

    if event.char == ' ':
        chars_typed += '*'

    elif event.char.encode('utf-8') == b'\r' and game_char == ' ':
        user_text.tag_add('correct', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_config('correct', background='green')
        char_score += 1
        current_indx += 1
        print('Try using the spacebar instead of enter for the words')

    elif game_char == event.char:
        user_text.tag_delete('delete')
        user_text.tag_add('correct', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_config('correct', background='green')
        char_score += 1
        current_indx += 1

    elif game_char != event.char or event.char.encode('utf-8') != b'\r' and game_char != ' ':
        user_text.tag_delete('delete')
        user_text.tag_add('incorrect', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_config('incorrect', background='red')
        current_indx += 1

    correct_char_label.config(text=f'Correct characters: {char_score}')
    correct_word_counter()
    user_text.config(state=DISABLED)


root = Tk()
user_text = Text(root, wrap=WORD)
user_text.tag_config('center', justify=CENTER)
word_generator = WordGenerator().generate_words(20)
user_text.insert(INSERT, word_generator)
user_text.tag_add('center', '1.0', END)
user_text.config(state=DISABLED)
user_text.place(x=5, y=5)

total_char_count = text_calculator()
current_indx = 1
char_score = 0
word_score = 0
chars_typed = ''

timer_label = Label(root)
timer_label.place(x=5, y=500)
correct_char_label = Label(root)
correct_char_label.place(x=5, y=550)
correct_word_label = Label(root)
correct_word_label.place(x=5, y=600)
character_score_label = Label(root)
character_score_label.place(x=5, y=650)
word_score_label = Label(root)
word_score_label.place(x=5, y=700)

root.geometry('700x900')
root.bind('<KeyPress>', key_press)

root.mainloop()
