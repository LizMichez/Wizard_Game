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
                self.level = int(x)
                print("Congratulations! You are now level", str(self.level) + "!")
                self.level_up()
                return

    def level_up(self):  # Somewhat randomly increases all of a player's stats
        def stat_up(stat, scale, min, max):
            boost = scale*randint(min, max)
            stat += boost
            print("Your", x, "went up by", boost)

        for x in self.stats:
            if self.element == "light" and x == "heal":  # certain stats go up by less
                stat_up(self.stats[x], 1, 1, 3)
            if self.element == "dark" and x == "drain":  # certain stats go up by less
                stat_up(self.stats[x], 1, 1, 3)
            stat_up(self.stats[x], 1, 1, 5)
        stat_up(self.health[1], 10, 2, 3)  # health goes up by 20 or 30
        stat_up(self.mana[1], 5, 3, 5)  # mana goes up by multiples of 5 from 15 to 25

    def equip(self, item):  # Attempts to put on an item and gain its status effects
        if item.element != self.element and item.element != "none":
            print(self.element)
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

    def stip(self, item):  # Takes off an item, removes its status effects, and puts it in the players inventory
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

    def consume(self, item):  # NOT DONE
        print("om nom nom slurp the potion")

    def use_spell(self, spell):  # NOT DONE
        print("Ur a wizard harry")

    def use_item(self, item):  # NOT DONE
        print("throw that rock")

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
