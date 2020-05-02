import player
import monsters


def battle(player, enemy):
    print("You have encountered a", enemy.name, "!")
    while player.health[0] and enemy.health[0] > 0:
        print("Your Stats:    health [", player.health[0], "/", player.health[1], "] mana    [", player.mana[0],
              "/", player.mana[1], "]\nEnemy Health:", enemy.health[0])


def player_turn(player, enemy):
    while True:
        while True:
            choice = input("Will you?\n   1.Run\n   2.Use a spell\n   3.Open Inventory\n   4.View Stats\n   5.Hit it")
            if choice not in range(1, 6):
                print("Please enter a valid input, that means a number, from 1 to 5, it's not hard")
            else:
                break

        if choice == 1:
            if player.stats["speed"] > enemy.stats["speed"]:
                print("You got away.")
                return "ran"
            else:
                print("You couldn't escape!")

        if choice == 2:
            while True:
                print("What spell will you use?")
                for x in player.spells:
                    print("   ", player.spells.index(x) + 1, ".", x.name)
                while True:
                    try:
                        spell = int(input())
                        break
                    except TypeError:
                        print("Enter the number corresponding to the spell you want to use")
                if spell not in range(1, len(player.spells)):
                        print("....The number has to be an actual spell, try again")
                else:
                    break
            player.use_spell(player.spells[spell-1], enemy)


def enemy_turn():
    print("rawr")
