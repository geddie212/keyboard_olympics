import pyglet, tkinter

pyglet.font.add_file('digital-7.ttf')

root = tkinter.Tk()
MyLabel = tkinter.Label(root, text="test", font=('digital-7', 25), fg='red')
MyLabel.pack()
root.mainloop()
