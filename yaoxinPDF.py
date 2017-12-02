#! python3

# yaoxinPDF.py - Replace line feeds with spaces of text on the clipboard.
# Make pdf easy to use.

# sudo pip3 install pynput pyperclip
# first

# python<version> yaoxinPDF.py



import pyperclip, datetime, pynput
from importlib import reload

def yaoxinPDF():


	text = pyperclip.paste()



	file = open('yaoxinPDF.txt', 'w')
	file.write(str(text))

	file.close()



	theFile = open('yaoxinPDF.txt', 'r')
	pyperclip.copy(theFile.read())
	fileForUse = pyperclip.paste()

	theFile.close()


	# Separate lines and delete line feeds.
	lines = fileForUse.split('\n') # each string in "lines" list are without line feeds already! 
	global Newtext
	Newtext = ' '.join(lines)
	
	pyperclip.copy(Newtext)
	


# The key combination to check
COMBINATION1 = {pynput.keyboard.Key.ctrl, pynput.keyboard.KeyCode.from_char('c')}
COMBINATION2 = {pynput.keyboard.Key.ctrl, pynput.keyboard.KeyCode.from_char('C')}

# The currently active modifiers
current = set()


def on_press(key):
	if key in COMBINATION1:
		current.add(key)
		if all(k in current for k in COMBINATION1):
			reload(pyperclip)
			yaoxinPDF()
			reload(pyperclip)
			yaoxinPDF()
			print('Saved to clipboard already! ' 'text lenth: ' + str(len(Newtext)) + '. ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))
	elif key in COMBINATION2:
		current.add(key)
		if all(k in current for k in COMBINATION2):
			reload(pyperclip)
			yaoxinPDF()
			reload(pyperclip)
			yaoxinPDF()
			print('Saved to clipboard already! ' 'text lenth: ' + str(len(Newtext)) + '. ' + datetime.datetime.now().strftime('%Y.%m.%d-%H:%M:%S'))
	if key == pynput.keyboard.Key.esc:
		listener.stop()


def on_release(key):
	try:
		current.remove(key)
	except KeyError:
		pass


with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()
