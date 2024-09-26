from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\lohwx\Desktop\Phishing Detector GUI\assets\login")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("450x400")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 400,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    205.0,
    114.0,
    anchor="nw",
    text="Login",
    fill="#333333",
    font=("OpenSans Bold", 16 * -1)
)

canvas.create_text(
    108.0,
    142.0,
    anchor="nw",
    text="Select an option below to get started",
    fill="#333333",
    font=("OpenSans Semibold", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("google login.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=115.0,
    y=181.0,
    width=222.0,
    height=45.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("microsoft login.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=115.0,
    y=241.0,
    width=222.0,
    height=45.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("Logo.png"))
image_1 = canvas.create_image(
    111.0,
    45.0,
    image=image_image_1
)

window.resizable(False, False)
window.mainloop()
