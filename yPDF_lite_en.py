import pyperclip, time

fo = open('%s.txt' % time.time(), 'w', encoding='UTF-8')
fo.write(str(pyperclip.paste()))
fo.close()

fo = open('yPDF.txt', 'r', encoding='UTF-8')
text = fo.read()
fo.close()

# Separate lines and delete line feeds.
text = text.split('\n') # each string in "lines" list are without line feeds already! 
text = ' '.join(text)
pyperclip.copy(text)
print('Saved to clipboard already! ' 'Text lenth: ' + str(len(text)) + '. ' + 'Current time: ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S')) + '. '