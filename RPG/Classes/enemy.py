class Enemy:

    #Function called when inicializing class/ instancing object
    def __init__(self, hp, mp):

        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp

    #Getting enemy HP
    def get_hp(self):
        return self.hp