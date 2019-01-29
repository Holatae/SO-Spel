#Walk in any direction
def walk(directions):
    pass

#Use an object
def use(object):
    pass

#returns all commands that exists
def help():
    pass


def map():
    import func
    f = open("karta.txt", "r")
    karta = f.read()
    print(func.change_char(karta, 5, "*"))
    f.close()


