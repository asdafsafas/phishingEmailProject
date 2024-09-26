
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\lohwx\Desktop\Phishing Detector GUI\assets\settings")


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
    30.0,
    81.0,
    anchor="nw",
    text="Settings",
    fill="#333333",
    font=("OpenSans Bold", 16 * -1)
)

log_out = PhotoImage(
    file=relative_to_assets("log out.png"))
button_1 = Button(
    image=log_out,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("log out"),
    relief="flat"
)
button_1.place(
    x=168.0,
    y=349.0,
    width=113.0,
    height=30.0
)

canvas.create_text(
    30.0,
    227.0,
    anchor="nw",
    text="(if checkbox is ‘OFF’ it will only run upon checking mail)",
    fill="#333333",
    font=("OpenSansHebrew Regular", 11)
)

canvas.create_text(
    30.0,
    290.0,
    anchor="nw",
    text="(if checkbox is 'OFF' it will not auto quarantine detected\n emails suspected of phishing.)",
    fill="#333333",
    font=("OpenSansHebrew Regular", 11)
)

open_email_web = PhotoImage(
    file=relative_to_assets("email web.png"))
button_2 = Button(
    image=open_email_web,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("open email web"),
    relief="flat"
)
button_2.place(
    x=30.0,
    y=123.0,
    width=136.0,
    height=19.0
)

notifications = PhotoImage(
    file=relative_to_assets("notifications.png"))
button_3 = Button(
    image=notifications,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("checkbox clicked"),
    relief="flat"
)
button_3.place(
    x=30.0,
    y=162.0,
    width=150.0,
    height=19.0
)

run_in_background = PhotoImage(
    file=relative_to_assets("run in background.png"))
button_4 = Button(
    image=run_in_background,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("checkbox clicked"),
    relief="flat"
)
button_4.place(
    x=30.0,
    y=201.0,
    width=150.0,
    height=19.0
)

auto_quarantine = PhotoImage(
    file=relative_to_assets("auto quarantine.png"))
button_5 = Button(
    image=auto_quarantine,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("checkbox clicked"),
    relief="flat"
)
button_5.place(
    x=30.0,
    y=263.0,
    width=245.0,
    height=19.0
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
button_6 = Button(
    image=settings,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("settings clicked"),
    relief="flat"
)
button_6.place(
    x=396.0,
    y=33.0,
    width=24.0,
    height=25.0
)

notification_bell = PhotoImage(
    file=relative_to_assets("notification bell.png"))
button_7 = Button(
    image=notification_bell,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("notification bell clicked"),
    relief="flat"
)
button_7.place(
    x=360.0,
    y=33.0,
    width=24.0,
    height=25.0
)

window.resizable(False, False)
window.mainloop()
