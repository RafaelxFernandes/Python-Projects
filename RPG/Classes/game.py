import random, math
from Classes.magic import Magic 

class background_colors:

    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:

    def __init__(self, name, hp, mp, attack, defense, magic, items):

        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.attack_high = attack + 10
        self.attack_low = attack - 10
        self.defense = defense
        self.magic = magic
        self.items = items

        self.actions = ["Attack", "Magic", "Items"]


    def generate_damage(self):
        return random.randrange(self.attack_low, self.attack_high)


    # def generate_magic_damage(self, i):

    #     magic_low = self.magic[i]["damage"] - 5
    #     magic_high = self.magic[i]["damage"] + 5

    #     return random.randrange(magic_low, magic_high)


    def take_damage(self, damage):
        
        self.hp -= damage

        if(self.hp < 0):
            self.hp = 0
        
        return self.hp


    def heal(self, damage):

        self.hp += damage

        if(self.hp > self.max_hp):
            self.hp = self.max_hp

    
    def get_hp(self):
        return self.hp

    
    def get_max_hp(self):
        return self.max_hp

    
    def get_mp(self):
        return self.mp


    def get_max_mp(self):
        return self.max_mp


    def reduce_mp(self, cost):
        self.mp -= cost


    # def get_magic_name(self, i):
    #     return self.magic[i]["name"]


    # def get_magic_cost(self, i):
    #     return self.magic[i]["cost"]


    def choose_action(self):

        print("\n" + background_colors.OK_BLUE + background_colors.BOLD + 
            self.name + " actions" + background_colors.ENDC)

        i = 1

        for item in self.actions:
            print("    " + str(i) + ": " + str(item))
            i += 1

    
    def choose_magic(self):

        print("\n" + background_colors.OK_BLUE + background_colors.BOLD + "Magics" + background_colors.ENDC)

        i = 1

        for magic in self.magic:
            print("    " + str(i) + ": " + magic.name 
            + " " * (9 - len(magic.name))
            + "| Cost: " + str(magic.cost))
            i += 1


    def choose_item(self):

        print("\n" + background_colors.OK_GREEN + background_colors.BOLD + "Items: " + background_colors.ENDC)

        i = 1

        for item in self.items:
            print("    " + str(i) + ". " + item["item"].name + ": " + item["item"].description 
                + " (x" + str(item["quantity"]) + ")" + background_colors.ENDC)
            i += 1


    def choose_target(self, enemies):

        i = 1

        print("\n" + background_colors.FAIL + background_colors.BOLD + 
            "    TARGET:" + background_colors.ENDC)

        for enemy in enemies:
            if(enemy.get_hp() != 0):
                print("        " + str(i) + ": " + enemy.name)
                i += 1

        choice = int(input("    Choose target: ")) - 1

        return choice

    
    def get_status(self):

        hp_string = str(self.hp) + "/" + str(self.max_hp)
        mp_string = str(self.mp) + "/" + str(self.max_mp)

        print(background_colors.BOLD + self.name + ":" + " " * (10 - len(self.name)) 
            + background_colors.OK_GREEN 
            + "HP: " + hp_string + background_colors.ENDC + "   "
            + background_colors.BOLD 
            + background_colors.OK_BLUE 
            + "MP: " + mp_string + background_colors.ENDC)


    def get_enemy_status(self):

        hp_string = str(self.hp) + "/" + str(self.max_hp)

        print(background_colors.BOLD + self.name + ":" + " " * (17 - len(self.name)) 
            + background_colors.FAIL
            + hp_string 
            + background_colors.ENDC)


    def choose_enemy_magic(self):
        
        magic_choice = random.randrange(0, len(self.magic))
        magic = self.magic[magic_choice]
        magic_damage = magic.generate_damage()

        porcentage = (self.hp/ self.max_hp) * 100

        if(self.mp < magic.cost or magic.type == "light" and porcentage > 50):
            self.choose_enemy_magic()
        else:
            return magic, magic_damage



    #TODO once you get hit or use magic, your HP/MP bar gets all red
    #u"\u2588 is the 219th ASCII character
    # def get_status(self):

    #     hp_bar_total = 25
    #     mp_bar_total = 10

    #     hp_bar_count = int(math.floor((self.hp/ self.max_hp) * hp_bar_total))
    #     hp_bar = background_colors.OK_GREEN + u"\u2588" * hp_bar_count
    #     negative_hp = background_colors.FAIL + u"\u2588" * (hp_bar_total - hp_bar_count)

    #     mp_bar_count = int(math.floor((self.mp/ self.max_mp) * mp_bar_total))
    #     mp_bar = background_colors.OK_BLUE + u"\u2588" * mp_bar_count
    #     negative_mp = background_colors.FAIL + u"\u2588" * (mp_bar_total - mp_bar_count)    

    #     hp_string = str(self.hp) + "/" + str(self.max_hp) + " "
    #     current_hp = ""

    #     if(len(hp_string) < 10):
    #         decreased_hp = 10 - len(hp_string)

    #         while(decreased_hp > 0):

    #             current_hp += " "
    #             decreased_hp -= 1

    #         current_hp += hp_string

    #     else:
    #         current_hp = hp_string

    #     mp_string = str(self.mp) + "/" + str(self.max_mp) + " "
    #     current_mp = ""

    #     if(len(mp_string) < 8):
    #         decreased_mp = 8 - len(mp_string)

    #         while(decreased_mp > 0):

    #             current_mp += " "
    #             decreased_mp -= 1

    #         current_mp += mp_string

    #     else:
    #         current_mp = mp_string

    #     print("                      _________________________                   __________")

    #     print(background_colors.BOLD + self.name + ":" + " " * (10 - len(self.name)) 
    #         + current_hp + "|" + background_colors.OK_GREEN 
    #         + hp_bar + negative_hp
    #         + background_colors.ENDC + background_colors.BOLD + "|         " 
    #         + current_mp + "|" + background_colors.OK_BLUE 
    #         + mp_bar + negative_mp
    #         + background_colors.ENDC + background_colors.BOLD + "|\n" 
    #         + background_colors.ENDC)
    

    # #TODO once enemy gets hit, its HP bar turns blank
    # def get_enemy_status(self):

    #     hp_bar = ""
    #     hp_bar_count = (self.hp/ self.max_hp) * 50

    #     while hp_bar_count > 0:

    #         hp_bar += u"\u2588"
    #         hp_bar_count -= 1

    #     while len(hp_bar) < 50:
    #         hp_bar += " "

    #     hp_string = str(self.hp) + "/" + str(self.max_hp) + " "
    #     current_hp = ""

    #     if(len(hp_string) < 12):
    #         decreased_hp = 12 - len(hp_string)

    #         while(decreased_hp > 0):

    #             current_hp += " "
    #             decreased_hp -= 1

    #         current_hp += hp_string

    #     else:
    #         current_hp = hp_string

    #     print("                               HP")
    #     print("                               __________________________________________________")

    #     print(background_colors.BOLD + self.name + ":" + " " * (17 - len(self.name)) 
    #         + current_hp + "|" + background_colors.FAIL
    #         + hp_bar 
    #         + background_colors.ENDC + background_colors.BOLD + "|\n" 
    #         + background_colors.ENDC)