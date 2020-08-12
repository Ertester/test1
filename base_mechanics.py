# import numpy as np
import random as rd

TEST_IMAGE_PATH = 'C:/Users/pastukhov.si/team/test1/images/levels/test_image.png'
AFFIRMATIVE_ANSWERS = ['yes', 'y', 'yep', 'ok', 'yeah', 'sure']
MOVE_TAGS = ['left', 'right', 'down', 'up']
MAP_SIZE = [1000, 1000]
MONSTERS_POOL = {
    'orc': [],
    'goblin': [],
    'demon': []
}


class Hero:

    def __init__(self, hit_points, attack, speed):
        self.attack = attack
        self.hit_points = hit_points
        self.speed = speed
        self.x_pos = 0
        self.y_pos = 0

    def set_location(self, position):
        x_pos, y_pos = position[0], position[1]
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move_hero_left(self):
        self.x_pos -= 1
        
    def move_hero_right(self):
        self.x_pos += 1
    
    def move_hero_down(self):
        self.y_pos -= 1
        
    def move_hero_up(self):
        self.y_pos += 1
        

your_hero = Hero(100, 10, 20)


class Level:

    def __init__(self, x_size, y_size, image):
        self.x_size = x_size
        self.y_size = y_size
        self.level_image = image


class Monster:

    def __init__(self, hit_points, attack, location, name):
        self.x_pos, self.y_pos = location[0], location[1]
        self.hit_points = hit_points
        self.attack = attack
        self.name = name


def spawn_monster():
    return 0


def moving_on_map():
    flag = True
    while flag:
        print('Type direction')
        direction = input()
        if direction == 'left':
            your_hero.move_hero_left()
        elif direction == 'right':
            your_hero.move_hero_right()
        elif direction == 'down':
            your_hero.move_hero_down()
        elif direction == 'up':
            your_hero.move_hero_up()
        else:
            print('try maybe type some from {}'.format(MOVE_TAGS))
            continue

        print('your new position is ({}, {})'.format(your_hero.x_pos, your_hero.y_pos))
        print('move further?')
        answer = input()

        if answer.lower() not in AFFIRMATIVE_ANSWERS:
            flag = False
            print('now you standing at position ({}, {})'.format(your_hero.x_pos, your_hero.y_pos))
        else:
            print('ok, then')


goblin_1 = Monster(20, 3, [10, 5], 'gobby-gob')
goblin_2 = Monster(20, 3, [20, 25], 'goblin THE THIRD')
goblin_3 = Monster(20, 3, [33, 14], 'billy')
goblins = [goblin_1, goblin_2, goblin_3]

orc_1 = Monster(40, 7, [36, 5], 'orcy-orc')
orc_2 = Monster(40, 7, [45, 44], 'jimmy orco')
orc_3 = Monster(40, 7, [80, 99], 'justin')
orcs = [orc_1, orc_2, orc_3]

demon_1 = Monster(60, 15, [67, 20], 'demmo-demon')
demon_2 = Monster(60, 15, [15, 55], 'velzevul')
demon_3 = Monster(60, 15, [34, 90], 'gektor')
demons = [demon_1, demon_2, demon_3]

for goblin in goblins:
    MONSTERS_POOL['goblin'].append(goblin)
for orc in orcs:
    MONSTERS_POOL['orc'].append(orc)
for demon in demons:
    MONSTERS_POOL['demon'].append(demon)

print(MONSTERS_POOL)

path = TEST_IMAGE_PATH
lvl_image = ''

first_level = Level(1000, 1000, lvl_image)

