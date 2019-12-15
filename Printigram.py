# PRINTIGRAM 
# First version: 16 July 2019
# Second version: 15 December 2019
# Tested for Python 3.7.2 on Windows 10 Pro
# The programme only works on Windows; need to change font to work on other OS.

# Imports. Pil for images, os for paths and file management, printipigeon to sent pictures to printi.
from PIL import Image, ImageDraw, ImageFont
import os
import printipigeon as pp

# The following two functions set the maximum word length and the width in pixels of the printi in question, either Fons's (printi.me/) or any other.

def maxlength(printi_name):
    if printi_name == '': 
        return 41
    else:                   
        return 27
def width(printi_name):
    if printi_name == '': 
        return 576
    else:                   # All Printi Mini's
        return 384

# The Printigram function. Turns an input message into a text image which is sent to Printi.
def printigram(inputtext):                                                      
    lines = []                                                                  # Create empty list to store individual lines
    while inputtext != '':                                                      # Continue creating lines until the string is empty (i.e. the whole string has been added to lines)
        if len(inputtext) <= maxlength(printi_name):                            # If string is not longer than the maximum line length, add it to the lines list.
            lines.append(inputtext)
            break
        else:                                                                   # If it is, add the longest possible string of words to the lines list (i.e. until the last space before the break)
            linebreak = inputtext.rfind(' ', 0, maxlength(printi_name))
            lines.append(inputtext[:linebreak])
            inputtext = inputtext[linebreak+1:]                                 # Delete the string of words you added to the lines list from the original string.
    img = Image.new('RGB', (width(printi_name),len(lines)*28-3),  color = 'white')          # Create an white image with the width of the printer and the length of the lines
    fnt = ImageFont.truetype('C:/Windows/Fonts/Consola.ttf', size=25)           # Use the Consolas font. Only works on Windows.
    for i in range(len(lines)):
        ImageDraw.Draw(img).text((0,i*28), lines[i], font=fnt, fill=(0,0,0))    # Write lines in black text.
    img.save('text.png')
    pp.send_from_path('text.png', printi_name)                                  # Use Printi Pigeon to sent pictures to correct printer                                                                        # Quit driver
    os.remove('text.png')                                                       # Remove image

# User-interactions. Ask which printi to sent messages to.
print('\n PRINTIGRAM \n Type "QUIT" to exit \n Type "CHANGE" to switch to a different Printi ')

printi_name = input('\n Which Printi? \n printi.me/')

message = input('\n Message: ')
while message != 'QUIT' and message != 'Q':
    if message == 'CHANGE' or message == 'C':                   # To change recipient Printi.
        printi_name = input('\n Which Printi? \n printi.me/')
    else:
        printigram(message)
    message = input('\n Message: ')
if message == 'QUIT' or message == 'Q':             
    print()
    exit()