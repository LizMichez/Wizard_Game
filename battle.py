import spells
from random import randint


def battle(player, enemy):
    print("\nYou have encountered a", enemy.name, "!")
    turn = 0
    while player.health[0] > 0 and enemy.health[0] > 0:
        turn += 1
        print("\nYour Stats: health [", player.health[0], "/", player.health[1], "], mana [", player.mana[0],
              "/", player.mana[1], "]\nEnemy Health:", enemy.health[0])

        your_move = player_turn(player, enemy)
        if your_move == "ran":
            break
        if player.health[0] < 0 or enemy.health[0] < 0:
            break
        enemy_turn(player, enemy)

    if player.health[0] <= 0 < enemy.health[0]:  # You die and the enemy is alive
        print("You were defeated and pass out, thankfully some adventurers came by and dragged you back to town")
        gold_loss = int(player.gold/randint(2, 5))
        player.gold -= gold_loss
        print("You lost", gold_loss, "gold.")

    elif enemy.health[0] <= 0 < player.health[0]:  # The enemy dies and you're alive
        print("You defeated the", enemy.name, "!")
        print("You gained", enemy.gold, "gold !")
        player.gold += enemy.gold
        if turn >= 10:
            player.exp_gain(enemy.exp)
        else:
            player.exp_gain(enemy.exp + 11 - turn)
        gained = enemy.drop
        if not gained == "nothing":
            print("You gained", gained.name, "!")
            player.acquire(gained)

    elif enemy.health[0] < 0 > player.health[0]:  # If both of you manage to die
        print("In an incredible display of failure both you and the", enemy.name, "were defeated. \n Thankfully some "
              "adventurers came by and made sure to loot the", enemy.name)
        print("Oh they also dragged you back to town")

    enemy.health[0] = enemy.health[1]
    enemy.mana[0] = enemy.mana[1]


def player_turn(player, enemy):
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
            if player.stats["speed"] > enemy.stats["speed"]:
                print("You got away.")
                return "ran"
            else:
                print("You couldn't escape!")

        if choice == 2:
                while True:
                    print("\nWhat spell will you use?")
                    for x in player.spells:
                        print("   ", player.spells.index(x) + 1, ".", x.name)
                    try:
                        spell = int(input())
                        print(spell)
                        if 0 > spell or spell > len(player.spells):
                            print(len(player.spells))
                            print("....The number has to be an actual spell, try again")
                        else:
                            break
                    except TypeError:
                        print("Enter the NUMBER corresponding to the spell you want to use")
                player.use_spell(player.spells[spell-1], enemy)
                return "spell"

        if choice == 3:
            player.open_inventory()
            # Need to be able to throw stuff

        if choice == 4:
            player.open_stats()

        if choice == 5:
            player.use_attack(spells.HIT, enemy)
            break


def enemy_turn(player, enemy):  # The enemy has three chances to pick an attack that works, otherwise it just chills
    i = 0
    while True:
        i += 1
        move = randint(0, len(enemy.attacks)-1)
        attack = enemy.attacks[move]
        try:  # If it is a spell
            if attack.mana >= enemy.mana[0]:
                enemy.use_spell(attack, player)
                break
        except AttributeError:
            enemy.use_attack(attack, player)
            break
        if i == 3:  # Enemy tries to use an attack that requires too much mana three times
            print("The enemy got distracted")
