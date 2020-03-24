import pygame
import DigiMap
import random


class DigiMon(pygame.sprite.Sprite):
    run_spd_factor = 1.5

    def __init__(self, image_name, location_xy, hp, atk, spd_limit, home):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_name)
        self.image_border = self.image.get_rect()
        self.image_border.left, self.image_border.top = location_xy
        # x and y speed
        self.walk_spd = [0, 0]
        self.spd_limit = spd_limit
        self.run_spd = self.spd_limit * DigiMon.run_spd_factor
        self.hp = hp
        self.atk = atk
        print('home is ', home)
        self.home_width_start, self.home_length_start, self.home_width_end, self.home_length_end = home

    def walk(self, horizon=True, vertical=True):
        self.image_border = self.image_border.move(self.walk_spd)
        if horizon and vertical:
            choice = random.randint(0, 1)
            if choice:
                self.walk_horizon()
            else:
                self.walk_vertical()

        if horizon:
            self.walk_horizon()
        if vertical:
            self.walk_vertical()

    def walk_horizon(self):
        step = random.randint(- self.spd_limit, self.spd_limit)
        if (self.image_border.left + step < self.home_width_start) or \
                (self.image_border.right + step > self.home_width_end):
            self.walk_spd[0] = - step
        else:
            self.walk_spd[0] = step

    def walk_vertical(self):
        step = random.randint(- self.spd_limit, self.spd_limit)
        if (self.image_border.top + step < self.home_length_start) or \
                (self.image_border.bottom + step > self.home_length_end):
            self.walk_spd[1] = - step
        else:
            self.walk_spd[1] = step

    def get_image(self):
        return self.image

    def get_border(self):
        return self.image_border


class DigimonFactory(object):
    def __init__(self, digimap):
        self.database = {}
        self.kinds = ['koromon', 'tanemon', 'tsunomon', 'yokomon']
        self.hp = [200, 250, 150, 300]
        self.atk = [30, 20, 40, 10]
        self.spd_limit = [20, 15, 10, 25]
        self.image_name = [ kind + '.png' for kind in self.kinds]
        self.home_name = [ kind + ' home' for kind in self.kinds]
        for i in range(len(self.kinds)):
            properties = {'hp': self.hp[i],
                          'atk': self.atk[i],
                          'spd_limit': self.spd_limit[i],
                          'image_name': self.image_name[i],
                          'home_name': self.home_name[i]
                          }
            self.database.update({self.kinds[i]: properties})
        self.digimap = digimap

    def birth(self, digimon_kind, location_center, number):
        digimon_property = self.database[digimon_kind]
        image_name = digimon_property['image_name']
        hp = digimon_property['hp']
        atk = digimon_property['atk']
        spd_limit = digimon_property['spd_limit']
        home_ranges = self.digimap.get_region_ranges(digimon_property['home_name'])
        digimon_group = DigimonGroup(digimon_kind)
        for i in range(number):
            location_x = random.randint(location_center[0] - 50, location_center[0] + 50)
            location_y = random.randint(location_center[1] - 50, location_center[1] + 50)
            location_xy = (location_x,  location_y)
            digimon = DigiMon(image_name, location_xy, hp, atk, spd_limit, home_ranges)
            digimon_group.add_digimon(digimon)
        return digimon_group


class DigimonGroup(object):
    def __init__(self, kind_name):
        self.group_size = 0
        self.group_name = kind_name
        self.group = pygame.sprite.Group()
        self.digimons = []

    def add_digimon(self, digimon):
        self.digimons.append(digimon)
        self.group.add(digimon)
        self.group_size += 1

    def get_group(self):
        return self.group

    def get_group_name(self):
        return self.group_name

    def group_walk(self):
        for digimon in self.digimons:
            digimon.walk()

    def group_blit(self, screen):
        for digimon in self.digimons:
            screen.blit(digimon.get_image(), digimon.get_border())
