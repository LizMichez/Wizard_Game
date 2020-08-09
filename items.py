# all items, what they do, cost, level to use, type, and effects
class Items:
    def __init__(self, name, category, element, level, worth, chuck, dmg_thrown, stat_effect, use_effect, description):
        self.name = str(name)
        self.category = str(category)  # based on where it goes on the body or drops or potions/food
        self.element = str(element)
        self.lev = int(level)  # level to use / wear item
        self.worth = int(worth)  # base worth, adjusted for selling rates
        self.chu = bool(chuck)  # can it be thrown
        self.dth = int(dmg_thrown)
        self.stat = stat_effect  # passive stat boost
        self.use = use_effect  # affect when used in battle
        self.des = str(description)


# Starter Items
F_W1 = Items("Basic Fire Wand", "wand", "fire", 0, 100, False, 0, {"magic": 3}, {},
             "A basic fire wand, it's warm to the touch'")
W_W1 = Items("Basic Water Wand", "wand", "water", 0, 100, False, 0, {"magic": 3}, {},
             "A basic water element wand, it's cool to the touch")
E_W1 = Items("Basic Earth Wand", "wand", "earth", 0, 100, False, 0, {"magic": 3}, {},
             "A basic earth element wand, it seems to be growing a leaf")
V_W1 = Items("Basic Air Wand", "wand", "air", 0, 100, False, 0, {"magic": 3}, {},
             "A basic air element wand, it's light and occasionally shocks you")
D_A1 = Items("Mysterious Dark Amulet", "necklace", "dark", 0, 125, False, 0, {"magic": 3}, {},
             "A mysterious silver necklace with a large dark stone, it somehow seems to absorb the light around it")
L_A1 = Items("Mysterious Light Amulet", "necklace", "light", 0, 125, False, 0, {"magic": 3}, {},
             "A mysterious gold necklace with a large pale stone, it glows with a soft light")

# Wands / Staffs
#  magic, strength, defense, speed, accuracy, luck, intel, heal, drain, health, energy):
F_W2 = Items("Sparky Fire Wand", "wand", "fire", 4, 250, False, 0, {"magic": 10}, {},
             "A fancy fire element wand, the end looks charred and smoldering")
F_W3 = Items("Flaming Fire Staff", "wand", "fire", 8, 750, False, 0, {"magic": 15, "strength": 10}, {},
             "An elaborate staff with a glowing red jem at the head, the wood smolders when you touch it")
W_W2 = Items("Cool Water Wand", "wand", "water", 4, 250, False, 0, {"magic": 10}, {},
             "A fancy water element wand, the end looks to be made of enchanted ice")
W_W3 = Items("Snow Staff", "wand", "water", 8, 750, False, 0, {"magic": 15, "accuracy": 10}, {},
             "An elaborate staff with a glowing blue jem at the head, snow appears around it when you touch it")
E_W2 = Items("Living Wand", "wand", "earth", 4, 250, False, 0, {"magic": 10}, {},
             "A fancy earth element wand, it appears to be growing a wide range of small plants on it")
E_W3 = Items("Tree Staff", "wand", "earth", 8, 750, False, 0, {"magic": 15, "defense": 10}, {},
             "An elaborate staff which appears to be a rootless portable tree, it has a green jem below its leaves")
V_W2 = Items("Breezy Wand", "wand", "air", 4, 250, False, 0, {"magic": 10}, {},
             "A fancy air element wand, electricity seems to flicker through it at your touch")
V_W3 = Items("Vortex Staff", "wand", "air", 8, 750, False, 0, {"magic": 15, "speed": 10}, {},
             "An elaborate staff with a glowing purple jem surrounded what appears to be a small tornado")
D_W1 = Items("Cursed Wand", "wand", "dark", 4, 250, False, 0, {"magic": 10}, {},
             "A fancy wand of black, twisted wood, it seems to sap the light from the area around it")
