import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import math
from sys import exit
import DigiMap
import Digimon


def config_window():
    pygame.init()
    screen_x = 600
    screen_y = 600
    screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)
    pygame.display.set_caption('Digital World')
    return screen


def init_map():
    regions = DigiMap.DigiMap()
    return regions


def init_digimons(digtal_regions):
    digimon_factory = Digimon.DigimonFactory(digtal_regions)
    birth_pos = {'koromon': {
                    'pos': (150, 150),
                    'number': 1
                  },
                 'tanemon': {
                     'pos': (450, 150),
                     'number': 1
                  },
                 'tsunomon': {
                     'pos': (150, 450),
                     'number': 1
                 },
                 'yokomon': {
                     'pos': (450, 450),
                     'number': 1
                 },
                'marineangemon': {
                    'pos': (300, 300),
                    'number': 1
                }
    }
    digimon_groups = []
    for kind_name, properties in birth_pos.items():
        digimon_groups.append(digimon_factory.birth(kind_name, properties['pos'], properties['number']))

    return digimon_groups


def main():
    screen = config_window()
    digital_regions = init_map()
    digimon_groups = init_digimons(digital_regions)
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # pygame.time.delay(200)
        screen.fill(THECOLORS['white'])
        region_pos_list = digital_regions.get_rect_tuples()
        region_color_list = digital_regions.get_region_colors()
        for i in range(digital_regions.get_region_size()):
            if region_color_list[i] == 'marineangemon home':
                continue
            pygame.draw.rect(screen, THECOLORS[region_color_list[i]], list(region_pos_list[i]), 0)
        for digimon_group in digimon_groups:
            digimon_group.group_walk(digimon_groups)
            digimon_group.group_blit(screen)
        pygame.display.flip()
        clock.tick(5)


if __name__ == '__main__':
    main()
