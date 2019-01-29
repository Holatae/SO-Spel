import commands
help = ""
use = ""
walk = ""

options = {
    help : commands.help,
    use : commands.use,
    walk : commands.walk,
}

def menu():
    print("Vad vill du göra")
    try:
        options[input()]
    except Exception as e:
        pass


