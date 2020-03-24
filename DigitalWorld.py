import pygame
from pygame.locals import *
from pygame.color import THECOLORS
import math
from sys import exit
import DigiMap
import Digimon


def config_window():
    pygame.init()
    screen_x = 600 + 200
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
                    'number': 5
                  },
                 'tanemon': {
                     'pos': (450, 150),
                     'number': 5
                  },
                 'tsunomon': {
                     'pos': (150, 450),
                     'number': 5
                 },
                 'yokomon': {
                     'pos': (450, 450),
                     'number': 5
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
    event_list = []
    event_size = 26
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        # pygame.time.delay(200)
        screen.fill(THECOLORS['white'])
        region_pos_list = digital_regions.get_rect_tuples()
        region_color_list = digital_regions.get_region_colors()
        '''
        for i in range(digital_regions.get_region_size()):
            if region_color_list[i] == 'marineangemon home':
                continue
            pygame.draw.rect(screen, THECOLORS[region_color_list[i]], list(region_pos_list[i]), 0)
        '''
        pygame.draw.rect(screen, (178, 200, 187), [0, 0, 600, 600], 0)
        pygame.draw.rect(screen, (30, 41, 61), [600, 0, 200, 600], 0)
        for digimon_group in digimon_groups:
            digimon_group.group_walk(digimon_groups, event_list)
            digimon_group.group_blit(screen)
            digimon_group.remove_dead(event_list)
        if len(event_list):
            if len(event_list) > event_size:
                event_list.pop(0)
            font = pygame.font.SysFont('microsoft Yahei', 20)
            for i in range(len(event_list)):
                event_str = event_list[i]
                event_color = (255, 200, 10)
                if event_str.endswith('dead'):
                    event_color = (255, 0, 0)
                surface = font.render(event_str, False, event_color)
                screen.blit(surface, (610, 70 + i * 20))
        font_event_title = pygame.font.SysFont('arial', 40)
        surface_title = font_event_title.render('Digital Event', False, (255, 255, 255))
        screen.blit(surface_title, (610, 10))
        pygame.display.flip()
        clock.tick(5)


if __name__ == '__main__':
    main()
