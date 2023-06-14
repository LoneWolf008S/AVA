import pytz
import datetime

"""
AVA - Advanced Voice Assistant 0.0
© Tejas Joshi 2023
A simple project made by LoneWolf008S for practice and entertainment purposes.

TODO:
• Make and implement a logging system
• Give it audio I/O system
• Try to implement actual AI in some way
• Implement some basic functions
"""

# Variables
tz = pytz.timezone("Asia/Kolkata")
mList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


# Functions
def show_time(now):                        # Shows time in an appended string
    return str(now.hour) + ":" + str(now.minute)


def show_date(now):
    return str(now.day) + " " + mList[(now.month-1)] + ", " + str(now.year)


def user_input_compute(u_inp):              # Processes the user input
    global tz
    if "time" in u_inp:
        c_time = datetime.datetime.now(tz)
        print(show_time(c_time))

    if "date" in u_inp:
        c_time = datetime.datetime.now(tz)
        print(show_date(c_time))


def user_input(text_mode=True):
    if text_mode:
        while True:
            u_val = input(">>> ").lower()
            user_input_compute(u_val)


user_input()
