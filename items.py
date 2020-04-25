# all items, what they do, cost, level to use, type, and effects
class Items:
    def __init__(self, name, category, element, level, worth, chuck, dmg_thrown, stat_effect, use_effect, description):
        self.name = str(name)
        self.category = str(category)  # based on where it goes on the body or drops or potions/food
        self.ele = str(element)
        self.lev = int(level)
        self.wor = int(worth)
        self.chu = bool(chuck)  # can it be thrown
        self.dth = int(dmg_thrown)
        self.stat = stat_effect  # passive stat boost
        self.use = use_effect  # when used in battle
        self.des = str(description)


# Starter Items
FW1 = Items("Basic Fire Wand", "wand", "fire", 0, 50, False, 0, {}, {},
            "A basic fire wand, it's warm to the touch'")
WW1 = Items("Basic Water Wand", "wand", "water", 0, 50, False, 0, {}, {},
            "A basic water element wand, it's cool to the touch")
EW1 = Items("Basic Earth Wand", "wand", "earth", 0, 50, False, 0, {}, {},
            "A basic earth element wand, it seems to be growing a leaf")
VW1 = Items("Basic Air Wand", "wand", "air", 0, 50, False, 0, {}, {},
            "A basic fire element wand, it's light and occasionally shocks you")
DA1 = Items("Mysterious Dark Amulet", "necklace", "dark", 0, 75, False, 0, {}, {},
            "A mysterious silver necklace with a large dark stone, it somehow seems to absorb the light around it")
LA1 = Items("Mysterious Dark Amulet", "necklace", "dark", 0, 75, False, 0, {}, {},
            "A mysterious gold necklace with a large pale stone, it glows with a soft light")

# Wands

# Jewelry

# Clothes

# Potions

# Drops (Other)
ROCK1 = Items("Pebble", "misc", "earth", 0, 1, True, 5, {}, {},
              "A relatively small pebble, why are you carrying this again?")
ROCK2 = Items("Rock", "misc", "earth", 0, 3, True, 10, {}, {},
              "A fist-sized rock, why are you carrying this again?")
ROCK3 = Items("Stone", "misc", "earth", 0, 5, True, 15, {}, {},
              "A melon-seized rock, why and how are you carrying this again?")
