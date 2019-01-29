import func
import commands

location = 0
options = {
    1 : func.new_game,
    2 : func.load_save,
    3 : func.quit,
    4 : func.cheat,
    5 : func.print_details,
    6 : commands.map,

}

def start_menu():
    #func.delay_print("Välkommen till SO-Spelet version " + str(func.get_version()) + "\n", 0.25)
    print("Välj allternativ")
    print("1. Nytt spel")
    print("2. Ladda spel")
    print("3. Avslut")

    try:
        options[int(input())]()
    except Exception as e:
        pass
    


start_menu()