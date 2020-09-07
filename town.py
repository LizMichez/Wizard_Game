# should include shops, school, gossip, training, crafting, quests?
from random import randint
import player
import text
import items
import monsters
import battle

p = player
t = text
it = items
m = monsters
b = battle

hours = 8


def town(person):
    global hours
    while hours < 22:
        print("Welcome to town! While here you can..")
        leoptions = []
        ii = 0
        for x in options:
            ii += 1
            print("     ", str(ii)+".", x)
            leoptions.append(x)
        try:
            choice = int(input("What will you do? : "))
            if choice in range(1, len(options)):
                options[leoptions[choice-1]](person)
            else:
                print("You have to pick an actual option you know")
        except (TypeError, ValueError):
            print("Enter the number corresponding to your choice")

    print("Tired after a long day you head to the Inn")
    inn(person)


def wander(person):  # Walk around and hear gossip, may run into someone on certain days  - - - IN PROGRESS
    global hours
    print("You wander around the central square of the town and listen to the world around you...")
    if hours < 20:
        t.tgossip()
    else:
        if person.element == "dark" and 5 == 3:  # TEMPORARY CONDITION, WILL BE HAS ENCOUNTERED TRAINER
            print("Encounter person")
        elif person.element == "dark":
            print("Train with person")
        else:
            print("    The square appears to be deserted, you listen to the fountain and bats flying overhead")
    hours += 1


def shop(person):
    global hours
    shops = ["Rissas' Delights", "Caspian's Couture", "Bubbles and Bobs"]  # Food, Clothes, Random Magicish Stuff
    inven1 = [it.B_MUFF, it.C_MUFF, it.F_MUFF, it.T_SOUP, it.R_SOUP, it.F_STEAK, it.P_STEAK, it.W_DRINK]
    inven2 = [it.HAT1, it.HAT2, it.F_HAT1, it.F_HAT2, it.W_HAT1, it.W_HAT2, it.E_HAT1, it.E_HAT2, it.V_HAT1, it.V_HAT2,
              it.D_HAT1, it.D_HAT2, it.L_HAT1, it.L_HAT2, it.GLASS1, it.GLASS2, it.SHIRT1, it.SHIRT2, it.SHIRT3,
              it.COAT1, it.COAT2, it.F_COAT1, it.F_COAT2, it.W_COAT1, it.W_COAT2, it.E_COAT1, it.E_COAT2, it.V_COAT1,
              it.V_COAT2, it.D_COAT1, it.D_COAT2, it.L_COAT1, it.L_COAT2, it.SHOES1, it.SHOES2, it.F_SHOES1,
              it.W_SHOES1, it.E_SHOES1, it.V_SHOES1, it.D_SHOES1, it.L_SHOES1]
    inven3 = [it.AM1, it.AM2, it.BR1, it.BR2, it.RNG1, it.RNG2, it.B_FRUIT, it.R_FRUIT]
    inventories = [inven1, inven2, inven3]
    if hours < 19:
        while True:
            print("Walking in the shopping district you see:")
            i = 1
            for x in shops:
                print(str(i)+". ", x)
                i += 1
            enter = input("Which one do you enter? [enter N to leave] : ")
            if enter == "n" or enter == "N":
                print("You return to the town square")
                return
            else:
                hours += 1
                try:  # actual shopping part
                    you_enter = shops[int(enter)-1]
                    t.shopTalk(you_enter, 0)
                    while True:
                        t.shopTalk(you_enter, 1)
                        i = 1
                        buyable = []
                        for x in inventories[int(enter) - 1]:
                            if x.element == person.element or x.element == "none":
                                print("     ", str(i)+".", x.name, "-", x.worth, "gold :", str(x.stat)[1:-1],
                                      "\n                   -", x.des)
                                buyable.append(x)
                                i += 1
                        purchase = input("What do you want to buy? [enter N to leave]")
                        try:
                            if purchase == "n" or purchase == "N":
                                t.shopTalk(you_enter, 3)
                                print("You return to the town square")
                                return
                            else:
                                t.shopTalk(you_enter, 2)
                                if person.gold > buyable[int(purchase)-1].worth and len(person.inventory) < person.inventoryCap:
                                    person.gold -= buyable[int(purchase)-1].worth
                                    person.acquire(buyable[int(purchase)-1])
                                    if int(enter) == 1:
                                        person.consume(buyable[int(purchase)-1])
                                elif person.gold < buyable[int(purchase)-1].worth:
                                    print("You can't afford this item")
                                elif len(person.inventory) >= person.inventoryCap:
                                    print("Your inventory is too full for this item, deal with that then try again")
                        except(TypeError, ValueError, IndexError):
                            print("That's not an item or an exit, lets try this again")

                except (TypeError, ValueError, IndexError):
                    print("That's not an option, remember to enter the number beside your choice")
    else:
        print("It's too late for any shops to be open, try coming back tomorrow.")


