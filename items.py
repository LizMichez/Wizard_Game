# all items, what they do, cost, level to use, type, and effects
class Items:
    def __init__(self, name, category, element, level, worth, chuck, dmg_thrown, stat_effect, use_effect, description):
        self.name = str(name)
        self.category = str(category)  # based on where it goes on the body or drops or potions/food
        self.element = str(element)
        self.lev = int(level)
        self.wor = int(worth)
        self.chu = bool(chuck)  # can it be thrown
        self.dth = int(dmg_thrown)
        self.stat = stat_effect  # passive stat boost
        self.use = use_effect  # when used in battle
        self.des = str(description)


# Starter Items
FW1 = Items("Basic Fire Wand", "wand", "fire", 0, 100, False, 0, {}, {},
            "A basic fire wand, it's warm to the touch'")
WW1 = Items("Basic Water Wand", "wand", "water", 0, 100, False, 0, {}, {},
            "A basic water element wand, it's cool to the touch")
EW1 = Items("Basic Earth Wand", "wand", "earth", 0, 100, False, 0, {}, {},
            "A basic earth element wand, it seems to be growing a leaf")
VW1 = Items("Basic Air Wand", "wand", "air", 0, 100, False, 0, {}, {},
            "A basic fire element wand, it's light and occasionally shocks you")
DA1 = Items("Mysterious Dark Amulet", "necklace", "dark", 0, 125, False, 0, {}, {},
            "A mysterious silver necklace with a large dark stone, it somehow seems to absorb the light around it")
LA1 = Items("Mysterious Light Amulet", "necklace", "dark", 0, 125, False, 0, {}, {},
            "A mysterious gold necklace with a large pale stone, it glows with a soft light")

# Wands

# Jewelry (necklace, ring, bracelet)
A1 = Items("Silver Amulet", "necklace", "none", 3, 100, False, 0, {"magic": 10}, {}, "An enchanted silver chain")
A2 = Items("Gold Amulet", "necklace", "none", 6, 220, False, 0, {"magic": 20}, {}, "An enchanted gold chain")

R1 = Items("Silver Ring", "ring", "none", 3, 60, False, 0, {"magic": 5}, {}, "An enchanted silver ring")
R2 = Items("Gold Ring", "ring", "none", 3, 150, False, 0, {"magic": 10}, {}, "An enchanted gold ring")

B1 = Items("Silver Bracelet", "bracelet", "none", 3, 80, False, 0, {"magic": 8}, {}, "An enchanted silver bracelet")
B2 = Items("Silver Ring", "ring", "none", 3, 180, False, 0, {"magic": 16}, {}, "An enchanted gold bracelet")

# Clothes (hat, glasses, coat, shirt, shoes)

# Potions (For ones that attack the enemy of have more special effects, link to future effects folder or spells)
MP1 = Items("Weak Mana Potion", "potion", "none", 0, 25, True, 5, {}, {"mana": 10}, "Restores 10 mana")
MP2 = Items("Mana Potion", "potion", "none", 3, 50, True, 5, {}, {"mana": 25}, "Restores 25 mana")
MP3 = Items("Strong Mana Potion", "potion", "none", 5, 100, True, 5, {}, {"mana": 100}, "Restores 100 mana")

HP1 = Items("Weak Health Potion", "potion", "none", 0, 25, True, 5, {}, {"health": 10}, "Restores 10 health")
HP2 = Items("Health Potion", "potion", "none", 3, 50, True, 5, {}, {"health": 25}, "Restores 25 health")
HP3 = Items("Strong Health Potion", "potion", "none", 5, 100, True, 5, {}, {"health": 100}, "Restores 100 health")

FP1 = Items("Strong Health Potion", "potion", "none", 7, 150, True, 5, {}, {"mana": 100, "health": 100},
            "Restores 100 health and 100 mana")

# Monster Drops (Other)
ROCK1 = Items("Pebble", "misc", "earth", 0, 1, True, 5, {}, {},
              "A relatively small pebble, why are you carrying this again?")
ROCK2 = Items("Rock", "misc", "earth", 0, 3, True, 10, {}, {},
              "A fist-sized rock, why are you carrying this again?")
ROCK3 = Items("Stone", "misc", "earth", 0, 5, True, 15, {}, {},
              "A melon-seized rock, why and how are you carrying this again?")

JELLY_C = Items("Clear Jelly", "misc", "none", 0, 15, True, 0, {}, {},
                "An apple sized ball of clear jelly, useful for cooking and has some medical properties")
JELLY_S = Items("Silver Jelly", "misc", "none", 0, 25, True, 0, {}, {},
                "An apple sized ball of silver jelly, useful for potions, cooking and medicine")
JELLY_G = Items("Gold Jelly", "misc", "none", 0, 50, True, 0, {}, {},
                "An apple sized ball of gold jelly, useful for potions, cooking, magic, generating mana, and medicine")

B_CLAW = Items("Bat Claw", "misc", "dark", 0, 20, True, 2, {}, {}, "The claw of a corrupt bat, it oozes darkness")
B_WING = Items("Bat Wing", "misc", "dark", 0, 25, True, 0, {}, {}, "The wing of a corrupt bat, it oozes darkness")
R_CLAW = Items("Bat Claw", "misc", "none", 0, 25, True, 4, {}, {}, "The claw of a swamp rat")
R_TAIL = Items("Bat Wing", "misc", "none", 0, 30, True, 2, {}, {}, "The wing of a swamp rat")

GEM = Items("Gem", "misc", "none", 0, 50, True, 10, {}, {}, "A colourless gem infused with no magic")
C_GEM = Items("Corrupt Gem", "misc", "dark", 3, 40, True, 10, {}, {}, "A black gem infused with dark magic")
F_GEM = Items("Fire Gem", "misc", "fire", 3, 45, True, 10, {}, {}, "A red gem infused with fire magic")
W_GEM = Items("Water Gem", "misc", "water", 3, 45, True, 10, {}, {}, "A blue gem infused with water magic")
E_GEM = Items("Earth Gem", "misc", "earth", 3, 45, True, 10, {}, {}, "A brown-green gem infused with earth magic")
A_GEM = Items("Air Gem", "misc", "air", 3, 45, True, 10, {}, {}, "A white gem infused with air magic")
L_GEM = Items("Light Gem", "misc", "light", 3, 45, True, 10, {}, {}, "A glowing gem infused with light magic")

# Filler Item
NO = Items("NO", "NO", "NO", 0, 0, False, 0, {}, {}, "NO")
