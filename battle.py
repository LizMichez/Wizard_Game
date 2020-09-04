from random import randint

import player
import spells

baddie = ""  # for external reference to enemy


def battle(you, enemy):
    print("\nYou have encountered a", str(enemy.name) + "!")
    player.state = player.states[1]
    global baddie
    baddie = enemy
    turn = 0
    while you.health[0] > 0 and enemy.health[0] > 0:
        turn += 1
        print("\nYour Stats: health [", you.health[0], "/", you.health[1], "], mana [", you.mana[0],
              "/", you.mana[1], "]\nEnemy Health:", enemy.health[0])

        your_move = player_turn(you, enemy)
        if your_move == "ran":
            break
        if you.health[0] < 0 or enemy.health[0] < 0:
            break
        enemy_turn(you, enemy)

    if you.health[0] <= 0 < enemy.health[0]:  # You die and the enemy is alive
        print("You were defeated and pass out, thankfully some adventurers came by and dragged you back to town")
        gold_loss = int(you.gold/randint(2, 5))
        you.gold -= gold_loss
        print("You lost", gold_loss, "gold.")

    elif enemy.health[0] <= 0 < you.health[0]:  # The enemy dies and you're alive
        print("You defeated the", enemy.name, "!")
        print("You gained", enemy.gold, "gold!")
        you.gold += enemy.gold
        gained = enemy.drop()
        if not gained == "nothing":
            for x in gained:
                you.acquire(x)
        if turn >= 10:
            you.exp_gain(enemy.exp)
        else:
            you.exp_gain(enemy.exp + 10 - turn)

    elif enemy.health[0] < 0 > you.health[0]:  # If both of you manage to die
        print("In an incredible display of failure both you and the", enemy.name, "were defeated. \n Thankfully some "
              "adventurers came by and made sure to loot the", enemy.name)
        print("Oh they also dragged you back to town")

    enemy.health[0] = enemy.health[1]
    enemy.mana[0] = enemy.mana[1]
    player.state = player.states[4]


def player_turn(you, enemy):
    while True:
        while True:
            try:
                choice = int(input("You can:\n   1.Run\n   2.Use a spell\n   "
                                   "3.Open Inventory\n   4.View Stats\n   5.Hit it\nWhat do you choose? "))
                if choice not in range(1, 6):
                    print("Please enter a valid input, that means a number, from 1 to 5, it's not hard")
                else:
                    break
            except TypeError:
                print("You need to enter a number, why is this so hard?")

        if choice == 1:
            if you.stats["speed"] > enemy.stats["speed"]:
                print("You got away.")
                return "ran"
            else:
                print("You couldn't escape!")

        if choice == 2:
            while True:
                print("\nWhat spell will you use?")
                for x in you.spells:
                    print("   ", you.spells.index(x) + 1, ".", x.name)
                try:
                    spell = int(input())
                    if 0 > spell or spell > len(you.spells):
                        print(len(you.spells))
                        print("....The number has to be an actual spell, try again")
                    else:
                        break
                except (TypeError, ValueError):
                    print("Enter the NUMBER corresponding to the spell you want to use")
            you.use_spell(you.spells[spell-1], enemy)
            return "spell"

        if choice == 3:
            bag = you.open_inventory()
            if bag == "yeet":
                break

        if choice == 4:
            you.open_stats()

        if choice == 5:
            you.use_attack(spells.HIT, enemy)
            break


def enemy_turn(you, enemy):  # The enemy has three chances to pick an attack that works, otherwise it just chills
    i = 0
    while True:
        i += 1
        move = randint(0, len(enemy.attacks)-1)
        attack = enemy.attacks[move]
        try:  # If it is a spell
            if attack.mana >= enemy.mana[0]:
                enemy.use_spell(attack, you)
                break
        except AttributeError:
            enemy.use_attack(attack, you)
            break
        if i == 3:  # Enemy tries to use an attack that requires too much mana three times
            print("The enemy got distracted")


def encounter(you, animal):  # For killing animals
    print("\nYou have encountered a", str(animal.name) + "!")
    player.state = player.states[1]

    print("\nYour Stats: health [", you.health[0], "/", you.health[1], "], mana [", you.mana[0],
          "/", you.mana[1], "]\nAnimal Health:", animal.health[0])

    your_move = player_turn(you, animal)

    if animal.health[0] <= 0:  # The enemy dies and you're alive
        print("You defeated the", animal.name, "!")
        gained = animal.drop()
        for x in gained:
            you.acquire(x)
    elif your_move == "ran":
        pass
    else:
        print("The animal escaped.")

    animal.health[0] = animal.health[1]
    player.state = player.states[4]
