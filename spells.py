# all spells and attacks used by both monsters and player, effects, and how they use the things stats
class Spell:
    def __init__(self, name, element, level, mana_cost, base_damage, base_def, drain, healing, recoil, description):
        self.name = name
        self.element = element
        self.lv = level
        self.mana = mana_cost
        self.base_dam = base_damage
        self.base_def = base_def
        self.drain = drain
        self.healing = healing
        self.recoil = recoil
        self.des = description


# Basic Spells

# Fire (A1, A2, H1, A3, D1, A4)
FIRE_A1 = Spell("Fire Ball", "fire", 0, 10, 15, 0, 0, 0, 0, "Shoot a small ball of fire")
FIRE_A2 = Spell("Fire Blast", "fire", 3, 20, 30, 0, 0, 0, 0, "Shoot a spray of flames")
FIRE_A3 = Spell("Fire Bomb", "fire", 9, 50, 100, 0, 0, 0, 20, "Create a huge explosion of flame")
FIRE_A4 = Spell("Inferno", "fire", 15, 75, 125, 0, 0, 0, 0, "Summon a huge column of fire")

FIRE_D1 = Spell("Fire Tornado", "fire", 12, 40, 50, 15, 0, 0, 0, "Surround yourself with a swirling wall of flame")

FIRE_H1 = Spell("Warm Rays", "Fire", 6, 25, 5, 0, 0, 25, 0, "Warm healing rays")

# Water

# Earth

# Air

# Dark

# Light
