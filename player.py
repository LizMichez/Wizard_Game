#  This file contains all functions and statistics related to the character class (main player capabilities)
#  These functions include : exp_gain, level_up, equip, strip, acquire, discard, restore, consume, use_spell, use_attack
#                            throw, open_inventory, open_stats, open_clothes
# Inventory cant use items, can throw and discard them
# Need to make type advantages a thing
from random import randint

import battle
import items

b = battle
i = items

day = 0

states = {1: "Battle", 2: "Inn", 3: "Town"}
state = ""

elementsW = ["dark", "light", "dark", "fire", "water", "earth", "air", "fire"]  # An elements weakness to their right


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

    clothes = {"hat": i.NO, "glasses": i.NO, "necklace": i.NO, "coat": i.NO, "shirt": i.NO, "bracelet": i.NO,
               "ring": i.NO, "wand": i.NO, "pants": i.NO, "shoes": i.NO}

    inventory = []
    inventoryCap = 25
    gold = 0

    level = int()
    experience = int()

    def exp_gain(self, exp):
        self.experience += int(exp)
        print("You gained", exp, "experience!")
        for x in range(5, 100):
            if x**2 < self.experience < (x+1)**2 and x - 4 != self.level:
                self.level = int(x - 4)
                print("\nCongratulations! You are now level", str(self.level) + "!")
                self.level_up()
                return

    def level_up(self):  # Somewhat randomly increases all of a player's stats
        for x in self.stats:
            if self.element == "light" and x == "heal":  # certain stats go up by less
                boost = 1 * randint(1, 3)
                self.stats[x] += boost
                print("     Your", x, "went up by", boost)
            elif self.element == "dark" and x == "drain":  # certain stats go up by less
                boost = 1*randint(1, 3)
                self.stats[x] += boost
                print("     Your", x, "went up by", boost)
            elif x == "drain" or x == "heal":
                continue
            else:
                boost = 1 * randint(1, 4)
                self.stats[x] += boost
                print("     Your", x, "went up by", boost)

        boost = 10 * randint(1, 3)
        self.health[1] += boost
        print("     Your max health went up by", boost)

        boost = 5 * randint(2, 5)
        self.mana[1] += boost
        print("     Your max mana went up by", boost)

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
                    for ii in item.stat:
                        self.stats[ii] += item.stat[ii]
                        print("You gained a", ii, "boost of", item.stat[ii])
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
            print("You have removed the", item.name, "and placed it in your inventory.")
            return
        print("Your inventory is too full to hold this item, free up some space then try again")

    def acquire(self, item):  # Get an item and add it to players inventory
        if len(self.inventory) < self.inventoryCap:
            self.inventory.append(item)
            print("You gained a", item.name)
            return
        print("Your inventory is full so you could not pick up the", item.name)

    def discard(self, item, speak):  # Remove one instance of an item from a players inventory
        self.inventory.remove(item)
        if speak:
            print("You have discarded the", item.name)

