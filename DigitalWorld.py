import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import math
from sys import exit
import DigiMap
import Digimon


def config_window():
    pygame.init()
    screen_x = 800
    screen_y = 800
    screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)
    pygame.display.set_caption('Digital World')
    return screen


def init_map():
    regions = DigiMap.DigiMap()
    regions.add_region('koromon home', (0, 0, 100, 100))
    regions.add_region('tanemon home', (100, 0, 100, 100))
    return regions


def init_digimons(digtal_regions):
    init_pos_koro = (50, 50)
    init_pos_tane = (150, 30)
    koromon_one = Digimon.KoroMon(init_pos_koro, digtal_regions)
    tanemon_one = Digimon.TaneMon(init_pos_tane, digtal_regions)
    return koromon_one, tanemon_one


def main():
    screen = config_window()
    digital_regions = init_map()
    koromon_one, tanemon_one = init_digimons(digital_regions)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        pygame.time.delay(200)
        screen.fill(THECOLORS['white'])
        # pygame.draw.rect(screen, THECOLORS['red'], digital_regions.get_region_ranges('koromon home'), 0)
        pygame.draw.rect(screen, THECOLORS['red'], [0, 0, 100, 100], 0)
        pygame.draw.rect(screen, THECOLORS['green'], [100, 0, 100, 100], 0)
        koromon_one.walk()
        tanemon_one.walk()
        screen.blit(koromon_one.get_image(), koromon_one.get_border())
        screen.blit(tanemon_one.get_image(), tanemon_one.get_border())
        pygame.display.flip()


if __name__ == '__main__':
    main()
