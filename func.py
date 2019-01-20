import time
import sys
import player


save_list = []

#Changes the name on the charater that is loaded
def change_name(name):
        player.name = name

#Save your current character into save.txt
def save(character):
        f = open("save.txt", "w")
        save_list.append(character.speed)
        save_list.append(character.power)
        save_list.append(character.defense_power)
        for item in save_list:
                f.write(str(item) + ",")
        f.close()

#Just for testing :)
def cheat():
        import main
        hej = player.character(1, 2, 1)
        save(hej)
        main.start_menu()
        
#Prints stats for loaded character .. For testing
def print_details():
        character = load_save()
        print(str(character.speed) + str(character.power))
        
        
#Loads savefile
def load_save():
    f = open("save.txt", "r")
    character_stats = f.read().split(",")
    return player.character(character_stats[0], character_stats[1], character_stats[2])


def move_forward():
    pass

def move_left():
    pass

def move_right():
    pass

def move_back():
    pass

#Returns game version
def get_version():
    return 0.1

#Starts a new game, Does NOT save
def new_game():
    delay_print("Du vaknar. Du vet inte vart du är\nDu har liggat å sovit länge\nDu måste hitta en väg ut.", 0.1)

#Quits the game
def quit():
    pass

#Make character appere 1 by 1. It's cool
def delay_print(words, delay_time):
    for letter in words:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay_time)

#Moved to menu.py
def menu(word):
    delay_print(word, 0.1)
    while True:
        input()