# Battle  and / or stat things
    def restore(self, lestat, name, amount, prints):  # Restore some health or mana without going over the max
        lestat[0] += amount
        if lestat[0] > lestat[1]:
            lestat[0] = lestat[1]
            if prints:
                print("You now have full", name)
        else:
            if prints:
                print("You restored", amount, name)

    def consume(self, item):  # NOT DONE
        if item.use:
            for x in item.use:
                if x == "health":
                    self.restore(self.health, "health", item.use[x], True)
                elif x == "mana":
                    self.restore(self.mana, "mana", item.use[x], True)
                else:
                    self.stats[x] += item.use[x]
        else:
            print("There's nothing to do with this item, you look at it sadly")

    def use_spell(self, spell, enemy):  # NOT DONE
        print("You cast", str(spell.name)+"!")
        if self.mana[0] < spell.mana:
            print("You do not have enough mana to complete this spell, you just wave your wand and look like an idiot")
            return
        self.mana[0] -= spell.mana
        if spell.base_dam > 0:  # Attack section
            hit = randint(0, 101)
            if hit < 35 - int(self.stats["accuracy"]*0.5):
                print("You missed the", str(enemy.name)+"!")
            elif b.baddie.element != "none" and spell.element == elementsW[elementsW.index(b.baddie.element)+1]:  # Super effective
                damage = spell.base_dam + int(self.stats["magic"]*1.5)
                enemy.health[0] -= damage
                print("You did", damage, "damage")
                self.restore(self.health, "health", int(damage * 0.01 * (self.stats["drain"] + spell.drain)), False)
            elif hit > 90 - int(self.stats["luck"]*0.5):
                damage = spell.base_dam + self.stats["magic"]
                enemy.health[0] -= damage
                print("You did", damage, "damage")
                self.restore(self.health, "health", int(damage * 0.01 * (self.stats["drain"]+spell.drain)), False)
            else:
                damage = spell.base_dam + self.stats["magic"] - enemy.defBoost
                if damage > 0:
                    enemy.health[0] -= damage
                    print("You did", damage, "damage")
                    self.restore(self.health, "health", int(damage*0.01*(self.stats["drain"]+spell.drain)), False)
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
                damage = int(item.dth*0.5*self.stats["strength"]) - enemy.stats["defense"]
                enemy.health[0] -= damage
                print("You threw the", item.name, "! \n It did", damage, "damage.")
                self.discard(item, False)
                return
            else:
                print("You threw the", item.name, "! \n It did no damage. Pathetic.")
                self.discard(item, False)
                return
        print("You can't throw this dummy!")

    def sleep(self):
        dream = int((self.health[0]/self.health[1])*10)
        if dream >= 9:
            print("\nYou went to sleep and had a great dream.... which of course you cant remember.")
        elif dream >= 5:
            print("\nYou went to sleep.")
        elif dream >= 2:
            print("\nYou collapsed into bed and slept like a rock... if rocks could sleep.")
        else:
            print("\nYou just made it to bed and collapsed into a sleep plagued with nightmares.")

        self.restore(self.health, "health", self.health[1], True)
        self.restore(self.mana, "mana", self.mana[1], True)

        global day
        day += 1

# Viewing information
    def open_inventory(self):
        chuck = False
        while not chuck:
            print("\nInventory")
            print("   Gold :", self.gold)
            if len(self.inventory) < 1:
                return
            printed = []
            ii = 0
            for x in self.inventory:
                if x not in printed:
                    ii += 1
                    print("      ", ii, ".", x.name, "[", self.inventory.count(x), "]")
                    printed.append(x)

            try:  # Interacting with items
                choose = int(input("Choose an item (letter to exit) : "))
                if choose not in range(1, len(printed)-1):
                    print("You have to enter the value of a item shown above.")
                item = printed[choose-1]
                print(item.name, ":", item.des, "\n     Item element :", item.element)
                while True:
                    print("What will you do with the item?: \n    1.Nothing\n    2.Discard\n    3.Throw")
                    choice = int(input())
                    if choice in range(1, 4):
                        if choice == 1:
                            print("Returning to inventory.")
                        elif choice == 2:
                            self.discard(item, True)
                            return
                        elif choice == 3:
                            if state == "Battle":
                                self.throw(item, b.baddie)
                                chuck = True
                            else:
                                print("You can't do that here.")
                        break
                    else:
                        print("You have to pick an actual option dummy")
            except (TypeError, ValueError):
                print("You closed your bag.")
                return
        if chuck:
            return "yeet"
            # NEED TO HAVE OPTION TO USE ITEMS

    def open_stats(self):  # Tells the player their stats
        print("\n")
        print(self.name, "- Level:", self.level)
        print("Health", self.health[0], "/", self.health[1])
        print("Mana", self.mana[0], "/", self.mana[1])
        for x in self.stats:
            print(x, self.stats[x])

    def open_clothes(self):  # Tells the player what they're wearing
        clotheson = []
        print("\nClothes")
        for x in self.clothes:
            if self.clothes[x] == i.NO:
                print("    ", x, ":")
            else:
                print("    ", x, ":", self.clothes[x].name)
                clotheson.append(x)
        if not state == "Battle":
            while True:
                choose = input("Do you want to change? (Y/N) : ")
                if choose == "y" or choose == "Y":
                    while True:
                        print("\nYou are wearing:")
                        for x in clotheson:
                            print("     "+str(clotheson.index(x)+1)+".", self.clothes[x].name)
                        try:
                            chooses = int(input("Select an item: "))
                            print("Do you want to remove the", self.clothes[clotheson[chooses-1]].name, "? (Y/N)")
                            choosess = input()
                            if choosess == "y" or choosess == "Y":
                                self.strip(self.clothes[clotheson[chooses-1]])
                                break
                            elif choosess == "n" or choosess == "N":
                                break
                        except (TypeError, ValueError, IndexError):
                            print("You know you have to enter a number of an item you're wearing right?")
                    break
                elif choose == "n" or choose == "N":
                    break
                else:
                    print("It's a yes or no question... enter Y or N")
