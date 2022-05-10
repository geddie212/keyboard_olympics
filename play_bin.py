import json
from tkinter import *
from word_generator import WordGenerator
import time
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

char_backup = 0
word_backup = 0

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("build/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def text_calculator():
    return len(word_generator)


def stopwatch():
    global start_time
    global finish_time
    global stopwatch_on
    if stopwatch_on:
        timer_label.config(text='{:10.2f}'.format(time.time() - start_time))
        timer_label.after(1, stopwatch)
    elif not stopwatch_on:
        if finish_time == 0:
            finish_time = time.time()
            timer_label.config(text='{:10.2f}'.format(finish_time - start_time))


def scorer():
    global word_generator
    global chars_typed
    global word_score
    global char_backup
    global word_backup
    try:
        if exact_char.encode('utf-8') != b'\x08':
            chars_typed += exact_char
        elif exact_char.encode('utf-8') == b'\x08':
            chars_typed = chars_typed[:-1]
        char_score = 0
        for i, char in enumerate(chars_typed):
            if char == word_generator[i]:
                char_score += 1
        chars_list = chars_typed.split(' ')
        word_g_list = word_generator.split(' ')
        word_score = 0
        for i, word in enumerate(chars_list):
            if word == word_g_list[i]:
                word_score += 1
        character_score_label.config(text=f'You wrote {char_score}/{total_char_count} characters correctly')
        word_score_label.config(text=f'You wrote {word_score}/{len(word_g_list)} words correctly')
        char_backup = char_score
        word_backup = word_score
    except IndexError:
        character_score_label.config(text=f'You wrote {char_backup}/{total_char_count} characters correctly')
        word_score_label.config(text=f'''You wrote {word_backup}/{len(word_generator.split(' '))} words correctly''')


def score_writer():
    global start_time
    global finish_time
    global char_backup
    global word_backup
    with open('high_score.json', 'r') as file:
        data = json.load(file)
        try:
            cpm = round(60 / (finish_time - start_time) * char_backup)
            wpm = round(60 / (finish_time - start_time) * word_backup)
        except ZeroDivisionError:
            cpm = 0
            wpm = 0
        if cpm > data['cpm'] and wpm > data['wpm']:
            write_data = {
                'cpm': cpm,
                'wpm': wpm
            }
            with open('high_score.json', 'w') as write_file:
                json.dump(write_data, write_file)
            high_score_label.config(text=f'High Score\nCharacters per minute: {cpm}\nWords per minute: {wpm}')
        else:
            high_score_label.config(
                text=f'''High Score\nCharacters per minute: {data['cpm']}\nWords per minute: {data['wpm']}''')


def final_scorer():
    global start_time
    global finish_time
    global char_backup
    global word_backup
    character_score_label.config(
        text=f'You write {round(60 / (finish_time - start_time) * char_backup)} characters per minute')
    word_score_label.config(text=f'You write {round(60 / (finish_time - start_time) * word_backup)} words per minute')


def key_press(event):
    global current_indx
    global total_char_count
    global start_time
    global char_score
    global exact_char
    global word_generator
    global stopwatch_on
    global stop_watch_initialise

    exact_char = event.char

    if current_indx == 0 and stop_watch_initialise == True:
        start_time = time.time()
        stopwatch()

    if current_indx == total_char_count:
        stopwatch_on = False
        stopwatch()
        scorer()
        final_scorer()
        score_writer()
        reset_button['state'] = 'normal'
        return

    if exact_char.encode('utf-8') == b'\x08' and current_indx != 0:
        current_indx -= 1
        user_text.tag_remove('correct', f'1.{current_indx}', f'1.{current_indx + 1}')
        user_text.tag_remove('incorrect', f'1.{current_indx}', f'1.{current_indx + 1}')
        user_text.tag_add('delete', f'1.{current_indx}', f'1.{current_indx + 1}')
        user_text.tag_config('delete', background='white')

    elif exact_char == word_generator[current_indx] or \
            exact_char.encode('utf-8') == b'\r' and word_generator[current_indx] == ' ':
        user_text.tag_delete('delete')
        user_text.tag_add('correct', f'1.{current_indx}', f'1.{current_indx + 1}')
        user_text.tag_config('correct', background='green')
        if exact_char.encode('utf-8') == b'\r':
            space_bar_label.config(text='Try using Space Bar instead of Enter to type faster')
        current_indx += 1

    elif exact_char != word_generator[current_indx] and current_indx != 0 or exact_char == ' ' and current_indx == 0:
        user_text.tag_delete('delete')
        user_text.tag_add('incorrect', f'1.{current_indx}', f'1.{current_indx + 1}')
        user_text.tag_config('incorrect', background='red')
        current_indx += 1

    elif exact_char != word_generator[current_indx] and current_indx == 0:
        user_text.tag_delete('delete')
        user_text.tag_add('incorrect', f'1.{current_indx}', f'1.{current_indx + 1}')
        user_text.tag_config('incorrect', background='red')
        current_indx += 1

    if current_indx == total_char_count:
        stopwatch_on = False
        stopwatch()
        scorer()
        final_scorer()
        score_writer()
        reset_button['state'] = 'normal'
        return

    stop_watch_initialise = False
    scorer()


def reset_game():
    global char_backup
    global word_backup
    global total_char_count
    global start_time
    global finish_time
    global current_indx
    global char_score
    global word_score
    global chars_typed
    global stopwatch_on
    global stop_watch_initialise
    global word_generator

    user_text.config(state=NORMAL)
    user_text.tag_config('center', justify=CENTER)
    user_text.delete('1.0', END)
    word_generator = WordGenerator().generate_words(5)
    user_text.insert(INSERT, word_generator)
    user_text.tag_add('center', '1.0', END)
    user_text.config(state=DISABLED)

    char_backup = 0
    word_backup = 0
    total_char_count = text_calculator()
    start_time = 0
    finish_time = 0
    current_indx = 0
    char_score = 0
    word_score = 0
    chars_typed = ''
    stopwatch_on = True
    stop_watch_initialise = True

    space_bar_label.config(text='')

    high_score_label = Label(root)
    score_writer()
    high_score_label.place(x=5, y=470)

    timer_label.config(text='')

    correct_char_label.config(text='')

    correct_word_label.config(text='')

    character_score_label.config(text='')

    word_score_label.config(text='')


root = Tk()
root.geometry("1920x1080")
root.configure(bg = "#FFFFFF")

canvas = Canvas(
    root,
    bg = "#FFFFFF",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    960.0,
    540.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    967.0,
    210.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    321.0,
    241.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    1642.0,
    85.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1642.0,
    321.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    967.0,
    677.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    967.0,
    920.0,
    image=image_image_7
)


canvas.create_rectangle(
    124.0,
    106.0,
    291.0,
    176.0,
    fill="#636363",
    outline="")

canvas.create_rectangle(
    351.0,
    106.0,
    518.0,
    176.0,
    fill="#636363",
    outline="")

canvas.create_rectangle(
    124.0,
    241.0,
    291.0,
    311.0,
    fill="#636363",
    outline="")

canvas.create_rectangle(
    351.0,
    241.0,
    518.0,
    311.0,
    fill="#636363",
    outline="")

canvas.create_rectangle(
    124.0,
    364.0,
    291.0,
    434.0,
    fill="#636363",
    outline="")

canvas.create_rectangle(
    351.0,
    364.0,
    518.0,
    434.0,
    fill="#636363",
    outline="")


canvas.create_rectangle(
    1474.0,
    225.0,
    1626.0,
    295.0,
    fill="#1EA2E3",
    outline="")

canvas.create_rectangle(
    1474.0,
    309.0,
    1626.0,
    416.0,
    fill="#1EA2E3",
    outline="")

canvas.create_rectangle(
    1658.0,
    225.0,
    1810.0,
    295.0,
    fill="#EA5149",
    outline="")

canvas.create_rectangle(
    1658.0,
    309.0,
    1810.0,
    416.0,
    fill="#EA5149",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
reset_button = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
reset_button.place(
    x=886.0,
    y=308.0,
    width=162.0,
    height=45.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    966.0,
    679.5,
    image=entry_image_1
)
user_text = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)

user_text.tag_config('center', justify=CENTER)
word_generator = WordGenerator().generate_words(5)
user_text.insert(INSERT, word_generator)
user_text.tag_add('center', '1.0', END)
user_text.config(state=DISABLED)

user_text.place(
    x=113.0,
    y=576.0,
    width=1706.0,
    height=205.0
)


total_char_count = text_calculator()
start_time = 0
finish_time = 0
current_indx = 0
char_score = 0
word_score = 0
chars_typed = ''
stopwatch_on = True
stop_watch_initialise = True

space_bar_label = Label(root)
space_bar_label.place(x=5, y=450)

high_score_label = Label(root)
score_writer()
high_score_label.place(x=1519, y=55)

timer_label = Label(root)
timer_label.place(x=5, y=530)

correct_char_label = Label(root)
correct_char_label.place(x=5, y=550)

correct_word_label = Label(root)
correct_word_label.place(x=5, y=600)

character_score_label = Label(root)
character_score_label.place(x=5, y=650)

word_score_label = Label(root)
word_score_label.place(x=5, y=700)

reset_button = Button(root, text='reset', command=reset_game)
reset_button.place(x=5, y=750)
reset_button['state'] = 'disabled'


root.bind('<KeyPress>', key_press)

root.mainloop()
