import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import math
from sys import exit
import DigiMap
import Digimon


def config_window():
    pygame.init()
    screen_x = 400
    screen_y = 400
    screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)
    pygame.display.set_caption('Digital World')
    return screen


def init_map():
    regions = DigiMap.DigiMap()
    return regions


def init_digimons(digtal_regions):
    digimon_factory = Digimon.DigimonFactory(digtal_regions)
    birth_pos = {'koromon': {
                    'pos': (100, 100),
                    'number': 3
                  },
                 'tanemon': {
                     'pos': (300, 100),
                     'number': 2
                  },
                 'tsunomon': {
                     'pos': (100, 300),
                     'number': 2
                 },
                 'yokomon': {
                     'pos': (300, 300),
                     'number': 2
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
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        pygame.time.delay(200)
        screen.fill(THECOLORS['white'])
        region_pos_list = digital_regions.get_rect_tuples()
        region_color_list = digital_regions.get_region_colors()
        for i in range(digital_regions.get_region_size()):
            pygame.draw.rect(screen, THECOLORS[region_color_list[i]], list(region_pos_list[i]), 0)
        for digimon_group in digimon_groups:
            digimon_group.group_walk()
            digimon_group.group_blit(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