D_W2 = Items("Deadwood Staff", "wand", "dark", 8, 750, False, 0, {"magic": 15, "drain": 10}, {},
             "An elaborate dark staff covered in black jem stones, patches of it appear to be made of pure darkness")
L_W1 = Items("Shimmering Wand", "wand", "light", 4, 250, False, 0, {"magic": 10}, {},
             "A fancy wand of light, shimmering wood, it seems to radiate light and life to the area around it")
L_W2 = Items("Dazzling Staff", "wand", "light", 8, 750, False, 0, {"magic": 15, "light": 10}, {},
             "An elaborate staff covered in clear, glowing, jem stones; some areas appear to be made of white marble")

# Jewelry (necklace, ring, bracelet)
AM1 = Items("Silver Amulet", "necklace", "none", 3, 100, False, 0, {"magic": 10}, {}, "An enchanted silver chain")
AM2 = Items("Gold Amulet", "necklace", "none", 6, 250, False, 0, {"magic": 15}, {}, "An enchanted gold chain")

RNG1 = Items("Silver Ring", "ring", "none", 3, 60, False, 0, {"magic": 5}, {}, "An enchanted silver ring")
RNG2 = Items("Gold Ring", "ring", "none", 5, 150, False, 0, {"magic": 10}, {}, "An enchanted gold ring")

BR1 = Items("Silver Bracelet", "bracelet", "none", 3, 80, False, 0, {"magic": 8}, {}, "An enchanted silver bracelet")
BR2 = Items("Silver Ring", "ring", "none", 5, 200, False, 0, {"magic": 12}, {}, "An enchanted gold bracelet")

# Clothes (hat, glasses, coat, shirt, shoes)

HAT1 = Items("Plain Cap", "hat", "none", 0, 15, False, 0, {"defense": 3}, {}, "A plain brown cap")
HAT2 = Items("Plain Helmet", "hat", "none", 2, 75, False, 0, {"defense": 10}, {}, "A sturdy metal helmet")
HAT3 = Items("Iron Helmet", "hat", "none", 5, 200, False, 0, {"defense": 20}, {}, "A well made helmet with guard")
F_HAT1 = Items("Red Cap", "hat", "fire", 2, 50, False, 0, {"defense": 3, "magic": 5}, {}, "A warm red cap")
F_HAT2 = Items("Fiery Pointed Hat", "hat", "fire", 6, 500, False, 0, {"defense": 7, "magic": 10}, {},
               "A fiery red witches hat, it appears to be somewhat made of magma.")
F_HAT3 = Items("Apollos Helm", "hat", "fire", 10, 1000, False, 0, {"defense": 10, "magic": 20, "strength": 10}, {},
               "A flaming helmet with a silver body and gold detail, it shines brighter than your future.")
W_HAT1 = Items("Blue Cap", "hat", "water", 2, 50, False, 0, {"defense": 3, "magic": 5}, {}, "A cool blue cap")
W_HAT2 = Items("Damp Pointed Hat", "hat", "water", 6, 500, False, 0, {"defense": 7, "magic": 10}, {},
               "A mildly damp witches hat, it seems to have ice forming on the tip.")
W_HAT3 = Items("Poseidon's Crown", "hat", "water", 10, 1000, False, 0, {"defense": 10, "magic": 20, "accuracy": 10}, {},
               "A cool silver helm with blue jewels, you can hear the ocean when you put it on.")
E_HAT1 = Items("Green Cap", "hat", "earth", 2, 50, False, 0, {"defense": 3, "magic": 5}, {}, "A stiff green cap")
E_HAT2 = Items("Earthen Pointed Hat", "hat", "earth", 6, 500, False, 0, {"defense": 7, "magic": 10}, {},
               "A mellow green witches hat, a garden appears to be sprouting on the top.")
E_HAT3 = Items("Crown of Thorns and Roses", "hat", "earth", 10, 1000, False, 0, {"defense": 20, "magic": 20}, {},
               "A crown of living golden roses, its heavier than it looks.")
