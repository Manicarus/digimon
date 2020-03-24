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
        self.home_width_start, self.home_width_end, self.home_length_start, self.home_length_end = home

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


class KoroMon(DigiMon):
    hp = 100
    atk = 30
    spd_limit = 20
    image_name = 'koromon.png'
    home_name = 'koromon home'

    def __init__(self, location_xy, digimap):
        home = digimap.get_region_ranges(KoroMon.home_name)
        super(KoroMon, self).__init__(KoroMon.image_name, location_xy, KoroMon.hp, KoroMon.atk, KoroMon.spd_limit, home)


class TaneMon(DigiMon):
    hp = 200
    atk = 20
    spd_limit = 5
    image_name = 'tanemon.png'
    home_name = 'tanemon home'

    def __init__(self, location_xy, digimap):
        home = digimap.get_region_ranges(KoroMon.home_name)
        super(TaneMon, self).__init__(TaneMon.image_name, location_xy, TaneMon.hp, TaneMon.atk, TaneMon.spd_limit, home)
