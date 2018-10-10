#! python3
# -*- coding: UTF-8 –*-

import os, pyperclip, time, datetime, re, shutil

CN_SPACE = ''


if not os.path.isdir('yPDF_cache'):
    os.mkdir('yPDF_cache')
cacheFilename = 'yPDF_cache\\' + str(time.time()) + '.txt'
fo = open(cacheFilename, 'w', encoding='UTF-8')
fo.write(str(pyperclip.paste()))
fo.close()

fo = open(cacheFilename, 'r', encoding='UTF-8')
text = fo.read()
fo.close()

# Split lines.
lineList = text.split('\n') # create a list, in which each string is without line feeds already! 

# Join lines with spaces.
text = ' '.join(lineList)

# Change one or more continous spaces into one.
Re_twoOrMoreSpaces = re.compile(r'''(
([\s^\t\n]){1,} # one or more spaces
)''', re.VERBOSE)

text = Re_twoOrMoreSpaces.sub('%s' % CN_SPACE, text)

# Change comma.
Re_comma = re.compile(r'''(
(,)
)''', re.VERBOSE)

text = Re_comma.sub('，', text)


# Change semicolon.
Re_semicolon = re.compile(r'''(
(;)
)''', re.VERBOSE)

text = Re_semicolon.sub('；', text)


# Copy new text to clipboard.
pyperclip.copy(text)


# Print Related Information for this run.
timeThisMoment = datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S')
print('Saved to clipboard already! Text lenth: ' + str(len(text)) + '. ' + 'Current time: ' + timeThisMoment + '. \na gaoyaoxin app')

# Delete cache directory and cache files in it.
shutil.rmtree('yPDF_cache')