V_HAT1 = Items("Purple Cap", "hat", "air", 2, 50, False, 0, {"defense": 3, "magic": 5}, {}, "A light purple cap")
V_HAT2 = Items("Gusty Pointed Hat", "hat", "air", 6, 500, False, 0, {"defense": 7, "magic": 10}, {},
               "A light, almost iridescent purple witches hat, its swaying despite the lack of breeze.")
V_HAT3 = Items("Zeus's Crown", "hat", "air", 10, 1000, False, 0, {"defense": 5, "magic": 20, "speed": 15}, {},
               "A small band of impossibly light metal, it crackles when touched.")
D_HAT1 = Items("Black Cap", "hat", "dark", 2, 50, False, 0, {"defense": 3, "magic": 5}, {}, "A pitch black cap")
D_HAT2 = Items("Murky Pointed Hat", "hat", "dark", 6, 500, False, 0, {"defense": 7, "magic": 10}, {},
               "A jet black witches hat, it seems to pull the light and warmth out of its surroundings")
D_HAT3 = Items("Hades Diadem", "hat", "dark", 10, 1000, False, 0, {"defense": 10, "magic": 20, "drain": 5}, {},
               "A elaborate crown made of obsidian, seems to be constantly surrounded by dark fog")
L_HAT1 = Items("White Cap", "hat", "light", 2, 50, False, 0, {"defense": 3, "magic": 5}, {}, "A shimmering white cap")
L_HAT2 = Items("Radiant Pointed Hat", "hat", "light", 6, 500, False, 0, {"defense": 7, "magic": 10}, {},
               "A glowing white witches hat, it seems to radiate joy and good health")
L_HAT3 = Items("Halo", "hat", "light", 10, 1000, False, 0, {"defense": 10, "magic": 20, "heal": 5}, {},
               "A band of light that seems to float above the wearers head, its cool to the touch")

GLASS1 = Items("Simple Glasses", "glasses", "none", 2, 50, False, 0, {"accuracy": 5}, {}, "Glasses ..... made of glass")
GLASS2 = Items("Shades", "glasses", "none", 5, 100, False, 0, {"accuracy": 10}, {}, "Like glasses but sun proof")
GLASS3 = Items("Safety Goggles", "glasses", "none", 7, 200, False, 0, {"accuracy": 10, "defense": 10}, {},
               "The best protection you can ever get")

SHIRT1 = Items("Plain Shirt", "shirt", "none", 0, 20, False, 0, {}, {}, "A plain brown shirt, it has patches and rips")
SHIRT2 = Items("White Cotton Shirt", "shirt", "none", 1, 40, False, 0, {"luck": 2}, {}, "A clean white cotton shirt")
SHIRT3 = Items("Chain-Mail Shirt", "shirt", "none", 4, 100, False, 0, {"defense": 10}, {}, "A simple chain-mail shirt")
SHIRT4 = Items("Dragon Scale Shirt", "shirt", "none", 9, 500, False, 0, {"defense": 20}, {},
               "An elaborate protective shirt made of nearly impenetrable dragon scales")

COAT1 = Items("Plain Coat", "coat", "none", 0, 75, False, 0, {"defense": 5}, {}, "A plain brown coat")
COAT2 = Items("Plated Cloak", "coat", "none", 6, 200, False, 0, {"defense": 15}, {},
              "A good quality cloak with metal plating in the torso area.")
F_COAT1 = Items("Ember Robes", "coat", "fire", 5, 150, False, 0, {"defense": 5, "magic": 10}, {}, "Smoking red robes")
F_COAT2 = Items("Cloak of Infernos", "coat", "fire", 8, 750, False, 0, {"defense": 10, "magic": 20}, {},
                "Flaming red robes with sparks coming off the hem")
W_COAT1 = Items("Frosted Robes", "coat", "water", 5, 150, False, 0, {"defense": 5, "magic": 10}, {}, "Cool blue robes")
W_COAT2 = Items("Glacial Cloak", "coat", "water", 8, 750, False, 0, {"defense": 10, "magic": 20}, {},
                "Deep blue robes with frosted hems")
