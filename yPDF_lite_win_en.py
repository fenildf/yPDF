#! python3
# -*- coding: UTF-8 –*-


import os, pyperclip, time, datetime, re

if not os.path.isdir('yPDF_cache'):
    os.mkdir('yPDF_cache')
randomFilename = 'yPDF_cache\\' + str(time.time()) + '.txt'
fo = open(randomFilename, 'w', encoding='UTF-8')
fo.write(str(pyperclip.paste()))
fo.close()

fo = open(randomFilename, 'r', encoding='UTF-8')
text = fo.read()
fo.close()

# Split lines.
lineList = text.split('\n') # create a list, in which each string is without line feeds already! 

# Join lines with spaces.
text = ' '.join(lineList)

# Change two or more continous spaces into one.
Re_twoOrMoreSpaces = re.compile(r'''(
([\s^\t\n]){2,} # two or more spaces
)''', re.VERBOSE)

text = Re_twoOrMoreSpaces.sub(' ', text)





# Change colon.
Re_colon = re.compile(r'''(
(∶)
)''', re.VERBOSE)

text = Re_colon.sub(':', text)



# Change comma.
Re_comma = re.compile(r'''(
(，)
)''', re.VERBOSE)

text = Re_comma.sub(',', text)


# Change period.
Re_period = re.compile(r'''(
(．)
)''', re.VERBOSE)

text = Re_period.sub('.', text)


# Change left_bracket_space.
Re_left_bracket_space = re.compile(r'''(
(\([\s^\t\n])
)''', re.VERBOSE)

text = Re_left_bracket_space.sub('(', text)



# Copy new text to clipboard.
pyperclip.copy(text)


# Print Related Information for this run.
timeThisMoment = datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S')
print('Saved to clipboard already! Text lenth: ' + str(len(text)) + '. ' + 'Current time: ' + timeThisMoment + '. ')