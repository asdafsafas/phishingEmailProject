from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\lohwx\Desktop\Phishing Detector GUI\assets\notifications")


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
canvas.create_rectangle(
    30.0,
    118.0,
    420.0,
    287.0,
    fill="#F5F5F5",
    outline="")

#to display the total number of suspected phishing emails
canvas.create_text(
    30.0,
    81.0,
    anchor="nw",
    text="3 Emails Detected ",
    fill="#C94949",
    font=("OpenSans Bold", 16 * -1)
)

#to display the subject of the email
canvas.create_text(
    42.0,
    133.0,
    anchor="nw",
    text="Subject: Lorem ipsum dolor",
    fill="#333333",
    font=("OpenSans Semibold", 12 * -1)
)

#to display the body of the email
canvas.create_text(
    42.0,
    162.0,
    anchor="nw",
    text="“body content”",
    fill="#333333",
    font=("OpenSans Semibold", 12 * -1)
)

canvas.create_rectangle(
    41.0,
    197.0,
    408.0,
    198.0,
    fill="#BDBDBD",
    outline="")

canvas.create_text(
    160.0,
    213.0,
    anchor="nw",
    text="Remove this email?",
    fill="#333333",
    font=("OpenSans Semibold", 14 * -1)
)

#to let user decide whether to keep or remove the suspected email
keep_email = PhotoImage(
    file=relative_to_assets("keep email.png"))
button_1 = Button(
    image=keep_email,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("keep email"),
    relief="flat"
)
button_1.place(
    x=82.0,
    y=242.0,
    width=136.0,
    height=30.0
)

remove_email = PhotoImage(
    file=relative_to_assets("remove email.png"))
button_2 = Button(
    image=remove_email,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("remove email"),
    relief="flat"
)
button_2.place(
    x=233.0,
    y=242.0,
    width=136.0,
    height=30.0
)

Logo = PhotoImage(
    file=relative_to_assets("Logo.png"))
image_1 = canvas.create_image(
    111.0,
    45.0,
    image=Logo
)

settings = PhotoImage(
    file=relative_to_assets("settings.png"))
button_3 = Button(
    image=settings,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("settings clicked"),
    relief="flat"
)
button_3.place(
    x=396.0,
    y=33.0,
    width=24.0,
    height=25.0
)

notifications = PhotoImage(
    file=relative_to_assets("notification bell.png"))
button_4 = Button(
    image=notifications,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("notifications clicked"),
    relief="flat"
)
button_4.place(
    x=360.0,
    y=33.0,
    width=24.0,
    height=25.0
)

window.resizable(False, False)
window.mainloop()
