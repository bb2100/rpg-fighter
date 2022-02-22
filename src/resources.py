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

    def get_attributes(self):
        return self.name, self.health, self.attack, self.armor

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



def save_character(char : Character):
    name, health, attack, armor = char.get_attributes()
    save_string = f"{name}/{health}/{attack}/{armor}\n"
    with open("saved_characters.txt", "a", encoding="utf8") as f:
        f.write(save_string)
        print(f"{name} has been successfully saved.")

def load_characters():
    characters = []
    with open("saved_characters.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            attributes = line.split("/")
            char = Character(attributes[0],
                             attributes[1],
                             attributes[2],
                             attributes[3])
            
            characters.append(char)
    return characters