# should include shops, school, gossip, training, crafting, quests?
import player
import text
import items
p = player
t = text
it = items

hours = 8


def town(person):
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
    inn()


def wander(person):  # Walk around and hear gossip, may run into someone on certain days
    print("You wander around the central square of the town and listen to the world around you...")
    global hours
    if hours < 20:
        t.tgossip()
    else:
        print("   The square appears to be deserted, you listen to the sounds of the fountain and bats flying overhead")
    hours += 1


def shop(person):  # IN DEVELOPMENT
    shops = ["Rissas' Delights", "Caspian's Couture", "Bubbles and Bobs"]  # Food, Clothes, Random Magicish Stuff
    inven1 = []
    inven2 = [it.HAT1, it.HAT2, it.FHAT1, it.FHAT2, it.WHAT1, it.WHAT2, it.EHAT1, it.EHAT2, it.VHAT1, it.VHAT2,
              it.DHAT1, it.DHAT2, it.LHAT1, it.LHAT2]
    inven3 = []
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
                try:
                    you_enter = shops[int(enter)-1]
                    # actual shopping part
                    t.shopTalk(you_enter, 0)
                    while True:
                        t.shopTalk(you_enter, 1)
                        i = 1
                        buyable = []
                        for x in inventories[int(enter) - 1]:
                            if x.element == person.element or x.element == "none":
                                print("     ", str(i)+".", x.name, "-", x.worth, "gold -", str(x.stat)[1:-1],
                                      "\n                   <", x.des)
                                buyable.append(x)
                                i += 1

                        purchase = input("What do you want to buy? ")

                except (TypeError, ValueError, IndexError):
                    print("That's not an option, remember to enter the number beside your choice")
    else:
        print("It's too late for any shops to be open, try coming back tomorrow.")


def craftsmen(person):
    print("can go to the brewer, wizard, armourer")


def school(person):
    print("Learn new spells for gold")


def library(person):
    print("read books on how the world works")


def inn(person):
    print("You can gossip, eat, sleep, and gamble here")


def adventure(person):
    print("Battle monsters or explore the area (and then get attacked by monsters)")


options = {"Wander": wander, "Adventure": adventure, "Shop": shop, "Visit a Craftsman": craftsmen,
           "Visit the School": school, "Visit the Library": library, "Return to Inn": inn}
