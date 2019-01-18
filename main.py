import func

options = {
    1 : func.new_game,
    2 : func.load_save,
    3 : func.quit,
}

def start_menu():
    func.delay_print("Välkommen till SO-Spelet version " + str(func.get_version()) + "\n", 0.25)
    print("Välj allternativ")
    print("1. Nytt spel")
    print("2. Ladda spel")
    print("3. Avslut")

    try:
        options[int(input())]()
    except Exception as e:
        pass
    


start_menu()