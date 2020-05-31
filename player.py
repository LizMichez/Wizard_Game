#  This file contains all functions and statistics related to the character class (main player capabilities)
#  These functions include : exp_gain, level_up, equip, strip, acquire, discard, restore, consume, use_spell, use_attack
#                            throw, open_inventory, open_stats, open_clothes
# PROBLEMS (MANY) WITH LEVEL_UP!!
import items
from random import randint


class Character:
    def __init__(self, magic, strength, defense, speed, accuracy, luck, intel, heal, drain, health, energy):
        self.stats = {"magic": magic, "strength": strength, "defense": defense, "speed": speed,
                      "accuracy": accuracy, "luck": luck, "intel": intel, "heal": heal, "drain": drain}
        self.health = [health, health]
        self.mana = [energy, energy]

    defBoost = 0

    gender = ""
    race = ""
    name = ""

    element = ""
    elementWords = []
    spells = []

    clothes = {"hat": items.NO, "glasses": items.NO, "necklace": items.NO, "coat": items.NO, "shirt": items.NO,
               "bracelet": items.NO, "ring": items.NO, "wand": items.NO, "pants": items.NO, "shoes": items.NO}

    inventory = []
    inventoryCap = 25
    gold = 0

    level = int()
    experience = int()

    def exp_gain(self, exp):
        self.experience += int(exp)
        for x in range(4, 100):
            if x**2 < self.experience < (x+1)**2 and x != self.level:
                self.level = int(x - 4)
                print("Congratulations! You are now level", str(self.level) + "!")
                self.level_up()
                return

    def level_up(self):  # Somewhat randomly increases all of a player's stats
        def stat_up(stat, scale, bot, top):
            boost = scale*randint(bot, top)
            stat += boost
            print("Your", x, "went up by", boost)

        for x in self.stats:
            if self.element == "light" and x == "heal":  # certain stats go up by less
                stat_up(self.stats[x], 1, 1, 3)
            if self.element == "dark" and x == "drain":  # certain stats go up by less
                stat_up(self.stats[x], 1, 1, 3)
            stat_up(self.stats[x], 1, 1, 5)
        stat_up(self.health[1], 10, 2, 3)  # max health goes up by 20 or 30
        stat_up(self.mana[1], 5, 3, 5)  # max mana goes up by multiples of 5 from 15 to 25

    def learn_spell(self, spell):
        if spell not in self.spells:
            print("You learned", spell.name, "!")
            self.spells.append(spell)
        else:
            print("You already know that spell!")

# Items / clothes related
    def equip(self, item):  # Attempts to put on an item and gain its status effects
        if item.element != self.element and item.element != "none":
            print("You can't wear items of an element that's not yours")
            return
        for x in self.clothes:
            if item.category == x:
                if self.clothes[x] == items.NO:
                    self.clothes[x] = item
                    print("\nYou have equip the", item.name)
                    for i in item.stat:
                        self.stats[i] += item.stat[i]
                        print("You gained a", i, "boost of", item.stat[i])
                    if item in self.inventory:
                        self.inventory.remove(item)
                    return
                else:
                    print("You already have an item in this slot, try taking that off and trying again")
                    return
        print("Item could not be equipped")

    def strip(self, item):  # Takes off an item, removes its status effects, and puts it in the players inventory
        if len(self.inventory) < self.inventoryCap:
            for x in item.stat:
                self.stats[x] -= item.stat[x]
            self.clothes[item.category] = items.NO
            self.inventory.append(item)
            return
        print("Your inventory is too full to hold this item, free up some space then try again")

    def acquire(self, item):  # Get an item and add it to players inventory
        if len(self.inventory) < self.inventoryCap:
            self.inventory.append(item)
            print("You gained a", item.name)
            return
        print("Your inventory is full so you could not pick up the", item.name)

    def discard(self, item):  # Remove one instance of an item from a players inventory
        self.inventory.remove(item)
        print("You have discarded the", item.name)

