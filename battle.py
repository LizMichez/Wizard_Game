# make sequence for battling, define monster class and variations of the classes
import items
import spells


def battle():
    print("Dun dun duun dun du du dun du du du")


class Monsters:
    def __init__(self, name, ele, gold, health, mana, attacks,
                 mag, stre, defe, spe, acc, luck, intel, heal, drain, drops, des):
        self.name = name
        self.element = ele
        self.gold = gold

        self.health = [health, health]
        self.mana = [mana, mana]
        self.attacks = attacks
        self.stats = {"magic": mag, "strength": stre, "defense": defe, "speed": spe,
                      "accuracy": acc, "luck": luck, "intel": intel, "heal": heal, "drain": drain}
        self.description = des
        self.drops = drops


# ALL MONSTERS NEED ATTACKS
SLIME = Monsters("Slime", "none", 10, 100, 0, [], 0, 10, 3, 5, 5, 0, 1, 0, 10,
                 [items.ROCK1, items.JELLY_C, items.JELLY_S, items.JELLY_G], "An aggressive little ball of jelly")
SLIME_B = Monsters("Slime", "none", 30, 200, 0, [], 0, 20, 5, 4, 5, 5, 5, 0, 30,
                   [items.ROCK2, items.JELLY_S, items.JELLY_G], "A very aggressive big ball of jelly")
CBAT = Monsters("Corrupt Bat", "dark", 5, 75, 50, [], 10, 5, 2, 20, 10, 2, 2, 0, 25,
                [items.B_CLAW, items.B_WING], "A bat that had an encounter with dark magic")
# SWAMP_RAT
# SWAMP_RAT_B
# UNDEAD_1
# UNDEAD_2
# UNDEAD_B
# FSPIRIT
# WSPIRIT
# ESPIRIT
# ASPIRIT
# LSPIRIT
# TROLL
# GIANT
# GIANT_B
# THEIF
# DLIZARD
# DRAGON
# DRAGON_B