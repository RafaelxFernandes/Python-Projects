#Imports
import random

class Enemy:

    #Enemy health points
    enemy_hp = 150

    #Function called when initializing class/ instancing object
    def __init__(self, min_enemy_atk, max_enemy_atk):

        self.min_enemy_atk = min_enemy_atk
        self.max_enemy_atk = max_enemy_atk


    #Damage given by enemy, random range from minimum to maximum
    def get_min_enemy_atk(self):

        print(self.min_enemy_atk)


#Creating instances of Enemy
enemy1 = Enemy(40, 60)
enemy1.get_min_enemy_atk()

enemy2 = Enemy(30, 40)
enemy2.get_min_enemy_atk()