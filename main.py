import player
import battle
import monsters
import spells
import town

p = player
b = battle
m = monsters
s = spells
tow = town

# runs story and literally everything, currently being used for testing
P1 = player.Character(10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100)
P1.name = "Bean"
P1.element = "dark"
P1.level = 2
P1.learn_spell(s.DARK_A1)
P1.learn_spell(s.DARK_A2)

P1.gold += 10000

tow.town(P1)
