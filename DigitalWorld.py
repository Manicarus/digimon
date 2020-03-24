import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import math
from sys import exit
import DigiMap
import Digimon


def config_window():
    pygame.init()
    screen_x = 200
    screen_y = 200
    screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)
    pygame.display.set_caption('Digital World')
    return screen


def init_map():
    regions = DigiMap.DigiMap()
    return regions


def init_digimons(digtal_regions):
    digimon_factory = Digimon.DigimonFactory(digtal_regions)
    birth_pos = {'koromon': (50, 50),
                 'tanemon': (150, 50),
                 'tsunomon': (50, 150),
                 'yokomon': (150, 150)
                 }
    digimons = []
    for kind_name, pos in birth_pos.items():
        digimons.append(digimon_factory.birth(kind_name, pos))
    return digimons


def main():
    screen = config_window()
    digital_regions = init_map()
    digimons = init_digimons(digital_regions)
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
        for digimon in digimons:
            digimon.walk()
            screen.blit(digimon.get_image(), digimon.get_border())
        pygame.display.flip()


if __name__ == '__main__':
    main()