# Battle  and / or stat things
    def restore(self, lestat, amount, prints):  # Restore some health or mana without going over the max
        lestat[0] += amount
        if lestat[0] > lestat[1]:
            lestat[0] = lestat[1]
            if prints:
                print("You now have full", lestat)
        else:
            if prints:
                print("You restored", amount, lestat)

    def consume(self, item):  # NOT DONE
        if item.use:
            for x in item.use:
                if x == "health":
                    self.restore(self.health, item.use[x], True)
                elif x == "mana":
                    self.restore(self.mana, item.use[x], True)
                else:
                    self.stats[x] += item.use[x]
        else:
            print("There's nothing to do with this item, you look at it sadly")

    def use_spell(self, spell, enemy):  # NOT DONE
        print("You cast", spell.name, "!")
        if self.mana[0] < spell.mana:
            print("You do not have enough mana to complete this spell, you just wave your wand and look like an idiot")
            return
        self.mana[0] -= spell.mana
        if spell.base_dam > 0:  # Attack section
            hit = randint(0, 101)
            if hit < 35 - int(self.stats["accuracy"]*0.5):
                print("You missed the", enemy.name, "!")
            elif hit > 90 - int(self.stats["luck"]*0.5):
                damage = spell.base_dam + self.stats["magic"]
                enemy.health[0] -= damage
                print("You did", damage, "damage")
                self.restore(self.health, int(damage * 0.01 * (self.stats["drain"]+spell.drain)), False)
            else:
                damage = spell.base_dam + self.stats["magic"] - enemy.defBoost
                if damage > 0:
                    enemy.health[0] -= damage
                    print("You did", damage, "damage")
                    self.restore(self.health, int(damage*0.01*(self.stats["drain"]+spell.drain)), False)
                else:
                    print("The enemy defended against the attack, it did no damage")

        if spell.healing > 0:  # Healing section
            self.health[0] += spell.healing + self.stats["heal"]
            print("You restored", spell.healing + self.stats["heal"], "health.")

        if spell.recoil > 0:  # Recoil section
            if spell.recoil - int(0.5*self.stats["intel"]) > 0:
                self.health[0] -= spell.recoil - self.stats["intel"]
                print("The recoil did", spell.recoil - self.stats["intel"], "damage")
            else:
                print("You were able to avoid the recoil")

        if spell.base_def > 0:  # Defense section
            self.defBoost += spell.base_def + self.stats["defense"]

    def use_attack(self, attack, enemy):
        damage = int(attack.damage/2) + int(0.5*self.stats["strength"]) - enemy.defBoost
        if damage > 0:
            enemy.health[0] -= damage
            print("You did", damage, "damage")
        else:
            print("The enemy defended against the attack, it did no damage")

        if attack.defense > 0:  # Defense section
            self.defBoost += attack.defense + self.stats["defense"]

        if attack.recoil > 0:  # Recoil section
            if attack.recoil - int(0.5*self.stats["intel"]) > 0:
                self.health[0] -= attack.recoil - self.stats["intel"]
                print("The recoil did")
            else:
                print("You were able to avoid the recoil")

    def throw(self, item, enemy):  # Throws an item at the opponent
        if item.chu:  # if the item is chuckable
            if int(item.dth*0.5*self.stats["strength"]) > enemy.stats["defense"]:
                enemy.health -= int(item.dth*0.5*self.stats["strength"]) - enemy.stats["defense"]
                print("You threw the", item.name, "! \n It did", item.dth, "damage.")
                self.discard(item)
                return
            else:
                print("You threw the", item.name, "! \n It did no damage. Pathetic.")
                self.discard(item)
                return
        print("You can't throw this dummy!")

# Viewing information
    def open_inventory(self):  # NEEDS TO show gold
        print("\nInventory")
        print("   Gold :", self.gold)
        if len(self.inventory) < 1:
            return
        printed = []
        i = 0
        for x in self.inventory:
            if x not in printed:
                i += 1
                print("      ", i, ".", x.name, "[", self.inventory.count(x), "]")
                printed.append(x)
        # print("NEED TO HAVE OPTION TO USE AND LEARN MORE ABOUT ITEMS")

    def open_stats(self):  # Tells the player their stats
        print("\n")
        print(self.name, "- Level:", self.level)
        print("Health", self.health[0], "/", self.health[1])
        print("Mana", self.mana[0], "/", self.mana[1])
        for x in self.stats:
            print(x, self.stats[x])

    def open_clothes(self):  # Tells the player what they're wearing
        print("\nClothes")
        for x in self.clothes:
            if self.clothes[x] == items.NO:
                print("    ", x, ":")
            else:
                print("    ", x, ":", self.clothes[x].name)
