# PRINTIGRAM 
# 30 June, 2019
# Tested for Python 3.7.2 on Windows 10 Pro
#
# Need to install: Chrome driver for Selenium from
# https://sites.google.com/a/chromium.org/chromedriver/. 
# 'chromedriver.exe' needs to be in the Python working directory.

# The programme only works on Windows; need to change font/webdriver to work on other OS.

# Imports. Pil for images, os for paths and file management, selenium for web browser usage.
from PIL import Image, ImageDraw, ImageFont
import os
from selenium import webdriver

# Change directory to where you have stored chromedriver.exe
os.chdir("C:/Users/Merlijn Kersten/Documents/Code/Printigram")

# Make Chrome headless (invisible)
options = webdriver.ChromeOptions()
options.add_argument('headless')

# The Printigram function
def printigram(inputtext):                                                      
    lines = []                                                                  # Create empty list to store individual lines
    while inputtext != '':                                                      # Continue creating lines until the string is empty (i.e. the whole string has been added to lines)
        if len(inputtext) <= maxlength:                                         # If string is not longer than the maximum line length, add it to the lines list.
            lines.append(inputtext)
            break
        else:                                                                   # If it is, add the longest possible string of words to the lines list (i.e. until the last space before the break)
            linebreak = inputtext.rfind(' ', 0, maxlength)
            lines.append(inputtext[:linebreak])
            inputtext = inputtext[linebreak+1:]                                 # Delete the string of words you added to the lines list from the original string.
    img = Image.new('RGB', (width,len(lines)*50-10),  color = 'white')          # Create an white image with the width of the printer and the length of the lines
    fnt = ImageFont.truetype('C:/Windows/Fonts/Consola.ttf', size=40)           # Use the Consolas font. Only works on Windows.
    for i in range(len(lines)):
        ImageDraw.Draw(img).text((0,i*50), lines[i], font=fnt, fill=(0,0,0))    # Write lines in black text.
    img.save('text.png')
    #driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)   # Open Chrome
    #driver.get(url)                                                                         # Open correct Printi url
    #driver.find_element_by_name('filepicker').send_keys('text.png')                         # Upload image
    #driver.quit()                                                                           # Quit driver
    #os.remove('text.png')                                                                   # Remove image

# Script to determine whether one of the words is too long to print. 
def findlengths(inputtext):
    words = inputtext.split(' ')
    maxinputlength = 0
    for i in range(len(words)):
        if len(words[i]) > maxinputlength:
            maxinputlength = len(words[i])
    return maxinputlength

# User-interactions.
print('\n PRINTIGRAM')
print(' Type "QUIT" to exit \n')

# Ask whether to send messages to printi.me or printi.me/mango (different address and different widths)
printi = input(' Which printi? Type F (Fons) or M (/mango): ')
while printi not in ['F', 'M', 'f', 'm']:   # Make sure that a Printi is chosen
    printi = input('\n Whoops! Try again. Type F (Fons) or M (/mango): ')
if printi == 'F' or printi == 'f':
    url = 'https://printi.me'
    width = 576                             # Width in pixels
    maxlength = 25                          # Maximum number of characters that fit on one line
else:
    url = 'https://printi.me/mango'
    width = 384                             # Width in pixels
    maxlength = 16                          # Maximum number of characters that fit on one line
# If new Printi comes online: simply add its details and key above.

# Ask for message input
message = input('\n Message: ')
while findlengths(message) > maxlength:     # Checks whether input words are short enough to print
    print('One of your words is too long. They cannot be longer than ' + str(maxlength) + ' characters.\n')
    message = input(' Message: ')
while message != 'QUIT':                    # Regular text: send it to chosen printi
    printigram(message)
    message = input('\n Message: ')
if message == 'QUIT':                       # 'QUIT': Quit programme
    print()
    exit()