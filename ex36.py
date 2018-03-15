from sys import argv
from sys import exit
from ex36_monster_fight import start_fight

script, name = argv
keys = ['deamon key', 'black key']
gold = 0
door = "none"
def player(name, keys, gold):
    player_name = name
    player_keys = keys
    player_gold = gold

    return player_name, player_keys, player_gold


player_name, player_keys, player_gold = player(name, keys, gold)

#print(player_name)
#print(player_keys)
#print(player_gold)

def crawling(player_name, player_keys, door):
    doors = door
    keys = player_keys
    player = player_name



    def starting_point(doors):
        print("You can see a long corridor. There are three doors. One of the far left, center and one on the right.")
        print("The center and right door seem to point to the north...")
        print("Where do you want to go?")
        doors = str(input("> "))

        if doors == "left":
            print(f"You've choosen the {doors} door. It gently cracks open and you enter a long corridor")
            #you_win()
            print("A monster appears from the darkness! Prepare to fight!")
            start_fight()
            you_win()
        if doors == "right":
            print(f"You've choosen the {doors} door. You open it and see a dark room with two smaller doors.")
            you_win()
        if doors == "center":
            if "deamon key" in keys:
                print(f"The {doors} door is locked. However you've found a key before...it fits! You've used the Deamon Key and unlocked the door.")
                print("You've seen this corridor before...hey, it's the room where it all started!")
                crawling(player, keys, doors)
            else:
                print(f"The {doors} door is locked. None of your keys fits.")
                starting_point(doors)
        else:
            print(f"Sorry, I don't know what '{doors}' means.")
            starting_point(doors)



    starting_point(doors)

def start_game(player_name):
    print(f"Hello, {player_name}! Let's begin our jurney in this deep and scary dungeon!")
    print("You can die here or find a way to get away from here with a huge sack of gold and glory!")
    crawling(player_name, player_keys, door)
def you_win():
    print("YOU WIN MODOFOKO!!!!")
    exit(0)

start_game(player_name)
#crawling(player_name, player_keys, door)
