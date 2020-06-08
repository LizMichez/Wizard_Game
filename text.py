# all major or very much repeated lines of text, named by when / what they're used for
from random import randint


def tgossip():  # Town Gossip
    gossip = ["My word have you seen what Eliza was wearing lately..... I KNOW!",
              "Isn't it weird how that one shop only shows up on some days.... no im not seeing things!",
              "I heard you can learn new spells at the school... apparently the headmistress is a terror though",
              "What's your favorite colour?.... That's wild mines red!",
              "Guess what, did you know some food from Rissas' can change your stat's? You knew? Impossible!",
              "You're broke again! Well you better hope a craftsman is buying those herbs you gathered!",
              "Oh I love those shoes! From Caspian's? Of course!",
              "Oh Jimmy stop eating that bun! You're getting it all over your clothes!",
              "You got thrown out of class again?! Man same that lady is impossible",
              "This is the end.... station... but i cant moveeee.. away from you.....[He appears to be signing]"]
    choice = randint(0, len(gossip)-1)
    choices = randint(0, len(gossip) - 1)
    print(" "*choices, gossip[choice])

# Pub Gossip
# Event Gossip
