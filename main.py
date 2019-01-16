import func

options = {
    1 : func.new_game,
    2 : func.load_save,
    3 : func.quit,
}

def start_menu():
    print("Välkommen till SO-Spelet version " + str(func.get_version()) + "\n")
    print("Välj allternativ")
    print("1. Nytt spel")
    print("2. Ladda spel")
    print("3. Avslut")
    options[int(input())]()
    


start_menu()