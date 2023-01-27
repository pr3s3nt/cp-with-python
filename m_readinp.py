import sys
def init(path):
    s = path.split('/')
    input_file = "./input/" + s[-1].split('.')[0] + ".inp"
    sys.stdin = open(input_file, 'r')
