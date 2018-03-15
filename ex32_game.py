def Gamestart():
    print("""Dungeon fighter 9000""")
    print("What's your name brave adventurer?")
    player_name =str(input("Name: "))
    print(f"Aaaah...I see...I've heard that name before...{player_name}.")
    #Dungeon_difficulty()
    return player_name

def Dungeon_difficulty():
    print(f"Choose the Dungeon difficulty: low, mid, hard")
    difficulty = str((input("> ")))
    if difficulty == 'low':
        print(f"You've choosen: {difficulty} difficulty. It won't hurt much then..")
        number_of_monsters = 5
        return difficulty, number_of_monsters
    elif difficulty == 'mid':
        print(f"You've choosen: {difficulty} difficulty. It'll bite quite a bit..")
        number_of_monsters = 10
        return difficulty, number_of_monsters
    elif difficulty == 'hard':
        print(f"You've choosen: {difficulty} difficulty. Sure you can handle it?")
        number_of_monsters = 20
        return difficulty, number_of_monsters
    else:
        print("Can't tell how hard you want to get grinded. Type again..")
        Dungeon_difficulty()

def player_inventory_show():
    inventory = {"slot1": "Sword", "slot2": "Health Potion", "slot3": "Mana Potion"}
    print(list(inventory.values()))

def Monster(monsters):
    print("M " * monsters)

def Map_builder(monsters, difficulty):
    if difficulty == 'low' or difficulty == 'mid':
        map_width = 40
        map_height = 40
    else:
        map_width = 60
        map_height = 50

    map = [[0 for x in range(map_width) for y in range(map_height)]]
    map[0][0] = 1
#    for i in range(map_width):
#        for j in range(map_height):
#            print(map[i][j])




Gamestart()
difficulty, number_of_monsters = Dungeon_difficulty()
player_inventory_show()
print(difficulty, number_of_monsters)
#Monster(number_of_monsters)
Map_builder(number_of_monsters, difficulty)


















#    def Map_builder(map_width, map_height, monsters):
#
#        enemies = monsters
#        def Monster_spawn(enemies):
#
#            if enemies
#                monster_appear = "M "
#                num_of_mon_left =
#            else:
#                monster_appear = " "
#            return monster_appear, num_of_mon_left
#
#        print("=" * map_width)
#
#        for i in range(int(map_height / 2)):
#            print("|", monster_appear * int(((map_width / 1) - 4)), "|")
#            enemies -= 1
#            Monster_spawn(enemies)
#
#        print("=" * map_width)
