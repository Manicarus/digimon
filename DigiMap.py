class DigiMap(object):
    def __init__(self):
        self.map = {
            'koromon home': {
                'pos': (0, 0, 300, 300),
                'color': 'red',
                'constraint': None
            },
            'tanemon home': {
                'pos': (300, 0, 300, 300),
                'color': 'blue',
                'constraint': None
        },
            'tsunomon home': {
                'pos': (0, 300, 300, 300),
                'color': 'green',
                'constraint': None
        },
            'yokomon home': {
                'pos': (300, 300, 300, 300),
                'color': 'yellow',
                'constraint': None
        }
        }
        self.region_size = len(self.map)
        self.rect_list = []
        self.color_list = []
        for region_name, properties in self.map.items():
            self.rect_list.append(properties['pos'])
            self.color_list.append(properties['color'])
            pos = list(properties['pos'])
            constraint = (pos[0], pos[1], pos[0] + pos[2], pos[1] + pos[3])
            self.map[region_name]['constraint'] = constraint

    def get_region_colors(self):
        return self.color_list

    def get_rect_tuples(self):
        return self.rect_list

    def get_region_size(self):
        return self.region_size

    def clear_regions(self):
        self.map.clear()

    def get_region_ranges(self, region_name):
        """
        return a tuple of region
        :param region_name:
        :return:
        """
        return self.map[region_name]['constraint']
