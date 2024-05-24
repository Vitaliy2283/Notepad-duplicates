# Author: Vitaliy Tsupriyan
# Alias: VAAL33
# Date: 05/19/2024
# Description: This code is for Notepad++ Python plugin. Code looks for a IDs in the queries/text that have 11 comprising alphanumeric characters in specific IDs patterns.
# If IDs has a duplicates all duplicates will be colored in the predefined colors. Code has 10 different color patterns. 


import re
from Npp import editor
from collections import defaultdict
from random import randint

# The function extracts all substrings of length 11 from the given text and counts the occurrences of each unique substring
def get_sub_string(text):
    length = 11
    counts = defaultdict(int)
    pattern = re.compile(r'\b[a-zA-Z0-9]{11}\b')
    for match in pattern.finditer(text):
        sub_string = match.group(0)
        counts[sub_string] += 1
    return counts

# Predefined list of colors (RGB tuples)
colors = [
    (255, 0, 0),     # Red
    (0, 255, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 255, 0),   # Yellow
    (255, 165, 0),   # Orange
    (128, 0, 128),   # Purple
    (0, 255, 255),   # Cyan
    (255, 192, 203), # Pink
    (128, 128, 0),   # Olive
    (0, 128, 128)    # Teal
]

# Get the text from the editor
try:
    text = editor.getText()
except NameError:
    text = ""

if text:
    sub_strings = get_sub_string(text)

    # Clear existing indicators
    for i in range(len(colors)):
        editor.setIndicatorCurrent(i)
        editor.indicatorClearRange(0, editor.getTextLength())

    duplicate_sets = {k: v for k, v in sub_strings.items() if v > 1}

    # Assign colors to duplicate sets
    color_map = {}
    for idx, key in enumerate(duplicate_sets):
        color_map[key] = colors[idx % len(colors)]

    # Set up the indicator styles
    for i, color in enumerate(colors):
        editor.indicSetStyle(i, INDICATORSTYLE.ROUNDBOX)  # Using rounded box style
        editor.indicSetUnder(i, True)  # Display indicator under text
        editor.indicSetFore(i, color)  # Set the color

    for match in re.finditer(r'\b[a-zA-Z0-9]{11}\b', text):
        sub_string = match.group(0)
        if sub_string in duplicate_sets:
            color = color_map[sub_string]
            indicator_number = colors.index(color)
            editor.setIndicatorCurrent(indicator_number)
            editor.indicatorFillRange(match.start(), 11)  # Highlight the substring


#    for sub_string, count in duplicate_sets.items(): 
#         print("Substring: {}, Count: {}, Color: {}".format(sub_string, count, color_map[sub_string]) )

       