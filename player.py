import items
# import spells

from random import randint


class Character:
    def __init__(self, magic, strength, defense, speed, accuracy, luck, intel, heal, drain, health, energy):
        self.stats = {"magic": magic, "strength": strength, "defense": defense, "speed": speed,
                      "accuracy": accuracy, "luck": luck, "intel": intel, "heal": heal, "drain": drain}
        self.health = [health, health]
        self.mana = [energy, energy]

    gender = ""
    race = ""
    name = ""

    element = ""
    elementWords = []
    spells = []

    clothes = {"hat": "", "glasses": "", "necklace": "", "coat": "", "shirt": "",
               "bracelet": "", "ring": "", "wand": "", "pants": "", "shoes": ""}
    inventory = []
    inventoryCap = 25
    gold = []

    level = int()
    experience = int()

    def exp_gain(self, exp):
        self.experience += int(exp)
        for x in range(4, 100):
            if x**2 < self.experience < (x+1)**2 and x != self.level:
                self.level = int(x)
                print("Congratulations! You are now level", str(self.level) + "!")
                self.level_up()
                return

    def level_up(self):  # Somewhat randomly increases all of a player's stats
        for x in self.stats:
            if x == "heal" or "drain":  # certain stats go up by less
                boost = randint(1, 2)
                self.stats[x] += boost
                print("Your", x, "went up by", boost)
            boost = randint(1, 5)  # most stats go up by 1 - 5
            self.stats[x] += boost
            print("Your", x, "went up by", boost)
        boost = randint(2, 3)  # health goes up by 20 or 30
        self.health[1] += 10*boost
        print("Your max health went up by", 10*boost)
        boost = randint(3, 6)  # mana goes up by multiples of 5 from 15 to 30
        self.mana[1] += 5*boost
        print("Your max mana went up by", 5*boost)

    def equip(self, item):  # Attempts to put on an item and gain its status effects
        for x in self.clothes:
            if item.category == x:
                if self.clothes[x] == "":
                    self.clothes[x] = item
                    print("\nYou have equip the", item.name)
                    for i in item.stat:
                        self.stats[i] += item.stat[i]
                        print("You gained a", i, "boost of", item.stat[i])
                    self.inventory.remove(item)
                    return
                else:
                    print("You already have an item in this slot, try taking that off and trying again")
                    return
        print("Item could not be equipped")

    def stip(self, item):  # Takes off an item, removes its status effects, and puts it in the players inventory
        if len(self.inventory) < self.inventoryCap:
            for x in item.stat:
                self.stats[x] -= item.stat[x]
            self.clothes[item.category] = ""
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

    def use_spell(self):  # NOT DONE
        print("Ur a wizard harry")

    def use_item(self):  # NOT DONE
        print("throw that rock")

    def open_inventory(self):  # NEEDS TO BE CONNECTED TO TOWN and / or Battle and show gold
        print("\nInventory")
        if len(self.inventory) < 1:
            print("Your inventory is empty")
        printed = []
        i = 0
        for x in self.inventory:
            if x not in printed:
                i += 1
                print("      ", i, ".", x.name, "[", self.inventory.count(x), "]")
                printed.append(x)
        # print("NEED TO HAVE OPTION TO USE AND LEARN MORE ABOUT ITEMS")

    def open_stats(self):  # Tells the player their stats
        print(self.name, "Level:", self.level)
        print("Health", self.health[0], "/", self.health[1])
        print("Mana", self.mana[0], "/", self.mana[1])
        for x in self.stats:
            print(x, self.stats[x])

    def open_clothes(self):  # Tells the player what they're wearing
        print("\nClothes")
        for x in self.clothes:
            if self.clothes[x] == "":
                print("    ", x, ":", self.clothes[x])
            else:
                print("    ", x, ":", items.DA1.name)  # This is bs, fix it so it actually says the item name and not just one that makes u feel better about your failure
