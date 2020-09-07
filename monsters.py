# make sequence for battling, define monster class and variations of the classes
import items
import spells
from random import randint
s = spells
it = items


class Animals:
    def __init__(self, name, health, ele, defe, spe, luck, intel, drops, des):
        self.name = name  # str
        self.element = ele  # str
        self.health = [health, health]  # int
        self.stats = {"defense": defe, "speed": spe, "luck": luck, "intel": intel}
        self.des = des  # str
        self.drops = drops  # array

    defBoost = 0

    def drop(self):
        items_dropped = []
        option = randint(0, len(self.drops)-1)
        if option == 3:
            items_dropped = self.drops
        else:
            items_dropped.append(self.drops[option])
        return items_dropped


class Monsters:
    def __init__(self, name, ele, gold, exp, health, mana, attacks,
                 mag, stre, defe, spe, acc, luck, intel, heal, drain, drops, des):
        self.name = name  # str
        self.element = ele  # str
        self.gold = gold  # int

        self.exp = exp  # int

        self.health = [health, health]  # int
        self.mana = [mana, mana]  # int
        self.attacks = attacks  # array
        self.stats = {"magic": mag, "strength": stre, "defense": defe, "speed": spe,
                      "accuracy": acc, "luck": luck, "intel": intel, "heal": heal, "drain": drain}  # ints
        self.description = des  # str
        self.drops = drops  # array

    defBoost = 0

    def restore(self, lestat, amount, prints):  # Restore some health or mana without going over the max
        lestat[0] += amount
        if lestat[0] > lestat[1]:
            lestat[0] = lestat[1]
            if prints:
                print("The enemy now has full", lestat)
        else:
            if prints:
                print("The enemy restored", amount, lestat)

    def use_spell(self, spell, player):  # NOT DONE
        print("The enemy cast", spell.name, "!")
        if self.mana < spell.mana:
            print("It failed")
            return
        self.mana -= spell.mana
        if spell.base_dam > 0:  # Attack section
            hit = randint(0, 101)
            if hit < 35 - int(self.stats["accuracy"]*0.5):
                print("It missed")
            elif hit > 90 - int(self.stats["luck"]*0.5):
                damage = spell.base_dam + self.stats["magic"]
                player.health[0] -= damage
                print("It did", damage, "damage")
                self.restore(self.health, int(damage * 0.01 * (self.stats["drain"]+spell.drain)), False)
            else:
                damage = spell.base_dam + self.stats["magic"] - player.defBoost
                if damage > 0:
                    player.health[0] -= damage
                    print("It did", damage, "damage")
                    self.restore(self.health, int(damage*0.01*(self.stats["drain"]+spell.drain)), False)
                else:
                    print("The enemy defended against the attack, it did no damage")

        if spell.healing > 0:  # Healing section
            self.health += spell.healing + self.stats["heal"]
            print("The enemy restored", spell.healing + self.stats["heal"], "health.")

        if spell.recoil > 0:  # Recoil section
            if spell.recoil - int(0.5*self.stats["intel"]) > 0:
                self.health[0] -= spell.recoil - self.stats["intel"]
                print("The recoil did", spell.recoil - self.stats["intel"], "damage to the opponent")
            else:
                print("The enemy avoided the recoil")

        if spell.base_def > 0:  # Defense section
            self.defBoost += spell.base_def + self.stats["defense"]

    def use_attack(self, attack, enemy):
        print("The enemy used", attack.name, "!")
        damage = attack.damage + int(0.5*self.stats["strength"]) - enemy.defBoost
        if damage > 0:
            enemy.health[0] -= damage
            print("You took", damage, "damage")
        else:
            print("You defended against the attack, it did no damage")

        if attack.defense > 0:  # Defense section
            self.defBoost += attack.defense + self.stats["defense"]

        if attack.recoil > 0:  # Recoil section
            if attack.recoil - int(0.5*self.stats["intel"]) > 0:
                self.health[0] -= attack.recoil - self.stats["intel"]
                print("The enemy took", attack.recoil - self.stats["intel"], "damage from recoil!")
            else:
                print("The enemy was able to avoid the recoil")

    def drop(self):
        items_dropped = []
        for x in self.drops:
            if randint(0, self.drops.index(x)*10) <= len(self.drops) - self.drops.index(x):
                items_dropped.append(x)
        if len(items_dropped) == 0:
            return "nothing"
        else:
            return items_dropped


