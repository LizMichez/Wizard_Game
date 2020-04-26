import player
import items
# import text
# import battle
# import town

# runs story and literally everything

P1 = player.Character(10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100)
P1.name = "Bean"
P1.element = "dark"
print(P1.element)
print(items.DA1.element)
P1.acquire(items.DA1)
P1.open_inventory()
P1.equip(items.DA1)
P1.open_inventory()
P1.open_clothes()
P1.open_stats()
