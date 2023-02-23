import random

def game(player):
    # m = ("r","p","s")
    d = {"r" : "rock", "p" : "paper", "s" : "scissors"}
    npc = random.choice(list(d.keys()))
    # npc = m[random.randrange(len(m))]
    if player == npc:
        result = "tie"
    elif player == "r" and npc == "s":
        result = "win"
    elif player == "p" and npc == "r":
        result = "win"
    elif player == "s" and npc == "p":
        result = "win"
    else:
        result = "lose"
    print("you: {} <-> npc: {} == {}".format(d[player], d[npc], result))

while True:
    player = input("[r]ock, [p]aper, [s]cissors, e[x]it :")
    if player == "x":
        break
    else:
        game(player)


