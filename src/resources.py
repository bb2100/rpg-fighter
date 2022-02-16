class Character:
    
    def __init__(self, name, health, attack, armor):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def __str__(self) -> str:
        return f"Name: {self.name}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"
    
    
    def take_damage(self, damage):
        relative_damage = damage -self.armor
        self.health -= relative_damage
        if self.health < 0: self.health = 0

    def get_attack(self): # Before damage
        return self.attack

    def get_health(self):
        return self.health

    def get_name(self):
        return self.name

class Goblin:
    
    def __init__(self, health, attack, armor, id):
        self.health = health
        self.attack = attack
        self.armor = armor
        self.id = id

    def __str__(self) -> str:
        return f"Goblin #{self.id}\nHealth: {self.health}\nAttack: {self.attack}\nArmor: {self.armor}"
    
    def take_damage(self, damage):
        relative_damage = damage -self.armor
        self.health -= relative_damage
        if self.health < 0: self.health = 0

    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_name(self):
        return f"Goblin #{self.id}"