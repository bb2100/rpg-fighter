from importlib import resources


import resources
from resources import Character, Goblin

if __name__ == "__main__":
    nemy = Character("Nemy", 20, 5, 2)
    goblin_one = Goblin(10, 3, 1)

    print(nemy)
    print()
    print(goblin_one)

    fight_round = 1
    print("=======Fight=======")
    while nemy.get_health() != 0 and goblin_one.get_health != 0:
        print(f"Round {fight_round}")
        nemy_attack = nemy.damage()
        goblin_one.take_damage(nemy_attack)
        if(goblin_one.get_health() ==0):
            print("Goblin has died")
            break
        else:
            print(f"Goblin has {goblin_one.get_health()} hp left.")
            goblin_attack = goblin_one.damage()
            nemy.take_damage(goblin_attack)
            print(f"Nemy has {nemy.get_health()} hp left.")
            if(nemy.get_health() == 0): print("Nemy has died.")
        fight_round += 1
    
    if(nemy.get_health() == 0): print("The Goblin won!")
    else: print("Nemy has won!")