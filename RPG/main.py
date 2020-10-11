#Just run 'python main.py' and good luck!

#TODO HP/ MP bars don't work properly -> game.py: get_status & get_enemy_status

# -*- coding: utf-8 -*-

import random
from Classes.game import background_colors, Person, Magic
from Classes.inventory import Item


#Create dark magic, which deals damage
fire = Magic("Fire", 10, 200, "dark")
thunder = Magic("Thunder", 12, 240, "dark")
blizzard = Magic("Blizzard", 8, 160, "dark")
meteor = Magic("Meteor", 20, 1000, "dark")
earthquake = Magic("Earthquake", 15, 800, "dark")

#Create light magic, which heals
cure = Magic("Cure", 12, 1200, "light")
cure_max = Magic("Max Cure", 25, 3000, "light")
cure_ultra = Magic("Ultra Cure", 50, 6000, "light")

#Create items
potion = Item("Potion", "potion", "Heals 500 HP", 500)
high_potion = Item("High Potion", "potion", "Heals 1500 HP", 1500)
super_potion = Item("Super Potion", "potion", "Heals 4000 HP", 4000)

elixir = Item("Elixir", "elixir", "Fully restores HP and MP of one party member", 9001)
high_elixir = Item("High Elixir", "elixir", "Fully restores party's HP and MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

#Instantiate People
#Players
player_magics = [fire, thunder, blizzard, meteor, cure, cure_max]

player_items = [
    {"item": potion, "quantity": 10}, 
    {"item": high_potion, "quantity": 5}, 
    {"item": super_potion, "quantity": 1},
    {"item": elixir, "quantity": 3},
    {"item": high_elixir, "quantity": 1},
    {"item": grenade, "quantity": 1}
]

player1 = Person("Tenshi", 4670, 140, 80, 35, player_magics, player_items)
player2 = Person("Bibi", 4320, 120, 60, 35, player_magics, player_items)
player3 = Person("Mimikyute", 4830, 170, 95, 35, player_magics, player_items)

players = [player1, player2, player3]

#Enemies
enemy_magics = [fire, meteor, cure_ultra]

enemy1 = Person("Bobokoblin 1", 1200, 130, 600, 325, enemy_magics, [])
enemy2 = Person("Final boss' boss", 20000, 350, 450, 50, enemy_magics, [])
enemy3 = Person("Bobokoblin 2", 1200, 130, 600, 325, enemy_magics, [])

enemies = [enemy1, enemy2, enemy3]

#Start code
runnning = True
i = 0

print("\n" + background_colors.FAIL + background_colors.BOLD + "Enemies appear!" + background_colors.ENDC)

while runnning:

    print("\n===================================\n")

    #print("NAME                 HP                                         MP")
    print("PARTY MEMBERS\n")

    for player in players:
        player.get_status()

    print("\n")

    for enemy in enemies:
        enemy.get_enemy_status()

    for player in players:

        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        #print("You chose " + str(choice))

        #Attack
        if(index == 0):
            damage = player.generate_damage()
            enemy = player.choose_target(enemies)
            
            enemies[enemy].take_damage(damage)
            
            print("\n" + player.name + " attacked " + enemies[enemy].name 
                +  " for " + str(damage) + " points of damage.")

            #Delete enemy from the array if dead
            if(enemies[enemy].get_hp() == 0):
                print("\n" + background_colors.FAIL + enemies[enemy].name + " has "
                + background_colors.BOLD + "died" + background_colors.ENDC)

                del enemies[enemy]

        #Magic
        elif(index == 1):
            player.choose_magic()
            magic_choice = int(input("Choose your magic: ")) - 1

            #Player pressed '0', so we go back to the menu options
            if(magic_choice == -1):
                continue
            
            # magic_damage = player.generate_magic_damage(magic_choice)
            # magic_name = player.get_magic_name(magic_choice)
            # cost = player.get_magic_cost(magic_choice)
            
            magic = player.magic[magic_choice]
            magic_damage = magic.generate_damage()

            current_mp = player.get_mp()

            if(magic.cost > current_mp):
                print(background_colors.FAIL + "\nNot enough MP\n" + background_colors.ENDC)
                continue

            player.reduce_mp(magic.cost)

            if(magic.type == "light"):
                player.heal(magic_damage)
                print(background_colors.OK_BLUE + "\n" + magic.name + " heals for " 
                    + str(magic_damage) + " HP." + background_colors.ENDC)

            elif(magic.type == "dark"):
                enemy = player.choose_target(enemies)
            
                enemies[enemy].take_damage(magic_damage)

                print(background_colors.OK_BLUE + "\n" + magic.name + " deals " 
                    + str(magic.damage) + " points of magical damage to "
                    + enemies[enemy].name + background_colors.ENDC)

                #Delete enemy from the array if dead
                if(enemies[enemy].get_hp() == 0):
                    print("\n" + background_colors.FAIL + enemies[enemy].name + " has "
                    + background_colors.BOLD + "died" + background_colors.ENDC)

                    del enemies[enemy]

        #Item
        elif(index == 2):
            player.choose_item()
            item_choice = int(input("Choose your item: ")) - 1

            #Player pressed '0', so we go back to the menu options
            if(item_choice == -1):
                continue

            if(player.items[item_choice]["quantity"] == 0):
                print(background_colors.FAIL + "\n" + "None left." + background_colors.ENDC)

            item = player.items[item_choice]["item"]
            player.items[item_choice]["quantity"] -= 1

            if(item.type == "potion"):
                player.heal(item.prop)
                print(background_colors.OK_GREEN + "\n" + item.name + " heals for " 
                    + str(item.prop) + " HP." + background_colors.ENDC)

            elif(item.type == "elixir"):

                if(item.name == "High Elixir"):
                    for p in players:
                        p.hp = p.max_hp
                        p.mp = p.max_mp
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                
                print(background_colors.OK_GREEN + "\n" + item.name + " fully restores HP/MP." 
                    + background_colors.ENDC)

            elif(item.type == "attack"):
                enemy = player.choose_target(enemies)
            
                enemies[enemy].take_damage(item.prop)

                print(background_colors.FAIL + "\n" + item.name + " deals " 
                    + str(item.prop) + " points of damage to "
                    + enemies[enemy].name + background_colors.ENDC)

                #Delete enemy from the array if dead
                if(enemies[enemy].get_hp() == 0):
                    print("\n" + background_colors.FAIL + enemies[enemy].name + " has "
                    + background_colors.BOLD + "died" + background_colors.ENDC)

                    del enemies[enemy]

    #Check if battle is over
    #Player lose condition
    defeated_players = 0

    for player in players:
        if(player.get_hp() == 0):
            defeated_players += 1
            del player

    if(defeated_players == len(players) - 1):
        print(background_colors.FAIL + "YOU DIED!" + background_colors.ENDC)
        runnning = False

    #Player win condition
    defeated_enemies = 0

    for enemy in enemies:    
        if(enemy.get_hp() == 0):
            defeated_enemies += 1
    
    if(defeated_enemies == len(enemies) - 1):
        print(background_colors.OK_GREEN + "You win!" + background_colors.ENDC)
        runnning = False
    

    #Enemy attack phase
    for enemy in enemies:
        enemy_choice = random.randrange(0, 2)

        #Attack
        if(enemy_choice == 0):
            target = random.randrange(0, len(players))
            enemy_damage = enemy.generate_damage()
            players[target].take_damage(enemy_damage)

            print("\n" +  background_colors.FAIL + enemy.name + background_colors.ENDC 
            + " attacks " + players[target].name + " for " + str(enemy_damage) + " points of damage.") 

        #Magic
        elif(enemy_choice == 1):
            magic, magic_damage = enemy.choose_enemy_magic()
            enemy.reduce_mp(magic.cost)

            if(magic.type == "light"):
                enemy.heal(magic_damage)

                print(background_colors.OK_BLUE + "\n" + magic.name + " heals " 
                + enemy.name + " for " + str(magic_damage) + " HP." + background_colors.ENDC)

            elif(magic.type == "dark"):
                target = random.randrange(0, len(players))
            
                players[target].take_damage(magic_damage)

                print(background_colors.FAIL + "\n" + enemy.name + "'s " + background_colors.ENDC
                    + magic.name + " deals " 
                    + str(magic.damage) + " points of magical damage to "
                    + players[target].name)

                #Delete player from the array if dead
                if(players[target].get_hp() == 0):
                    print("\n" + background_colors.OK_GREEN + players[target].name + background_colors.ENDC 
                    + background_colors.FAIL + " has "
                    + background_colors.BOLD + "died" + background_colors.ENDC)

                    del players[target]

            # print("\n" + enemy.name + " chose " + str(magic) + " damage is" + str(magic_damage))