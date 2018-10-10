#! python3
# -*- coding: UTF-8 –*-

import os, pyperclip, time, datetime, re, shutil

EN_SPACE = ' '


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

# Change two or more continous spaces into one.
Re_twoOrMoreSpaces = re.compile(r'''(
([\s^\t\n]){2,} # two or more spaces
)''', re.VERBOSE)

text = Re_twoOrMoreSpaces.sub('%s' % EN_SPACE, text)





# Change colon.
Re_colon = re.compile(r'''(
(∶)
)''', re.VERBOSE)

text = Re_colon.sub(':', text)



# Change comma.
Re_comma = re.compile(r'''(
(，)
)''', re.VERBOSE)

text = Re_comma.sub(', ', text)


# Change period.
Re_period = re.compile(r'''(
(．)
)''', re.VERBOSE)

text = Re_period.sub('. ', text)


# Change period_cn.
Re_period_cn = re.compile(r'''(
(。)
)''', re.VERBOSE)

text = Re_period_cn.sub('.', text)




# Change left_bracket_space.
Re_left_bracket_space = re.compile(r'''(
(\([\s^\t\n])
)''', re.VERBOSE)

text = Re_left_bracket_space.sub('(', text)


# Change left_bracket_cn.
Re_left_bracket_cn = re.compile(r'''(
(（)
)''', re.VERBOSE)

text = Re_left_bracket_cn.sub(' (', text)



# Change right_bracket_cn.
Re_right_bracket_cn = re.compile(r'''(
(）)
)''', re.VERBOSE)

text = Re_right_bracket_cn.sub(') ', text)


# Change right_bracket_space_period.
Re_right_bracket_space_period = re.compile(r'''(
(\) .)
)''', re.VERBOSE)

text = Re_right_bracket_space_period.sub(').', text)










# Copy new text to clipboard.
pyperclip.copy(text)


# Print Related Information for this run.
timeThisMoment = datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S')
print('Saved to clipboard already! Text lenth: ' + str(len(text)) + '. ' + 'Current time: ' + timeThisMoment + '. \na gaoyaoxin app')

# Delete cache directory and cache files in it.
shutil.rmtree('yPDF_cache')