# Forest / Basic Monsters
SLIME = Monsters("Slime", "none", 10, 10, 50, 0, [s.STHROW, s.BDSLAM], 0, 5, 3, 5, 5, 0, 1, 0, 10,
                 [it.ROCK1, it.JELLY_C, it.JELLY_S, it.JELLY_G], "An aggressive little ball of jelly")
SLIME_B = Monsters("Slime", "none", 30, 20, 100, 0, [s.STHROW, s.BDSLAM], 0, 15, 5, 4, 5, 5, 5, 0, 30,
                   [it.ROCK2, it.JELLY_S, it.JELLY_G], "A very aggressive big ball of jelly")
CBAT = Monsters("Corrupt Bat", "dark", 5, 15, 75, 50, [s.BITE, s.SCRATCH, s.DARK_A1], 10, 3, 2, 20, 10, 2, 2, 0, 25,
                [it.B_CLAW, it.B_WING], "A bat that had an encounter with dark magic")

# Swamp Monsters
SWAMP_RAT = Monsters("Swamp Rat", "none", 15, 20, 100, 0, [s.BITE, s.SCRATCH], 0, 10, 7, 10, 7, 0, 5, 0, 0,
                     [it.ROCK1, it.R_CLAW, it.R_TAIL], "A large rat that lives mainly in swamps")
SWAMP_RAT_B = Monsters("Swamp Rat", "earth", 45, 40, 200, 50, [s.BITE, s.SCRATCH, s.EARTH_A1], 5, 20, 10, 10, 7, 0, 5,
                       0, 0, [it.ROCK2, it.R_CLAW, it.R_TAIL], "The leader of a pack of rats that lives in swamps")
UNDEAD_1 = Monsters("Undead", "dark", 50, 25, 150, 50, [s.BITE, s.DARK_A1, s.HIT], 10, 10, 10, 5, 10, 5, 10, 0, 20,
                    [it.ROCK2, it.C_GEM, it.RNG1],
                    "An moving corpse, it appears to have been reanimated through necromancy")
UNDEAD_2 = Monsters("Undead Archer", "dark", 50, 25, 150, 50, [s.ARROW, s.DARK_A1], 10, 10, 10, 5, 10, 5, 15, 0, 20,
                    [it.ROCK1, it.C_GEM, it.BR1],
                    "A moving corpse, it appears to have been reanimated through necromancy")
UNDEAD_3 = Monsters("Undead Sorcerer", "dark", 75, 30, 100, 150, [s.DARK_A1, s.DARK_A2, s.DARK_A3], 20, 5, 2, 5, 10, 10,
                    15, 0, 25, [it.ROCK2, it.C_GEM, it.AM1],
                    "The moving corpse of a once dead sorcerer, it's magic has become corrupt")
UNDEAD_B = Monsters("Undead Captain", "dark", 100, 50, 300, 100, [s.STAB, s.DARK_A1, s.DARK_A2], 15, 15, 15, 3, 10, 5,
                    20, 0, 20, [it.ROCK2, it.C_GEM, it.BR2], "The reanimated corpse of a long dead adventurer")

