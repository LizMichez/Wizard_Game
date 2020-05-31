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

# Water (A1, A2, H1, D1, A3, A4)
WATER_A1 = Spell("Hail", "water", 0, 10, 15, 0, 0, 0, 0, "Drop small balls of ice from the sky")
WATER_A2 = Spell("Bubble", "water", 3, 15, 25, 0, 0, 0, 0, "Surround your opponent with a bubble of water")
WATER_A3 = Spell("Ice Spikes", "water", 12, 50, 75, 10, 0, 0, 0, "Impale opponent with ice spikes")
WATER_A4 = Spell("Torrent", "water", 15, 75, 100, 0, 0, 25, 0, "Unleashes a torrent of mana infused water")

WATER_D1 = Spell("Ice Wall", "water", 9, 40, 0, 100, 0, 0, 0, "Create an ice wall")

WATER_H1 = Spell("Transfusion", "water", 6, 30, 30, 0, 0, 40, 0, "Drains fluid from opponent while replenishing you")

# Earth (A1, D1, A2, A3, D2, A4)
EARTH_A1 = Spell("Rock Throw", "earth", 0, 10, 15, 0, 0, 0, 0, "Picks up a rock and throws it, but with magic")
EARTH_A2 = Spell("Mud Blast", "earth", 6, 20, 30, 5, 0, 0, 0, "Summon a blast of high pressure mud")
EARTH_A3 = Spell("Cliff Jump", "earth", 9, 40, 60, 0, 0, 0, 0, "Make a cliff under opponent then destroy the cliff")
EARTH_A4 = Spell("Quake", "earth", 15, 75, 175, 0, 0, 0, 50, "Creates an earthquake in the surrounding area")

EARTH_D1 = Spell("Rock Wall", "earth", 3, 15, 0, 30, 0, 0, 0, "Create a wall of rock")
EARTH_D2 = Spell("Stalagmites", "earth", 12, 60, 45, 60, 0, 0, 0, "Creates a field of ground spikes")

# Air (A1, A2, A3, H1, A4, A5)
AIR_A1 = Spell("Gust", "air", 0, 10, 15, 0, 0, 0, 0, "Blows the opponent over. Hard.")
AIR_A2 = Spell("Air Blades", "air", 3, 25, 35, 0, 0, 0, 0, "Hurls blades of high pressure air")
AIR_A3 = Spell("Air Ball", "air", 6, 30, 50, 0, 0, 0, 10, "Hurls a ball of high pressure air, can cause flying rocks")
AIR_A4 = Spell("Tornado", "air", 12, 55, 130, 0, 0, 0, 40, "Creates a tornado around you, can cause flying trees")
AIR_A5 = Spell("Gravity", "air", 15, 100, 175, 0, 0, 0, 0, "Lift opponent up to the clouds then drop them")

AIR_H1 = Spell("Healing Gust", "air", 9, 35, 15, 0, 0, 35, 0, "Pushes opponents away and surrounds you with pure air")

# Dark (A1, A2, A3, A4, D1, A5)
DARK_A1 = Spell("Dark Ball", "dark", 0, 10, 15, 0, 10, 0, 0, "Hurl a ball of dark energy")
DARK_A2 = Spell("Shadow Tether", "dark", 3, 25, 30, 0, 20, 0, 0, "Control opponent through their shadow")
DARK_A3 = Spell("Shadow Claw", "dark", 6, 35, 50, 0, 0, 0, 0, "Creates tearing claws of shadow")
DARK_A4 = Spell("Void Blast", "dark", 9, 50, 100, 0, 75, 0, 0, "Summon a blast of pure darkness")
DARK_A5 = Spell("Eclipse", "dark", 15, 125, 125, 0, 125, 0, 0, "Blot out the sun and drain the life from enemies")

DARK_D1 = Spell("Warp", "dark", 12, 125, 0, 1000, 0, 0, 50, "Teleports you away from opponents attack")

# Light (A1, H1, D1, H2, D2, A2)
LIGHT_A1 = Spell("Light Beam", "light", 0, 10, 25, 0, 0, 0, 0, "Summon a beam of light")
LIGHT_A2 = Spell("Heaven Ray", "light", 15, 150, 250, 0, 0, 20, 0, "Concentrates all the light in the area into a beam")

LIGHT_D1 = Spell("Light Screen", "light", 6, 30, 10, 40, 0, 0, 0, "Create a sharp light barrier")
LIGHT_D2 = Spell("Prism", "light", 12, 100, 50, 150, 0, 50, 0, "Creates prisms of light around everyone")

LIGHT_H1 = Spell("Healing Rays", "light", 3, 20, 5, 0, 0, 30, 0, "Summon warm rays of light")
LIGHT_H2 = Spell("Starfall", "light", 9, 50, 20, 0, 0, 80, 0, "Concentrated light particles fall on the area")

# Monster


class Attack:
    def __init__(self, name, damage, defense, recoil):
        self.name = name
        self.damage = damage
        self.defense = defense
        self.recoil = recoil


BDSLAM = Attack("Body Slam", 25, 0, 5)
BITE = Attack("Bite", 20, 0, 0)
ARROW = Attack("it's bow to fire an arrow", 30, 0, 0)
SCRATCH = Attack("Scratch", 20, 0, 0)
SLASH = Attack("Slash", 35, 0, 0)
STHROW = Attack("Slime Throw", 15, 0, 0)
HIT = Attack("Punch", 15, 0, 0)
STAB = Attack("Stab", 30, 0, 0)
CLUB = Attack("it's club to hit you", 40, 0, 0)

BLOCK = Attack("Block", 0, 50, 0)
