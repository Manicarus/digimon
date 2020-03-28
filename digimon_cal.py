import matplotlib.pyplot as plt


class Digi(object):
    def __init__(self, name, stage, type, attribute, memory, es, hp, sp, atk, defend, lnt, spd):
        self.name = name
        self.stage = stage
        self.type = type
        self.hp = hp
        self.attribute = attribute
        self.memory = memory
        self.es = es
        self.hp = hp
        self.sp = sp
        self.atk = atk
        self.lnt = lnt
        self.defend = defend
        self.spd = spd
        self.parents = []
        self.sons = []

    def add_parent(self, parent_name):
        self.parents.append(parent_name)

    def add_son(self, son_name):
        self.parents.append(son_name)

    def show(self):
        print('digi name is ', self.name)


class DigiGroup(object):
    def __init__(self):
        self.digis = dict()
        self.size = 0

    def add_digi(self, digi):
        self.digis[digi.name] = digi
        self.size += 1

    def remove_digi(self, digi_name):
        self.digis.pop(digi_name)
        self.size -= 1

    def get_digis(self):
        return self.digis

    def get_digi(self, digi_name):
        return self.digis[digi_name]

    def init_digis(self, file_name):
        with open(file_name, 'r') as f:
            for digi in f.readlines():
                digi = digi[:-1]
                digi_tuple = tuple(eval(digi))
                digi_instance = Digi(*digi_tuple)
                self.digis[digi_instance.name] = digi_instance
                self.size += 1


def draw_digis(digi_group):
    color_list = []
    hp_list = []  # x axis
    sp_list = []  # y axis
    stage_list = ['Baby', 'In-Training', 'Rookie', 'Champion', 'Ultimate',
                  'Mega', 'Ultra', 'Armor', 'None']
    color_pre = ['b', 'y', 'g', 'crimson', 'gray', 'maroon', 'pink', 'orange', 'wheat']
    for digi_name, digi in digi_group.get_digis().items():
        hp_list.append(digi.hp)
        sp_list.append(digi.sp)
        stage = digi.stage
        index = stage_list.index(stage)
        if index < 0:
            print('error: ', digi_name)
        else:
            color_list.append(color_pre[index])

    fig = plt.figure(num='fig', figsize=(8, 8), dpi=75, facecolor='#FFFFFF')
    ax = fig.add_subplot(111)
    ax.scatter(hp_list, sp_list, s=400, c=color_list, alpha=0.5, edgecolors='w', marker='o')
    ax.legend(bbox_to_anchor=(-0.04, 1.001), loc='lower left', fontsize=20, frameon=True, ncol=3, borderpad=1,
               labelspacing=1, handlelength=3, handletextpad=0.5, borderaxespad=1, columnspacing=1)
    plt.show()


def main():
    digi_group = DigiGroup()
    file_name = 'save_pic/1.txt'
    digi_group.init_digis(file_name)
    draw_digis(digi_group)


if __name__ == '__main__':
    main()