# Mountain Monsters
FSPIRIT = Monsters("Fire Spirit", "fire", 75, 40, 200, 150, [s.FIRE_A1, s.FIRE_A2, s.FIRE_H1], 30, 5, 5, 20, 30, 20, 30,
                   25, 0, [it.ROCK1, it.F_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
WSPIRIT = Monsters("Water Spirit", "water", 75, 40, 200, 150, [s.WATER_A1, s.WATER_A2, s.WATER_H1], 30, 5, 5, 20, 30,
                   20, 30, 25, 0, [it.ROCK1, it.W_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
ESPIRIT = Monsters("Earth Spirit", "earth", 75, 40, 200, 150, [s.EARTH_A1, s.EARTH_D1, s.EARTH_A2], 30, 5, 5, 20, 30,
                   20, 30, 25, 0, [it.ROCK1, it.E_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
ASPIRIT = Monsters("Air Spirit", "air", 75, 40, 200, 150, [s.AIR_A1, s.AIR_A2, s.AIR_A3], 30, 5, 5, 20, 30, 20, 30, 25,
                   0, [it.ROCK1, it.A_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
LSPIRIT = Monsters("Light Spirit", "light", 75, 40, 200, 150, [s.LIGHT_A1, s.LIGHT_H1, s.LIGHT_D1], 30, 5, 5, 20, 30,
                   20, 30, 25, 0, [it.ROCK1, it.L_GEM],
                   "A being made from pure mana, thought to be the spirit of an ancient mage")
GOBLIN = Monsters("Goblin", "dark", 150, 50, 200, 100, [s.SCRATCH, s.SLASH, s.DARK_A3], 15, 15, 10, 30, 20, 5, 25, 0,
                  20, [it.ROCK2, it.GEM, it.BR1, it.BR2, it.AM2], "A twisted dark thing with a wicked sense of humor")
GIANT = Monsters("Giant", "none", 200, 50, 300, 0, [s.HIT, s.BDSLAM], 0, 40, 30, 20, 20, 10, 15, 0, 0,
                 [it.ROCK3], "A large, aggressive, humanoid")
GIANT_B = Monsters("Giant Soldier", "none", 300, 75, 400, 0, [s.HIT, s.BDSLAM, s.STAB, s.SLASH], 0, 60, 40, 15, 25, 10,
                   20, 0, 0, [it.ROCK3],
                   "A very large, very aggressive, very armed, humanoid. Who looks very angry.")

# Cave Monsters
TROLL = Monsters("Troll", "none", 100, 50, 225, 0, [s.SLASH, s.BDSLAM, s.CLUB], 0, 40, 35, 20, 25, 30, 40, 0, 0,
                 [it.ROCK2, it.ROCK3], "A twisted humanoid creature, well known for its riddles")
DLIZARD = Monsters("Dragon Lizard", "fire", 200, 75, 200, 300, [s.FIRE_A1, s.SLASH, s.FIRE_A2], 35, 30, 35, 40, 30, 20,
                   25, 0, 0, [it.F_GEM, it.GEM], "A cross between a dragon and a lizard")
DRAGON = Monsters("Mature Dragon", "fire", 300, 100, 250, 400, [s.FIRE_A1, s.FIRE_H1, s.FIRE_A2, s.FIRE_A3], 50, 40, 35,
                  40, 30, 50, 35, 40, 0, [it.F_GEM, it.GEM, it.D_WING, it.D_CLAW, it.D_TAIL], "A mighty fire dragon")

# Event Monsters (specific drops / attacks)
# THIEF = Monsters("Thief", ele, gold, health, mana, attacks,
#                  mag, stre, defe, spe, acc, luck, intel, heal, drain, drops, des)
# DRAGON_B = Monsters("Azeroth : Light Bringer", "light")

# Animals

DEER = Animals("Deer", 50, "none", 5, 15, 5, 5, [it.D_MEAT, it.D_PELT], "A fully grown healthy looking deer")
RABBIT = Animals("Rabbit", 15, "none", 2, 50, 15, 5, [it.R_MEAT, it.R_PELT], "A fully grown fluffy little rabbit")
FISH = Animals("Fish", 10, "none", 2, 15, 5, 5, [it.F_MEAT, it.F_SCALES], "A melon sized fish")
GOAT = Animals("Goat", 150, "none", 15, 15, 5, 5, [it.G_MEAT, it.G_PELT], "A fully grown, rather fluffy, mountain goat")
BEAR = Animals("Bear", 200, "none", 50, 15, 5, 5, [it.B_MEAT, it.B_PELT], "A decent sized, docile, black bear")

#  Location / Biomes
Monster_Loc = [[SLIME, CBAT, SLIME_B],
               [SLIME, CBAT, SLIME_B, SWAMP_RAT, SWAMP_RAT_B, UNDEAD_1, UNDEAD_2, UNDEAD_3, UNDEAD_B],
               [FSPIRIT, WSPIRIT, ESPIRIT, ASPIRIT, LSPIRIT, GOBLIN, GIANT, GIANT_B],
               [CBAT, GOBLIN, TROLL, DLIZARD, DRAGON]]

Animal_Loc = [[DEER, RABBIT], [FISH], [DEER, RABBIT, GOAT], [GOAT, FISH, BEAR]]
