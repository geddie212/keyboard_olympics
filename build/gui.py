
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1920x1080")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
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
    973.0,
    image=image_image_7
)

canvas.create_text(
    150.0,
    47.99999999999999,
    anchor="nw",
    text="CORRECT \nCHARACTERS",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    377.0,
    47.99999999999999,
    anchor="nw",
    text="CORRECT \nWORDS",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
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

canvas.create_text(
    150.0,
    195.0,
    anchor="nw",
    text="TOTAL",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    377.0,
    195.0,
    anchor="nw",
    text="TOTAL",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
)

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

canvas.create_text(
    150.0,
    326.0,
    anchor="nw",
    text="CPM",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
)

canvas.create_text(
    377.0,
    323.0,
    anchor="nw",
    text="WPM",
    fill="#FFFFFF",
    font=("Poppins Bold", 16 * -1)
)

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

canvas.create_text(
    1519.0,
    54.99999999999999,
    anchor="nw",
    text="HIGH SCORE",
    fill="#FFFFFF",
    font=("Poppins Black", 40 * -1)
)

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

canvas.create_text(
    1502.0,
    232.0,
    anchor="nw",
    text="CPM",
    fill="#FFFFFF",
    font=("Poppins Black", 40 * -1)
)

canvas.create_text(
    1531.0,
    322.0,
    anchor="nw",
    text="0",
    fill="#FFFFFF",
    font=("Poppins Black", 55 * -1)
)

canvas.create_text(
    1715.0,
    321.0,
    anchor="nw",
    text="0",
    fill="#FFFFFF",
    font=("Poppins Black", 55 * -1)
)

canvas.create_text(
    1679.0,
    233.0,
    anchor="nw",
    text="WPM",
    fill="#FFFFFF",
    font=("Poppins Black", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=886.0,
    y=308.0,
    width=162.0,
    height=45.0
)

canvas.create_text(
    867.0,
    204.0,
    anchor="nw",
    text="00:00",
    fill="#000000",
    font=("DigitalNumbers Regular", 50 * -1)
)

canvas.create_text(
    623.0,
    496.0,
    anchor="nw",
    text="Type the words below",
    fill="#FFFFFF",
    font=("Poppins Bold", 40 * -1)
)

canvas.create_text(
    124.0,
    584.0,
    anchor="nw",
    text="Lorem Ipsum etc etc etc etc",
    fill="#000000",
    font=("Verdana", 40 * -1)
)

canvas.create_text(
    565.0,
    803.0,
    anchor="nw",
    text="keyboard text",
    fill="#000000",
    font=("Poppins Regular", 40 * -1)
)

canvas.create_text(
    705.0,
    934.0,
    anchor="nw",
    text="KEYBOARD",
    fill="#FFFFFF",
    font=("Poppins Bold", 30 * -1)
)

canvas.create_text(
    1083.0,
    934.0,
    anchor="nw",
    text="OLYMPICS",
    fill="#FFFFFF",
    font=("Poppins Bold", 30 * -1)
)

canvas.create_text(
    137.0,
    117.0,
    anchor="nw",
    text="0",
    fill="#EA5149",
    font=("DigitalNumbers Regular", 35 * -1)
)

canvas.create_text(
    364.0,
    116.0,
    anchor="nw",
    text="0",
    fill="#EA5149",
    font=("DigitalNumbers Regular", 35 * -1)
)

canvas.create_text(
    137.0,
    251.0,
    anchor="nw",
    text="0",
    fill="#EA5149",
    font=("DigitalNumbers Regular", 35 * -1)
)

canvas.create_text(
    364.0,
    250.0,
    anchor="nw",
    text="0",
    fill="#EA5149",
    font=("DigitalNumbers Regular", 35 * -1)
)

canvas.create_text(
    137.0,
    376.0,
    anchor="nw",
    text="0",
    fill="#EA5149",
    font=("DigitalNumbers Regular", 35 * -1)
)

canvas.create_text(
    364.0,
    375.0,
    anchor="nw",
    text="0",
    fill="#EA5149",
    font=("DigitalNumbers Regular", 35 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    966.0,
    679.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=113.0,
    y=576.0,
    width=1706.0,
    height=205.0
)
window.resizable(False, False)
window.mainloop()