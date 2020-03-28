READ_BUFFER_SIZE = 1024


def read_whole_file(path):
    '''
    generator function: read a file by using a file path
    eg. for i in read_whole_file('xx.txt') or next(read_whole_file('xx'))
    :param path: type of path is str
    :return:
    '''
    with open(path, 'rb') as f:
        while True:
            content = f.read(READ_BUFFER_SIZE)
            if content:
                yield content
            else:
                return