E_COAT1 = Items("Earthy Robes", "coat", "earth", 5, 150, False, 0, {"defense": 5, "magic": 10}, {}, "Leafy green robes")
E_COAT2 = Items("Cloak of Jem Stones", "coat", "earth", 8, 750, False, 0, {"defense": 10, "magic": 20}, {},
                "Deep green robes with jem stones scattered around the hems")
V_COAT1 = Items("Breezy Robes", "coat", "air", 5, 150, False, 0, {"defense": 5, "magic": 10}, {}, "Light, purple robes")
V_COAT2 = Items("Cloak of Hurricanes", "coat", "air", 8, 750, False, 0, {"defense": 10, "magic": 20}, {},
                "Striking purple robes billowing despite the lack of breeze")
D_COAT1 = Items("Dark Robes", "coat", "dark", 5, 150, False, 0, {"defense": 5, "magic": 10}, {}, "Dark black robes")
D_COAT2 = Items("Cloak of the Abyss", "coat", "dark", 8, 750, False, 0, {"defense": 10, "magic": 20}, {},
                "Inky black hooded robes that seem to absorb the light around them")
L_COAT1 = Items("Bright Robes", "coat", "light", 5, 150, False, 0, {"defense": 5, "magic": 10}, {}, "Stark white robes")
L_COAT2 = Items("Radiant Cloak", "coat", "light", 8, 750, False, 0, {"defense": 10, "magic": 20}, {},
                "Brilliant white hooded robes with shining hems")

SHOES1 = Items("Plain Brown Shoes", "shoes", "none", 0, 50, False, 0, {}, {}, "Simple brown shoes with leather straps")
SHOES2 = Items("Classy Silver Shoes", "shoes", "none", 3, 150, False, 0, {"speed": 5}, {}, "Classy. Silver. Shoes.")
F_SHOES1 = Items("Smoldering Shoes", "shoes", "fire", 6, 300, False, 0, {"speed": 7, "magic": 8, "strength": 5}, {},
                 "Shoes that look like smoldering embers . . . I'm sure it's safe")
W_SHOES1 = Items("Frosted Shoes", "shoes", "water", 6, 300, False, 0, {"speed": 10, "magic": 10}, {},
                 "Shoes that appear to be made of ice . . . But they're warm . . . and comfy")
E_SHOES1 = Items("Earthen Shoes", "shoes", "earth", 6, 300, False, 0, {"speed": 5, "magic": 10, "defense": 5}, {},
                 "They look like muddy boots . . . but they're magic")
V_SHOES1 = Items("Airstream Shoes", "shoes", "air", 6, 300, False, 0, {"speed": 15, "magic": 5}, {},
                 "Light, incredibly comfy purple and yellow shoes")
D_SHOES1 = Items("Black Shoes", "shoes", "dark", 6, 300, False, 0, {"speed": 7, "magic": 13}, {},
                 "They're black shoes . . . very black shoes")
L_SHOES1 = Items("Glimmering Shoes", "shoes", "light", 6, 300, False, 0, {"speed": 7, "magic": 13}, {},
                 "Brilliant white, very classy shoes")

# Food (Status restoring) Muffins -> Mana, Soup -> Health, Steak, Water -> Mana + Health, Fruit -> Stats perm
B_MUFF = Items("Blueberry Muffin", "food", "none", 0, 15, False, 0, {}, {"mana": 10}, "Tasty, decent sized muffin")
C_MUFF = Items("Cinnamon Swirl Muffin", "food", "none", 0, 25, False, 0, {}, {"mana": 25},
               "Tasty, decent sized muffin with a cinnamon swirl glaze")
F_MUFF = Items("Fancy Custard Muffin", "food", "none", 0, 40, False, 0, {}, {"mana": 100},
               "Tasty, decent sized muffin with fancy icing and a custard filling")

