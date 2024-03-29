
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *


def check():
    try:
        if ent1.get() :
            kg = ent1.get() 
            gram = int(kg) * 1000
            ent2.insert(INSERT, f"{gram} G")
        else:
            gram = ent2.get()
            kg= int(gram) // 1000
            ent1.insert(INSERT , f"{kg} KG")    
    except ValueError:
            if ent1.get() :
                ent2.insert(INSERT, "error number")
            else:
                ent1.insert(INSERT, "error number")


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\d\jam\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("375x667")
window.configure(bg = "#6E6E6E")
window.title("kilogram to gram ")
window.iconbitmap("x.ico")



canvas = Canvas(
    window,
    bg = "#6E6E6E",
    height = 667,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=check,
    relief="flat"
)
button_1.place(
    x=97.0,
    y=563.0,
    width=174.0,
    height=51.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    184.5,
    242.5,
    image=entry_image_1
)
ent1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font="tahoma 14 bold"
)
ent1.place(
    x=115.0,
    y=219.0,
    width=139.0,
    height=45.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    182.5,
    451.5,
    image=entry_image_2
)
ent2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    font="tahoma 12 bold"
)
ent2.place(
    x=113.0,
    y=426.0,
    width=139.0,
    height=49.0
)

canvas.create_rectangle(
    92.0,
    140.0,
    274.0,
    201.0,
    fill="#FF0000",
    outline=""
)

canvas.create_text(
    113.0,
    149.0,
    anchor="nw",
    text="kilogram  ",
    fill="#FFFFFF",
    font=("HammersmithOne Regular", 32 * -1)
)

canvas.create_rectangle(
    93.0,
    334.0,
    276.0,
    395.02893447875977,
    fill="#FF0000",
    outline=""
)

canvas.create_text(
    132.0,
    334.0,
    anchor="nw",
    text="gram",
    fill="#FFFFFF",
    font=("FrancoisOne Regular", 36 * -1)
)

canvas.create_rectangle(
    0.0,
    0.0,
    375.0,
    96.0,
    fill="#000000",
    outline="")

canvas.create_text(
    69.0,
    18.0,
    anchor="nw",
    text="kilogram to gram ",
    fill="#FF0000",
    font=("FrancoisOne Regular", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
