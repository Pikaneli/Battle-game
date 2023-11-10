import random
import pprint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items, exp, lvl, maxexp = 120):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name
        self.exp = exp
        self.lvl = lvl
        self.maxexp = 120

    def generate_damage(self):
        critical_chance = random.randint(1, 100)
        if critical_chance <= 5:
            print("\n" + bcolors.WARNING + bcolors.UNDERLINE + "Critical hit!" + bcolors.ENDC)
            return (random.randrange(self.atkl, self.atkh))*2
        else:
            return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost
        
    def get_level(self):
        return self.lvl
    
    def get_exp(self):
        return self.exp
    
    def increase_stats(self):
        self.maxhp += self.lvl*(100)
        self.maxmp += self.lvl*(15)
        self.atkl += self.lvl*(10)
        self.atkh += self.lvl*(10)
        self.df += self.lvl*(10)
        
    def increase_xp(self):
        level = self.lvl
        xp = self.exp
        if (level < 2):
            xp += random.randint(5,8)
        elif (level < 3):
            xp += random.randint(8,14)
        elif (level < 4):
            xp += random.randint(15,30)
        else:
            xp += random.randint(30,50)
        self.exp = xp
        self.lvl = level
    
    def increase_lvl(self):
        level = self.lvl
        xp = self.exp
        if (level == 1 and xp > 10) or (level == 2 and xp > 30) or (level == 3 and xp > 75) or (level == 4 and xp >= 120):
            level += 1
            print("\n" + bcolors.WARNING + bcolors.UNDERLINE + "Level up!" + bcolors.ENDC)
            self.increase_stats()
            if(level == 5):
                print("\n" + bcolors.WARNING + bcolors.UNDERLINE + "You've reached max level" + bcolors.ENDC)
        self.lvl = level
        self.exp = xp

    def choose_action(self):
        i = 1
        print("\n" + "    " + bcolors.BOLD + bcolors.UNDERLINE + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    ACTIONS:" + bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    MAGIC:" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "    ITEMS:" + bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name + ":", item["item"].description, " (x" + str(item["quantity"]) +")")
            i += 1

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "    TARGET:" + bcolors.ENDC)
        for enemy in enemies:
            if enemy.get_hp() != 0:
                print("        " + str(i) + ".", enemy.name)
                i += 1
        choice = int(input("    Choose target: ")) - 1
        return choice

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                    __________________________________________________ ")
        print(bcolors.BOLD + self.name + "  " +
              current_hp + " |" + bcolors.FAIL + hp_bar + bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10
        
        exp_bar = ""
        exp_ticks = (self.exp / self.maxexp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "
            
        while exp_ticks > 0:
            exp_bar += "█"
            exp_ticks -= 1
            
        while len(exp_bar) < 10:
            exp_bar += " "

        #HP
        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)

            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

        #MP
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_string

        else:
            current_mp = mp_string
        
        #XP    
        exp_string = str(self.exp) + "/" + str(self.maxexp)
        current_exp = ""
        
        if len(exp_string) < 7:
            decreased = 7 - len(exp_string)
            while decreased > 0:
                current_exp += " "
                decreased -= 1

            current_exp += exp_string

        else:
            current_exp = exp_string

        '''print("                     _________________________              __________ ")
        print(bcolors.BOLD + self.name + "    " +
              current_hp + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|    " +
              current_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|")'''
        print("                       _________________________              __________             __________")
        print(bcolors.BOLD + str(self.name) + " " +
              "(" + str(self.lvl) + ")" + "  " +
              current_hp + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + "|    " +
              current_mp + " |" + bcolors.OKBLUE + mp_bar + bcolors.ENDC + "|   " +
              current_exp + " |" + bcolors.WARNING + exp_bar + bcolors.ENDC + "|")      
              

    def choose_enemy_spell(self):
        magic_choice = random.randrange(0, len(self.magic))
        spell = self.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        pct = self.hp / self.maxhp * 100

        if self.mp < spell.cost or spell.type == "white" and pct > 50:
            self.choose_enemy_spell()
        else:
            return spell, magic_dmg
