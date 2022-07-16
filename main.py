from tkinter import *
from PIL import ImageTk, Image
from scrape import ScrapeFollowers

# Colors used
PINK = '#fb114d'
TEXT_COLOR = '#4a4949'
FIELDS_COLOR = '#586365'
CIRCLE_COLOR = '#c4c4c4'

FONT = 'Inter'

ABOUT_TEXT = 'The application uses a username and password,\n' \
             'to automatically check that all the friends you follow have ' \
             'returned the following.\nYou need to have the Chrome browser installed to run the application. \n' \
             'Application will open the browser and navigate to your profile, and check followers. \n' \
             'After that you will get .csv file whit names of users who do not follow you back.\n' \
             '\nYou use this app on your' \
             ' own responsibility.'

followers = ScrapeFollowers()


# close window after scrape
def destroy_window():
    window.destroy()


# function for start scraping
def call():
    username = input_username.get()
    password = input_password.get()
    followers_num = followers_number.get()
    following_num = following_number.get()
    followers.scrape(username, password, followers_num, following_num)


# info window
def about_window():
    info_window = Tk()
    info_window.title("About")
    info_canvas = Canvas(info_window, width=600, height=400, bg='white')
    info_title = Label(info_window, text="About", font=(FONT, 18, 'italic'), fg=PINK, bg='white', justify=CENTER)
    info_text = Label(info_window, text=ABOUT_TEXT, font=(FONT, 12, 'italic'),
                      fg=TEXT_COLOR, bg='white', justify=CENTER)
    info_text.place(x=20, y=100)
    info_title.place(x=260, y=10)
    info_canvas.pack()


# main app visualization
window = Tk()
window.title("Followers checker")
window.resizable(False, False)
canvas = Canvas(width=1200, height=800, bg='white')

canvas.pack()

background_image = Image.open("../Instagram photo.jpg")
resized_image = background_image.resize((600, 800), resample=Image.Resampling.LANCZOS)
canvas.image = ImageTk.PhotoImage(resized_image)
canvas.create_image(0, 0, image=canvas.image, anchor='nw')

line_image = Image.open('../Vector 1Line.png')
canvas.line_image = ImageTk.PhotoImage(line_image)
canvas.create_image(820, 90, image=canvas.line_image)

circle_image = Image.open('../circle.png')
canvas.circle_image = ImageTk.PhotoImage(circle_image)
canvas.create_image(1160, 380, image=canvas.circle_image)

icon_follower = Image.open('../follower.png')
canvas.icon_follower = ImageTk.PhotoImage(icon_follower)
canvas.create_image(690, 170, image=canvas.icon_follower)

icon_info = Image.open('../info.png')
icon_info_resize = icon_info.resize((31, 41), resample=Image.Resampling.LANCZOS)
canvas.icon_info = ImageTk.PhotoImage(icon_info_resize)
img_label = Label(image=canvas.icon_info)
info_button = Button(canvas, image=canvas.icon_info, bg='white', borderwidth=0, command=about_window)
info_button.place(x=1162, y=740)


title = Label(text='Follower Checker', font=(FONT, 30, 'italic'), fg=TEXT_COLOR, bg='white')
title.place(x=660, y=29)

username_text = Label(text='Instagram Name:', font=(FONT, 20, 'italic'), fg=TEXT_COLOR, bg='white')
username_text.place(x=667, y=250)

password_text = Label(text='Instagram Password:', font=(FONT, 20, 'italic'), fg=TEXT_COLOR, bg='white')
password_text.place(x=667, y=398)

followers_following_number = Label(text='Followers/Following Num:', font=(FONT, 20, 'italic'), fg=TEXT_COLOR, bg='white')
followers_following_number.place(x=667, y=546)

backslash = Label(text='/', font=(FONT, 20, 'italic'), fg=TEXT_COLOR, bg='white')
backslash.place(x=758, y=590)

about_text = Label(text='About', font=(FONT, 16, 'italic'), fg=TEXT_COLOR, bg='white')
about_text.place(x=1095, y=750)


input_username = Entry(bg=FIELDS_COLOR, bd=0, font=(FONT, 18, 'italic'), fg='white')
input_username.place(width=335, height=45, x=667, y=291)

followers_number = Entry(bg=FIELDS_COLOR, bd=0, font=(FONT, 18, 'italic'), fg='white')
followers_number.place(width=88, height=45, x=667, y=587)

following_number = Entry(bg=FIELDS_COLOR, bd=0, font=(FONT, 18, 'italic'), fg='white')
following_number.place(width=88, height=45, x=777, y=587)

input_password = Entry(bg=FIELDS_COLOR, bd=0, font=(FONT, 18, 'italic'), fg='white', show="*")
input_password.place(width=335, height=45, x=667, y=439)

check_button = Button(text='Check Now', font=(FONT, 20, 'italic'), fg='white', bg=PINK, highlightthickness=0, bd=0,
                      activebackground=CIRCLE_COLOR, command=lambda: [call(), destroy_window()])
check_button.place(width=200, height=50, x=667, y=702)


window.mainloop()
