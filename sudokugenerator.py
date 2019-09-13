#Sudoku generator for printi.me/mango
#13 September 2019, Python 3.7;2
#Adjust difficulty: line 26
#If Inconsolata Regular not installed or using non-Windows OS, change: line 48
#Change printi: line 60

from random import sample
from PIL import Image, ImageDraw, ImageFont
import printipigeon as pp
import os

#os.chdir('C:/Users/Merlijn Kersten/Documents/GitHub/printigram') #For testing

#Code by Alain T. at https://stackoverflow.com/questions/45471152/how-to-create-a-sudoku-puzzle-in-python
base  = 3
side  = base*base
nums  = sample(range(1,side+1),side)
board = [[nums[(base*(r%base)+r//base+c)%side] for c in range(side) ] for r in range(side)]
rows  = [ r for g in sample(range(base),base) for r in sample(range(g*base,(g+1)*base),base) ] 
cols  = [ c for g in sample(range(base),base) for c in sample(range(g*base,(g+1)*base),base) ]            
board = [[board[r][c] for c in cols] for r in rows]
squares = side*side

########################################################
#Adjust difficulty. 1: solved, 0: empty, 4//7: default #
empties = squares * 4//7                               #
########################################################

for p in sample(range(squares),empties):
    board[p//side][p%side] = 0
numSize = len(str(side))

#Make list of sudoku lines
lines = []
for i in range(9):
    templine = ''
    for item in board[i]:
        if item == 0:
            templine += '  '
        else:
            templine += str(item) + ' '
        if len(templine) in [3, 7]:
            templine += ' '
    lines.append(templine)

#Make image out of sudoku lines, draw major division lines, print using printi pigeon
img = Image.new('RGB', (590,700),  color = 'white')       
fnt = ImageFont.truetype('C:/Windows/Fonts/Inconsolata-Regular.ttf', size=70)       
for i in range(len(lines)):
    ImageDraw.Draw(img).text((0,i*80), lines[i], font=fnt, fill=(0,0,0))
d = ImageDraw.Draw(img)
d.line([(192,0), (192,700)], fill=(0,0,0), width=5) 
d.line([(402,0), (402,700)], fill=(0,0,0), width=5)   
d.line([(0,238), (590,238)], fill=(0,0,0), width=5)
d.line([(0,477), (590,477)], fill=(0,0,0), width=5)
img.save('sudoku.png')

####################################################
#Change 'mango' for other printi names if required #
pp.send_from_path('sudoku.png', 'mango')           #
####################################################

os.remove('sudoku.png')