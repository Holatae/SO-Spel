#All varibles
name = ""
age = ""
health = 0
money = 0
power = 0
speed = 0
defense_power = 0

#'''
#sClass character. This creates a character with power, speed and defense power
#All the characters in the game should be created with this function
#'''
class character():
        #The init function.. creates the character
        def __init__(self, power, speed, defense_power):
                self.power = power
                self.speed = speed
                self.defense_power = defense_power
        
        #atacks a difftent character
        def attack(self ,power_of_enemy, speed_of_enemy, health_of_enemy):
                pass
        
        #Die.. talks for it self
        def die(self):
                pass

#def attack(power_of_enemy, speed_of_enemy, health_of_enemy):
#       pass

def get_attacked(power_of_enemy, speed_of_enemy):
    pass

#It will see if you can block an attack
def block(power_of_enemy, speed_of_enemy):
    if power_of_enemy > defense_power:
        get_attacked(power_of_enemy - defense_power, 0)

#It will se if you could run from an enimy like in pokémon
def run(speed_of_enemy):
    if speed > speed_of_enemy:
        return True
    else:
        return False

#Meny on your team agenst another team.. like Athen vs Sparta 
def war():
    pass

#Pays money. can be used to upgrade wepons
def pay(amount):
    global money
    if amount > money:
        return False
    else:
        money = money - amount
        return True

#If you sell something to a shop
def get_payed(amount):
    global money
    money = money + amount