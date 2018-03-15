import random, os
from time import sleep

player_health = 100
player_armor = 50

def clear_screen(numlines=100):
    """ Clear the console.
        numlines in an optional argument used only as a fall-back.
    """
    if os.name == "posix":
        # Unix/Linux/MacOS/BSD/etc
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        # DOS/Windows
        os.system('CLS')
    else:
        # Fallback for other operatin systems.
        print('\n' * numlines)

def da_buffer(buffer_counter):
    internal_buffer = int(buffer_counter)
    if internal_buffer % 5 == 0:
        clear_screen()
    else:
        pass
        #print("NOT yet.")


def monster_fight(player_heal, player_arm, equipment, enchantment_usage):
    turn = 0
    p_h = int(player_health)
    p_a = int(player_armor)
    m_h = 40
    usage = enchantment_usage

    print("Ready to fight...")
    sleep(3)
    clear_screen()
    print("------FIGHT!!!!------\n")

    while (p_h > 0) and (m_h > 0):
        turn = turn + 1
        da_buffer(turn)
        #player_attack = dagger_power()
        #player_attack = player_equipped(left_hand)
        #potrzebuje jakas liczbe, wybrany miecz
        # Player attacking the monster
        if usage == 0:
            equipment = "dagger"
        else:
            pass

        if equipment == "poisoned dagger":
            player_attack = dagger_power('poison', usage)
        elif equipment == "dagger":
            player_attack = dagger_power(0,-1)
        elif equipment == "onehand sword":
            player_attack = onehand_sword_power()
        else:
            player_attack = random.randint(0, 2)

        m_h = m_h - player_attack
        print(f"You attack the monster with and bleed him for {player_attack}. Monster has {m_h} health left.\n")
        usage -= 1
        sleep(0.7)

        if m_h <= 0:
            print(f"You WON and killed the monster! Congratulations! You have gain 100 exp. Your health is {p_h}.")
        else:
            # Monaster attacking the player
            m_a = random.randint(1,10)
            p_h = p_h - m_a
            print(f"Monster hits you for {m_a}. You have {p_h} health left.\n")
            sleep(0.7)

            if p_h <= 0:
                print(f"You LOOSE. The monster has mutilated you. Monster feasts on your carcas.")
            else:
                pass


def dagger_power(enchantment_1, usage):
    ench_1 = str(enchantment_1)
    usage_count = int(usage)
    if usage_count > 0:
        print(f"The poison slips from the dagger for the {usage_count} time..")
    elif usage_count == 0:
        print("The poison slips from the dagger the last time....good luck!")
    else:
        pass

    if ench_1 == "poison":
        print(">>>Poisoned Dagger Attack!<<<")
        poison_dose = random.randint(4, 6)
        dagger = random.randint(1, 3) + poison_dose - (usage_count % 2) # the poison slips a bit after each stab :)
        #dagger = 10
    else:
        print(">>>Normal Dagger Attack!<<<")
        dagger = random.randint(1, 3)
        #dagger = 5
    return dagger # returns INT

def onehand_sword_power():
    print(">>>Onehand sword attack!<<<")
    onehand_sword = random.randint(2, 5)
    return onehand_sword # returns INT


def start_fight():
# Starting the fight...
    print("Choose what weapon to equip before fight:\n")
    print("dagger or onehand sword") # na sztywno, nie ma inventory na razie
    equipment = str(input("> "))
    if equipment == 'dagger':
        print("Apply poison on dagger? yes/no")
        poison_apply = str(input("> "))
        if poison_apply == "yes":
            equipment = str("poisoned dagger")
            enchantment_usage = 5
        else:
            equipment = str("dagger")
            enchantment_usage = 0
    elif equipment == 'onehand sword':
        equipment = str("onehand sword")
        enchantment_usage = 0
    else:
        print("So you want to fight bare hands. OOOK.")
        equipment = str('none')
        enchantment_usage = 0

    #poison = 'poison'
    #player_initial_power = player_equipped(left_hand) # This is INT
    #player_initial_power2 = dagger_power(poison, 0) # This is INT
    #player_initial_power3 = onehand_sword_power() # This is INT
    #print(str(player_initial_power) + " uga buga 1")
    #print(str(player_initial_power2) + " uga buga 2")
    #print(str(player_initial_power3) + " uga buga 3")

    #monster_fight(player_health, player_armor, player_initial_power) # INT, INT, INT
    monster_fight(player_health, player_armor, equipment, enchantment_usage)


#start_fight()
