# make sequence for battling, define monster class and variations of the classes
import items
import spells
s = spells
i = items


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


# Forest / Basic Monsters
SLIME = Monsters("Slime", "none", 10, 50, 0, [s.STHROW, s.BDSLAM], 0, 5, 3, 5, 5, 0, 1, 0, 10,
                 [i.ROCK1, i.JELLY_C, i.JELLY_S, i.JELLY_G], "An aggressive little ball of jelly")
SLIME_B = Monsters("Slime", "none", 30, 100, 0, [s.STHROW, s.BDSLAM], 0, 15, 5, 4, 5, 5, 5, 0, 30,
                   [i.ROCK2, i.JELLY_S, i.JELLY_G], "A very aggressive big ball of jelly")
CBAT = Monsters("Corrupt Bat", "dark", 5, 75, 50, [s.BITE, s.SCRATCH, s.DARK_A1], 10, 3, 2, 20, 10, 2, 2, 0, 25,
                [i.B_CLAW, i.B_WING], "A bat that had an encounter with dark magic")

# Swamp Monsters
SWAMP_RAT = Monsters("Swamp Rat", "none", 15, 100, 0, [s.BITE, s.SCRATCH], 0, 10, 7, 10, 7, 0, 5, 0, 0,
                     [i.ROCK1, i.R_CLAW, i.R_TAIL], "A large rat that lives mainly in swamps")
SWAMP_RAT_B = Monsters("Swamp Rat", "earth", 45, 200, 50, [s.BITE, s.SCRATCH, s.EARTH_A1], 5, 20, 10, 10, 7, 0, 5, 0, 0,
                       [i.ROCK2, i.R_CLAW, i.R_TAIL], "The leader of a pack of rats that lives in swamps")
UNDEAD_1 = Monsters("Undead", "dark", 50, 150, 50, [s.BITE, s.DARK_A1, s.HIT], 10, 10, 10, 5, 10, 5, 10, 0, 20,
                    [i.ROCK2, i.C_GEM, i.R1],
                    "An moving corpse, it appears to have been reanimated through necromancy")
UNDEAD_2 = Monsters("Undead Archer", "dark", 50, 150, 50, [s.ARROW, s.DARK_A1], 10, 10, 10, 5, 10, 5, 15, 0, 20,
                    [i.ROCK1, i.C_GEM, i.B1],
                    "A moving corpse, it appears to have been reanimated through necromancy")
UNDEAD_3 = Monsters("Undead Sorcerer", "dark", 75, 100, 150, [s.DARK_A1, s.DARK_A2, s.DARK_A3], 20, 5, 2, 5, 10, 10, 15,
                    0, 25, [i.ROCK2, i.C_GEM, i.A1],
                    "The moving corpse of a once dead sorcerer, it's magic has become corrupt")
UNDEAD_B = Monsters("Undead Captain", "dark", 100, 300, 100, [s.STAB, s.DARK_A1, s.DARK_A2], 15, 15, 15, 3, 10, 5, 20,
                    0, 20, [i.ROCK2, i.C_GEM, i.B2], "The reanimated corpse of a long dead adventurer")

# Mountain Monsters
FSPIRIT = Monsters("Fire Spirit", "fire", 75, 200, 150, [s.FIRE_A1, s.FIRE_A2, s.FIRE_H1], 30, 5, 5, 20, 30, 20, 30, 25,
                   0, [i.ROCK1, i.F_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
WSPIRIT = Monsters("Water Spirit", "water", 75, 200, 150, [s.WATER_A1, s.WATER_A2, s.WATER_H1], 30, 5, 5, 20, 30, 20,
                   30, 25, 0, [i.ROCK1, i.W_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
ESPIRIT = Monsters("Earth Spirit", "earth", 75, 200, 150, [s.EARTH_A1, s.EARTH_D1, s.EARTH_A2], 30, 5, 5, 20, 30, 20,
                   30, 25, 0, [i.ROCK1, i.E_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
ASPIRIT = Monsters("Air Spirit", "air", 75, 200, 150, [s.AIR_A1, s.AIR_A2, s.AIR_A3], 30, 5, 5, 20, 30, 20, 30, 25, 0,
                   [i.ROCK1, i.A_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
LSPIRIT = Monsters("Light Spirit", "light", 75, 200, 150, [s.LIGHT_A1, s.LIGHT_H1, s.LIGHT_D1], 30, 5, 5, 20, 30, 20,
                   30, 25, 0, [i.ROCK1, i.L_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
GOBLIN = Monsters("Goblin", "dark", 150, 200, 100, [], 15, 15, 10, 30, 20, 5, 25, 0, 20,
                  [i.ROCK2, i.GEM, i.B1, i.B2, i.A2], "A twisted dark creature with a wicked sense of humor")
GIANT = Monsters("Giant", "none", 200, 300, 0, [s.HIT, s.BDSLAM], 0, 40, 30, 20, 20, 10, 15, 0, 0,
                 [i.ROCK3], "A large, aggressive, humanoid")
GIANT_B = Monsters("Giant Soldier", "none", 300, 400, 0, [s.HIT, s.BDSLAM, s.STAB, s.SLASH], 0, 60, 40, 15, 25, 10, 20,
                   0, 0, [i.ROCK3],
                   "A very large, very aggressive, very armed, humanoid. Who looks angry.")

# Cave Monsters
# TROLL = Monsters("Troll", "none")
# DLIZARD = Monsters("Dragon Lizard", "fire")
# DRAGON = Monsters("Small Dragon", "fire")
#
# # Event Monsters
# THIEF = Monsters("Thief", "none")
# DRAGON_B = Monsters("Azeroth : Light Bringer", "light")

