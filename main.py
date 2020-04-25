import player
import items
# import text
# import battle
# import town

# runs story and literally everything

P1 = player.Character(10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100)
P1.acquire(items.DA1)
P1.open_inventory()
P1.equip(items.DA1)
P1.open_inventory()
P1.open_clothes()

