class DigiMap(object):
    def __init__(self):
        self.map = {}

    def add_region(self, region_name, region_ranges):
        """
        add a region into digital world
        :param region_name: region name, str
        :param region_ranges: a tuple describe a rect (left, top, width, length)
        :return: None
        """
        region_width_start, region_length_start, width, length = region_ranges
        region_width_end = region_width_start + width
        region_length_end = region_length_start + length
        self.map.update({region_name: (region_width_start, region_width_end, region_length_start, region_length_end)})

    def remove_region(self, region_name):
        self.map.pop(region_name)

    def clear_regions(self):
        self.map.clear()

    def get_region_ranges(self, region_name):
        """
        return a tuple of region
        :param region_name:
        :return:
        """
        return self.map[region_name]
