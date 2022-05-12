import json
from tkinter import *
from word_generator import WordGenerator
import time
from pathlib import Path
import pyglet

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

char_backup = 0
word_backup = 0

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("build/assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


pyglet.font.add_file('build/assets/digital-7.ttf')
pyglet.font.add_file('build/assets/Poppins-Bold.ttf')
pyglet.font.add_file('build/assets/Poppins-Black.ttf')
pyglet.font.add_file('build/assets/Poppins-Light.ttf')


def text_calculator():
    return len(word_generator)


def stopwatch():
    global start_time
    global finish_time
    global stopwatch_on
    if stopwatch_on:
        timer_label.config(text='{00:10.2f}'.format(time.time() - start_time))
        timer_label.after(1, stopwatch)
    elif not stopwatch_on:
        if finish_time == 0:
            finish_time = time.time()
            timer_label.config(text='{00:10.2f}'.format(finish_time - start_time))


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
        correct_char_score.config(text=f'{char_score}')
        correct_word_score.config(text=f'{word_score}')
        total_char_qty.config(text=f'{total_char_count}')
        total_word_qty.config(text=f'{len(word_g_list)}')
        char_backup = char_score
        word_backup = word_score
    except IndexError:
        correct_char_score.config(text=f'{char_backup}')
        correct_word_score.config(text=f'{word_backup}')
        total_char_qty.config(text=f'{total_char_count}')
        total_word_qty.config(text=f'''{len(word_generator.split(' '))}''')


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
            high_score_cpm_result.config(text=f'{cpm}')
            high_score_wpm_result.config(text=f'{wpm}')
        else:
            high_score_cpm_result.config(text=f'''{data['cpm']}''')
            high_score_wpm_result.config(text=f'''{data['wpm']}''')


def final_scorer():
    global start_time
    global finish_time
    global char_backup
    global word_backup
    character_score_label.config(
        text=f'{round(60 / (finish_time - start_time) * char_backup)}')
    word_score_label.config(text=f'{round(60 / (finish_time - start_time) * word_backup)}')


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
        reset_button['bg'] = '#2c8bb9'
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
        user_text.tag_config('correct', background='#097f06')
        if exact_char.encode('utf-8') == b'\r':
            keyboard_prompt_label.config(text='Try using Space Bar instead of Enter to type faster')
        current_indx += 1

    elif exact_char != word_generator[current_indx] and current_indx != 0 or exact_char == ' ' and current_indx == 0:
        user_text.tag_delete('delete')
        user_text.tag_add('incorrect', f'1.{current_indx}', f'1.{current_indx + 1}')
        user_text.tag_config('incorrect', background='#e41a27')
        current_indx += 1

    elif exact_char != word_generator[current_indx] and current_indx == 0:
        user_text.tag_delete('delete')
        user_text.tag_add('incorrect', f'1.{current_indx}', f'1.{current_indx + 1}')
        user_text.tag_config('incorrect', background='#e41a27')
        current_indx += 1

    if current_indx == total_char_count:
        stopwatch_on = False
        stopwatch()
        scorer()
        final_scorer()
        score_writer()
        reset_button['state'] = 'normal'
        reset_button['bg'] = '#2c8bb9'
        return

    stop_watch_initialise = False
    scorer()

root = Tk()
root.geometry("1920x1080")
root.configure(bg="#FFFFFF")

canvas = Canvas(
    root,
    bg="#FFFFFF",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
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
    global correct_char_score
    global correct_word_score
    global total_char_qty
    global total_word_qty
    global character_score_label
    global word_score_label
    global reset_button
    global timer_label

    user_text.config(state=NORMAL)
    user_text.tag_config('center', justify=CENTER)
    user_text.delete('1.0', END)
    word_generator = WordGenerator().generate_words(100)
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

    score_writer()

    timer_label.config(text='')

    correct_char_score.config(text='0')
    correct_word_score.config(text='0')

    total_char_qty.config(text=f'{len(word_generator)}')
    total_word_qty.config(text=f'''{len(word_generator.split(' '))}''')

    character_score_label.config(text='0')
    word_score_label.config(text='0')

    reset_button['state'] = 'disabled'
    reset_button['bg'] = 'grey'

reset_button = Button(borderwidth=0, highlightthickness=0, command=reset_game, text='RESET', font=('Poppins-Bold', 20))
reset_button.place(x=886.0, y=308.0, width=162.0, height=45.0)
reset_button['bg'] = 'grey'
reset_button['state'] = 'disabled'

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    966.0,
    679.5,
    image=entry_image_1
)

user_text = Text(bd=0, bg="#FFFFFF", highlightthickness=0, font=('Verdana', 20), wrap=WORD)
user_text.tag_config('center', justify=CENTER)
word_generator = WordGenerator().generate_words(100)
user_text.insert(INSERT, word_generator)
user_text.tag_add('center', '1.0', END)
user_text.config(state=DISABLED)

user_text.place(x=113.0, y=576.0, width=1706.0, height=205.0)

total_char_count = text_calculator()
start_time = 0
finish_time = 0
current_indx = 0
char_score = 0
word_score = 0
chars_typed = ''
stopwatch_on = True
stop_watch_initialise = True

high_score_title = Label(root, text='HIGH SCORE', font=('Poppins-Black', 40), fg='white', bg='#252525')
high_score_title.place(x=1475, y=53)

high_score_cpm = Label(root, text='CPM', font=('Poppins-Black', 40), fg='white', bg='#1ea2e3')
high_score_cpm.place(x=1487, y=227)

high_score_wpm = Label(root, text='WPM', font=('Poppins-Black', 40), fg='white', bg='#ea5149')
high_score_wpm.place(x=1665, y=227)

high_score_cpm_result = Label(root, font=('Poppins-Black', 50), fg='white', bg='#1ea2e3')
high_score_cpm_result.place(x=1485, y=320)

high_score_wpm_result = Label(root, font=('Poppins-Black', 50), fg='white', bg='#ea5149')
high_score_wpm_result.place(x=1670, y=320)

score_writer()

timer_label = Label(root, font=('digital-7', 40), fg='#232323', bg='#2c8bb9')
timer_label.place(x=847, y=205)

instructions_label = Label(root, text='Type the words below', font=('Poppins-Light', 40), fg='white', bg='#252525')
instructions_label.place(x=700, y=490)

keyboard_prompt_label = Label(root, font=('Poppins-Light', 20), fg='#252525', bg='white')
keyboard_prompt_label.place(x=650, y=800)

correct_char_text = Label(root, text='CORRECT\nCHARACTERS', font=('Poppins-Black', 15), fg='white', bg='#252525')
correct_char_text.place(x=140, y=50)

correct_word_text = Label(root, text='CORRECT\nWORDS', font=('Poppins-Black', 15), fg='white', bg='#252525')
correct_word_text.place(x=385, y=50)

total_char_text = Label(root, text='TOTAL', font=('Poppins-Black', 15), fg='white', bg='#252525')
total_char_text.place(x=175, y=195)

total_word_text = Label(root, text='TOTAL', font=('Poppins-Black', 15), fg='white', bg='#252525')
total_word_text.place(x=400, y=195)

cpm_label = Label(root, text='CPM', font=('Poppins-Black', 15), fg='white', bg='#252525')
cpm_label.place(x=183, y=322)

wpm_label = Label(root, text='WPM', font=('Poppins-Black', 15), fg='white', bg='#252525')
wpm_label.place(x=410, y=322)

correct_char_score = Label(root, text='0', font=('digital-7', 30), fg='#e41a27', bg='#636363')
correct_char_score.place(x=195, y=115)

correct_word_score = Label(root, text='0', font=('digital-7', 30), fg='#e41a27', bg='#636363')
correct_word_score.place(x=425, y=115)

total_char_qty = Label(root, text=f'{len(word_generator)}', font=('digital-7', 30), fg='#e41a27', bg='#636363')
total_char_qty.place(x=195, y=255)

total_word_qty = Label(root, text=f'''{len(word_generator.split(' '))}''', font=('digital-7', 30), fg='#e41a27',
                       bg='#636363')
total_word_qty.place(x=425, y=255)

character_score_label = Label(root, text='0', font=('digital-7', 30), fg='#e41a27', bg='#636363')
character_score_label.place(x=195, y=375)

word_score_label = Label(root, text='0', font=('digital-7', 30), fg='#e41a27', bg='#636363')
word_score_label.place(x=425, y=375)

logo_text_keyboard = Label(root, text='KEYBOARD', font=('Poppins-Black', 20), fg='white', bg='#285fb5')
logo_text_keyboard.place(x=710, y=885)

logo_text_olympics = Label(root, text='OLYMPICS', font=('Poppins-Black', 20), fg='white', bg='#e41a27')
logo_text_olympics.place(x=1090, y=885)

root.bind('<KeyPress>', key_press)

root.mainloop()
