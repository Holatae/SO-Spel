import time
import sys

def change_name(name):
    pass

def save(slot):
    pass

def load_save(slot):
    pass

def move_forward():
    pass

def move_left():
    pass

def move_right():
    pass

def move_back():
    pass

def get_version():
    return 0.1

def new_game():
    f = open("Begining.txt", "r")
    print(f.readlines())
    words = f.readlines()
    words.join()
    delay_print(f.readlines(), 0.25)

def quit():
    pass

def delay_print(words, delay_time):
    for letter in words:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay_time)