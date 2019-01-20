import time
import sys
import player

save_list = []


def change_name(name):
        player.name = name

def save(character):
        f = open("save.txt", "w")
        save_list.append(character.speed)
        save_list.append(character.power)
        save_list.append(character.defense_power)
        for item in save_list:
                f.write(str(item) + ",")
        f.close()


def cheat():
        hej = player.character(1, 2, 1)
        save(hej)
        
        

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
    delay_print("Du vaknar. Du vet inte vart du är\nDu har liggat å sovit länge\nDu måste hitta en väg ut.", 0.1)

def quit():
    pass

def delay_print(words, delay_time):
    for letter in words:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay_time)

def menu(word):
    delay_print(word, 0.1)
    while True:
        input()