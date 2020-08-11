# all major or very much repeated lines of text, named by when / what they're used for
from random import randint


def tgossip():  # Town Gossip
    gossip = ["My word have you seen what Eliza was wearing lately..... I KNOW!",
              "Isn't it weird how that one shop only shows up on some days.... no I'm not seeing things!",
              "I heard you can learn new spells at the school... apparently the headmistress is a terror though",
              "What's your favorite colour?.... That's wild mines red!",
              "Guess what, did you know some food from Rissas' can change your stat's? You knew? Impossible!",
              "You're broke again! Well you better hope a craftsman is buying those herbs you gathered!",
              "Oh I love those shoes! From Caspian's? Of course!",
              "Oh Jimmy stop eating that bun! You're getting jam all over your clothes!",
              "You got thrown out of class again?! Man same that lady is impossible",
              "This is the end.... station... but I can't moveeee.. away from you.....[He appears to be signing]",
              "Did you see that man lurking around the fountain at night.... looked almost like a ghost",
              "What did I tell you about going out that late?! You never know what type of creep you could run into"]
    choice = randint(0, len(gossip)-1)
    spaces = " "*randint(0, len(gossip) - 1)
    print(spaces, "- - -", gossip[choice])

# Pub Gossip
# Event Gossip


def shopTalk(store, stage):
    greetings = ["[A large, half snake woman is sitting behind a counter in an oddly frilly restaurant]\n"
                 "Why hello there darling, welcome to Rissasssss, let me know which delightssss you want to buy.",
                 "[You enter to see a well dressed satyr in an incredibly well kept clothing store]\n"
                 "Greetings, yes I can see why you came here, I'm sure any of our wares would help improve.... that.",
                 "[An oddly dressed old man is in the back of a horribly cluttered room filled with bits and bobs]\n"
                 "Why are you here.... a shop? Ah right well I suppose you can look around."]
    browsing = ["The menu reads:", "The items available in your size and type are:", "He appears to be selling:"]
    buying = ["Oh that looks ssssssimply ssssscruptiouse!", "Yes that would definitely improve your state.", "Buy that?"
              "ah yes I suppose you can do that."]
    leaving = ["Have a nice day ssssweety!", "Tally Ho!", "...[The man appears to be ignoring you]"]

    shops = ["Rissas' Delights", "Caspian's Couture", "Bubbles and Bobs"]
    stages = [greetings, browsing, buying, leaving]
    storeOT= shops.index(store)

    print(stages[stage][storeOT])


def readLibrary(book, page):
    history_of_magic = ["page 1", "second page", "3", "IV", "Cinque"]
    monster_dictionary = []
    dueling_the_basics = []
    intro_to_herbology = []
    town_history = []

    books = [history_of_magic, monster_dictionary, dueling_the_basics, intro_to_herbology, town_history]
    if int(page) > len(books[book])-1:
        print(books[book][page])
        print("You have finished the book and return it to its shelf.")
        return "done"
    else:
        print(books[book][page])

