import random
from tkinter import *
from word_generator import WordGenerator


def text_calculator():
    return len(user_text.get('1.0', END))


def key_press(event):
    global current_indx
    global total_char_count
    user_text.config(state=NORMAL)
    game_char = user_text.get(f'1.{current_indx - 1}', f'1.{current_indx}')
    if event.char.encode('utf-8') == b'\x08' and current_indx != 1:
        current_indx -= 1
        user_text.tag_add('delete', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_config('delete', background='white')
    elif event.char.encode('utf-8') == b'\r' and game_char == ' ':
        user_text.tag_add('correct', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_config('correct', background='green')
        print('Try using the spacebar instead of enter for the words')
        current_indx += 1
    elif game_char == event.char:
        user_text.tag_delete('delete')
        user_text.tag_add('correct', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_config('correct', background='green')
        current_indx += 1
    elif game_char != event.char or event.char.encode('utf-8') != b'\r' and game_char != ' ':
        user_text.tag_delete('delete')
        user_text.tag_add('incorrect', f'1.{current_indx - 1}', f'1.{current_indx}')
        user_text.tag_config('incorrect', background='red')
        current_indx += 1
    elif current_indx + 1 == total_char_count:
        print('Game Over')
        user_text.config(state=DISABLED)
        current_indx += 1
        return
    user_text.config(state=DISABLED)


root = Tk()
user_text = Text(root, wrap=WORD)
user_text.tag_config('center', justify=CENTER)
user_text.insert(INSERT, WordGenerator().generate_words(50))
user_text.tag_add('center', '1.0', END)
user_text.config(state=DISABLED)
total_char_count = text_calculator()
current_indx = 1

user_text.place(x=5, y=5)
root.geometry('700x300')
root.bind('<KeyPress>', key_press)

root.mainloop()