T_SOUP = Items("Red-Fruit Soup", "food", "none", 0, 20, False, 0, {}, {"health": 25}, "Red, hearty, heterogeneous soup")
R_SOUP = Items("Rabbit Monster Stew", "food", "none", 0, 30, False, 0, {}, {"health": 75},
               "Chunky stew made from locally raised rabbit monsters")

F_STEAK = Items("Flank Steak", "food", "none", 0, 50, False, 0, {}, {"mana": 25, "health": 25},
                "The flank steak of some animal . . . not sure which one but not going to ask")
P_STEAK = Items("Dragon Tail Steak", "food", "none", 0, 75, False, 0, {}, {"mana": 80, "health": 100},
                "Meat from the tail of a Dragon Lizard, it's infused with magic")

B_FRUIT = Items("Blue Fruit", "food", "none", 0, 300, False, 0, {}, {"health": 10}, "Magical blue glowing fruit")
R_FRUIT = Items("Red Fruit", "food", "none", 0, 300, False, 0, {}, {"mana": 10}, "Magical red glowing fruit")
G_FRUIT = Items("Golden Fruit", "food", "none", 0, 500, False, 0, {}, {"mana": 10, "health": 10}, "Golden shiny fruit")

W_DRINK = Items("Water", "food", "none", 0, 10, False, 0, {}, {"mana": 10, "health": 10}, "Di-hydrogen monoxide")

# Potions (For ones that attack the enemy of have more special effects, link to future effects folder or spells)
M_POT1 = Items("Weak Mana Potion", "potion", "none", 0, 25, True, 5, {}, {"mana": 10}, "Restores 10 mana")
M_P0T2 = Items("Mana Potion", "potion", "none", 3, 50, True, 5, {}, {"mana": 25}, "Restores 25 mana")
M_POT3 = Items("Strong Mana Potion", "potion", "none", 5, 100, True, 5, {}, {"mana": 100}, "Restores 100 mana")

HP_POT1 = Items("Weak Health Potion", "potion", "none", 0, 25, True, 5, {}, {"health": 10}, "Restores 10 health")
HP_POT2 = Items("Health Potion", "potion", "none", 3, 50, True, 5, {}, {"health": 25}, "Restores 25 health")
HP_POT3 = Items("Strong Health Potion", "potion", "none", 5, 100, True, 5, {}, {"health": 100}, "Restores 100 health")

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
D_WING = Items("Dragon Wing", "misc", "none", 0, 50, True, 10, {}, {}, "The wing material of a dragon")
D_CLAW = Items("Dragon Claw", "misc", "none", 0, 75, True, 15, {}, {}, "The claw of a dragon, about the size of a rat")
D_TAIL = Items("Dragon Tail", "misc", "none", 0, 100, True, 25, {}, {}, "The tail of a dragon aka chunk of magic meat")

GEM = Items("Gem", "misc", "none", 0, 50, True, 10, {}, {}, "A colourless gem infused with no magic")
C_GEM = Items("Corrupt Gem", "misc", "dark", 3, 40, True, 10, {}, {}, "A black gem infused with dark magic")
F_GEM = Items("Fire Gem", "misc", "fire", 3, 45, True, 10, {}, {}, "A red gem infused with fire magic")
W_GEM = Items("Water Gem", "misc", "water", 3, 45, True, 10, {}, {}, "A blue gem infused with water magic")
E_GEM = Items("Earth Gem", "misc", "earth", 3, 45, True, 10, {}, {}, "A brown-green gem infused with earth magic")
A_GEM = Items("Air Gem", "misc", "air", 3, 45, True, 10, {}, {}, "A white gem infused with air magic")
L_GEM = Items("Light Gem", "misc", "light", 3, 45, True, 10, {}, {}, "A glowing gem infused with light magic")


# Filler Item
NO = Items("NO", "NO", "NO", 0, 0, False, 0, {}, {}, "NO")
