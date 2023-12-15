from math import sin, cos, radians
import string
from time import sleep

size = 2**10
field = [[' ' for _ in range(size)] for _ in range(size)]
field_trace = [[' ' for _ in range(size)] for _ in range(size)]
print_field = lambda f: print('\n', *[''.join(['|']+i+['|']) for i in f], '\n', sep='\n')

pos = (int(size/2), int(size/2)) #y x
dir_ = -90

field[pos[0]][pos[1]] = ' '
field_trace[pos[0]][pos[1]] = '0'
# print_field(field)
step_amount = 0
def step(field):
    global pos, dir_, field_trace, step_amount
    step_amount+=1
    if field[pos[0]][pos[1]] == ' ':
        dir_+=90
        dir_=dir_%360
        field[pos[0]][pos[1]] = '█'

    elif field[pos[0]][pos[1]] == '█':
        dir_-=90
        dir_=dir_%360
        field[pos[0]][pos[1]] = ' '
    
    
    pos = (pos[0]+int(1*sin(radians(dir_))), pos[1]+int(1*cos(radians(dir_))))
    field_trace[pos[0]][pos[1]] = string.ascii_letters[ step_amount%30]
    
    


while True:
    try:
        step(field)
    except Exception as e:
        print(e)
        # print_field(field)
        # print_field(field_trace)
        break

from PIL import Image
import numpy as np
count = sum([sum([0 if j==' ' else 1 for j in field]) for i in field])
print(count)

pixels = [
   [(0,0,0) if j=='█' else (255,255,255) for j in i] for i in field
]

# Convert the pixels into an array using numpy
array = np.array(pixels, dtype=np.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('new.png')

# while True:
#     try:
#         step(field)
#     except:


#         print_field(field)
#         print_field(field_trace)
#         break