def craftsmen(person):
    global hours
    print("can go to the brewer, wizard, armourer, butcher")


def school(person):
    global hours
    print("Learn new spells for gold")


def library(person):  # Books still in development, library is fine
    global hours
    print("You walk into the old library with beautiful wood carvings and shelves of books")
    while True:
        books = ["History of Magic", "Monster Guide", "Dueling - The Basics", "Introduction to Plants", "Town History"]
        print("On the shelves you see:")
        for x in books:
            print("       " + str(books.index(x) + 1) + ".", x)
        choice = input("What do you want to read? [enter N to leave]")
        try:
            if choice == "n" or choice == "N":
                print("You return to the town square.")
                return
            else:
                page = 0
                while True:
                    progress = t.readLibrary(int(choice)-1, page)
                    if progress == "done":
                        break

                    cont = input("Do you want to continue? [Y/N] ")
                    if cont == "y" or cont == "Y":
                        page += 1
                    elif cont == "n" or cont == "N":
                        print("You close the book and put it back on the shelf")
                        break
                    else:
                        print("Since you clearly can't read, you return the book to the shelf")
        except(ValueError, TypeError, IndexError):
            print("That's not an option or the exit, lets try this again")


def inn(person):
    global hours
    print("You can gossip, eat, sleep, and gamble here")


def adventure(person):  # WEIRDLY BROKEN / ROYALLY FUCKED
    global hours
    places = ["Grassy Fields", "Murky Swamp", "Forlorn Mountains", "Abandoned Caves"]
    odds = [[1, 2, 3], [3, 2, 1], [2, 3, 1], [3, 2, 1]]  # battle, encounter, find

    print("You walk up to the village gate, there are four teleport pedestals.")
    while True:
        print("Do you go to the:")
        for x in places:
            print("       " + str(places.index(x) + 1) + ".", x)
        choice = input("Where do you want to go? [enter N to leave]")
        if choice == "n" or choice == "N":
            print("You walk back to the town square.")
            return

        try:
            place = int(choice)-1
            if person.level < place*4:
                print("You are stopped by the guards at the gate who inform you your level is too low for this area.")
            else:
                print("You are warped to the", places[place] + ".")
                break
        except(ValueError, TypeError, IndexError):
            print("That's not an option or the exit, lets try this again")

    while True:
        print("You can explore until the 20th, hour. It is currently the", str(hours) + "th hour.")
        cont = input("Enter Y to explore or N to return to town : ")
        if cont == "N" or cont == "n":
            print("You return to town.")
            return
        elif cont == "Y" or cont == "y":
            num = randint(0, 10)  # Used to choose what you do based on areas encounter odds
            if num == 1:
                event = odds[place].index(1)
            elif num <= 4:
                event = odds[place].index(2)
            else:
                event = odds[place].index(3)

            if event == 0:  # Battle
                hours += 1
                state = b.battle(person, m.Monster_Loc[place][randint(0, len(m.Monster_Loc[place])-1)])
                if state == "win" or state == "ran":
                    pass
                else:
                    hours += 1
                    return
            elif event == 1:  # Encounter Animal
                hours += 0.5
                b.encounter(person, m.Animal_Loc[place][randint(0, len(m.Animal_Loc[place])-1)])
            elif event == 2:  # Find Plant
                hours += 0.5
                plant = it.Location_P[place][randint(0, len(it.Location_P[place])-1)]
                person.acquire(plant)
        else:
            print("That's not an option, lets try this again")

        if hours >= 20:
            print("It is now the", hours, "hour, you are warped back to town.")


options = {"Wander": wander, "Adventure": adventure, "Shop": shop, "Visit a Craftsman": craftsmen,
           "Visit the School": school, "Visit the Library": library, "Return to Inn": inn}
