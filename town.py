# should include shops, school, gossip, training, crafting, quests?
# import player
import text

hours = 8


def town():
    while hours < 18:
        print("Welcome to town! While here you can..")
        leoptions = []
        ii = 0
        for x in options:
            ii += 0
            print("     ", str(ii)+".", x)
            leoptions.append(x)
        try:
            choice = int(input("What will you do? : "))
            if choice in range(1, len(options)-1):
                options[leoptions[choice-1]]()
            else:
                print("You have to pick an actual option you know")
        except (TypeError, ValueError):
            print("Enter the number corresponding to your choice")


def wander():  # Walk around and hear gossip, may run into someone on certain days
    print("You wander around the central square of the town and listen to the world around you...")
    global hours
    if hours < 20:
        text.tgossip()
    else:
        print("   The square appears to be deserted, you listen to the sounds of the fountain and bats flying overhead")
    hours += 1


def shop():
    print("Choose from the food shop, magic shop, and clothes shop")


def craftsmen():
    print("can go to the brewer, wizard, armourer")


def school():
    print("Learn new spells for gold")


def library():
    print("read books on how the world works")


def inn():
    print("You can gossip, eat, sleep, and gamble here")


def adventure():
    print("Battle monsters or explore the area (and then get attacked by monsters)")


options = {"Wander": wander, "Adventure": adventure, "Shop": shop, "Visit a Craftsman": craftsmen,
           "Visit the School": school, "Visit the Library": library, "Return to Inn": inn}
