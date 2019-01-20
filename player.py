name = ""
age = ""
health = 0
money = 0
power = 0
speed = 0
defense_power = 0

class character():
        def __init__(self, power, speed, defense_power):
                self.power = power
                self.speed = speed
                self.defense_power = defense_power
        
        def attack(self ,power_of_enemy, speed_of_enemy, health_of_enemy):
                pass

#def attack(power_of_enemy, speed_of_enemy, health_of_enemy):
 #   pass

def get_attacked(power_of_enemy, speed_of_enemy):
    pass

def block(power_of_enemy, speed_of_enemy):
    if power_of_enemy > defense_power:
        get_attacked(power_of_enemy - defense_power, 0)

def run(speed_of_enemy):
    if speed > speed_of_enemy:
        return True
    else:
        return False

def war():
    pass

def pay(amount):
    global money
    if amount > money:
        return False
    else:
        money = money - amount
        return True

def get_payed(amount):
    global money
    money = money + amount