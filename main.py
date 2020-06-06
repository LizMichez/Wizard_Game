import player, items, battle, monsters, spells
b = battle
m = monsters
s = spells

# runs story and literally everything

P1 = player.Character(10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100)
P1.name = "Bean"
P1.element = "dark"

P1.acquire(items.DA1)
P1.acquire(items.ROCK2)
P1.acquire(items.ROCK3)
# P1.open_inventory()
# P1.equip(items.LA1)
# P1.equip(items.DA1)
# P1.open_inventory()
# P1.open_clothes()
# P1.open_stats()
P1.learn_spell(s.DARK_A1)
b.battle(P1, m.SLIME)
