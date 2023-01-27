import sys
s = __file__.split('/')
input_file = "../input/" + s[-1].split('.')[0] + ".inp"
sys.stdin = open(input_file, 'r')
#print(input_file)