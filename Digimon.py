import pygame
import random


class DigiMon(pygame.sprite.Sprite):
    run_spd_factor = 1.5
    evolve_exp_required = [10, 30, 60]

    def __init__(self, digimon_name, image_name, location_xy, hp, atk, spd_limit, home):
        self.digimon_name = digimon_name
        pygame.sprite.Sprite.__init__(self)
        image_name = 'pic/' + image_name
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location_xy
        # x and y speed
        self.walk_spd = [0, 0]
        self.spd_limit = spd_limit
        self.run_spd = self.spd_limit * DigiMon.run_spd_factor
        self.hp = hp
        self.atk = atk
        self.exp = 0
        self.finish_evolves = [False, False, False]
        print('home is ', home)
        self.home_width_start, self.home_length_start, self.home_width_end, self.home_length_end = home

    def walk(self, horizon=True, vertical=True):
        self.rect = self.rect.move(self.walk_spd)
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
        if (self.rect.left + step < self.home_width_start) or \
                (self.rect.right + step > self.home_width_end):
            self.walk_spd[0] = - step
        else:
            self.walk_spd[0] = step

    def walk_vertical(self):
        step = random.randint(- self.spd_limit, self.spd_limit)
        if (self.rect.top + step < self.home_length_start) or \
                (self.rect.bottom + step > self.home_length_end):
            self.walk_spd[1] = - step
        else:
            self.walk_spd[1] = step

    def get_image(self):
        return self.image

    def get_border(self):
        return self.rect

    def increase_exp(self):
        self.exp += 1

    def evolve(self):
        for evolve_level in range(len(self.finish_evolves)):
            if not self.finish_evolves[evolve_level]:
                if self.exp >= DigiMon.evolve_exp_required[evolve_level]:
                    self.finish_evolves[evolve_level] = True
                    print(self.exp)
                    upper_name = DigimonFactory.evolve_map[self.digimon_name]
                    upper_image_name = upper_name + '.png'
                    x_reserved = self.rect.left
                    y_reserved = self.rect.top
                    self.digimon_name = upper_name
                    upper_image_name = 'pic/' + upper_image_name
                    self.image = pygame.image.load(upper_image_name)
                    self.rect = self.image.get_rect()
                    self.rect.left, self.rect.top = (x_reserved, y_reserved)
                else:
                    break

    def restore(self):
        restore_hp = 200
        if self.hp + restore_hp > DigimonFactory.limits[self.digimon_name][0]:
            self.hp = DigimonFactory.limits[self.digimon_name][0]
        else:
            self.hp += restore_hp


class DigimonFactory(object):
    evolve_map = {
        'koromon': 'agumon',
        'tanemon': 'palmon',
        'tsunomon': 'gabumon',
        'yokomon': 'biyoumon',
        'agumon':'geogreymon',
        'palmon': 'togomon',
        'biyoumon': 'birdramon',
        'gabumon': 'garurumon',
        'togomon': 'lillymon',
        'garurumon': 'weregarurumon',
        'birdramon': 'garudamon',
        'geogreymon': 'rizegreymon',
        'lillymon': 'rosemon',
        'weregarurumon': 'metalgaruru',
        'garudamon': 'hououmon',
        'rizegreymon': 'wargreymon'
    }

    limits = {
        'koromon': [200, 4],
        'tanemon': [300, 2],
        'tsunomon': [240, 3],
        'yokomon': [280, 2],
        'agumon': [400, 80],
        'palmon': [600, 40],
        'biyoumon': [540, 50],
        'gabumon': [480, 60],
        'togomon': [900, 60],
        'garurumon': [720, 90],
        'birdramon': [840, 75],
        'geogreymon': [600, 120],
        'lillymon': [1200, 80],
        'weregarurumon': [960, 120],
        'garudamon': [1080, 100],
        'rizegreymon': [800, 160],
        'marineangemon': [1000, 1]
    }

    def __init__(self, digimap):
        self.database = {}
        self.kinds = ['koromon', 'tanemon', 'tsunomon', 'yokomon', 'marineangemon']
        self.hp = [200, 300, 240, 280, 1000]
        self.atk = [1, 1, 1, 1, 1]
        self.spd_limit = [10, 10, 10, 10, 1]
        self.image_name = [kind + '.png' for kind in self.kinds]
        self.home_name = [kind + ' home' for kind in self.kinds]
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
            location_x = random.randint(location_center[0] - 100, location_center[0] + 100)
            location_y = random.randint(location_center[1] - 100, location_center[1] + 100)
            location_xy = (location_x,  location_y)
            digimon = DigiMon(digimon_kind, image_name, location_xy, hp, atk, spd_limit, home_ranges)
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

    def add_group_element_tmp(self, digimon):
        self.group.add(digimon)

    def remove_element_tmp(self, digimon):
        self.group.remove(digimon)

    def group_walk(self, groups):
        for group in groups:
            if group.group_name == self.group_name:
                for digimon in self.digimons:
                    is_collide = self.collide_inner_group(digimon)
                    if is_collide:
                        digimon.restore()
                    digimon.walk()
            else:
                for digimon in self.digimons:
                    self.collide_inter_groups(digimon, group)
                    digimon.walk()


    def group_blit(self, screen):
        for digimon in self.digimons:
            x = digimon.get_border().left
            y = digimon.get_border().top

            hp_percent = digimon.hp / DigimonFactory.limits[digimon.digimon_name][0]
            print('hp_percent', hp_percent)
            pygame.draw.rect(screen, (255, 0, 0), (x, y - 6, 32, 5))
            pygame.draw.rect(screen, (100, 128, 0), (x, y - 6, 32 * hp_percent, 5))
            screen.blit(digimon.get_image(), digimon.get_border())


    def collide_inter_groups(self, digimon, group):
        group.add_group_element_tmp(digimon)
        is_collide = False
        if pygame.sprite.spritecollide(digimon, group.get_group(), False):
            print(self.group_name, ' collide with ', group.group_name)
            is_collide = True
            digimon.increase_exp()
            attack_value = DigimonFactory.limits[group.group_name][1]
            digimon.hp -= attack_value
            if digimon.hp <= 0:
                digimon.hp = 0
            choice = random.randint(0, 1)
            if not choice:
                digimon.walk_spd[0] = - digimon.walk_spd[0]
            else:
                digimon.walk_spd[1] = - digimon.walk_spd[1]
        group.remove_element_tmp(digimon)
        return is_collide


    def collide_inner_group(self, digimon):
        self.group.remove(digimon)
        is_collide = False
        if pygame.sprite.spritecollide(digimon, self.group, False):
            # print(self.group_name, ' collide !!!')
            is_collide = True
            # digimon.increase_exp()
            digimon.restore()
            choice = random.randint(0, 1)
            if not choice:
                digimon.walk_spd[0] = - digimon.walk_spd[0]
            else:
                digimon.walk_spd[1] = - digimon.walk_spd[1]
        self.group.add(digimon)
        return is_collide


