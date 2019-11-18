import sys, webbrowser, pyperclip
print("Starte google maps")
#Dette er kun et test program
sys.argv
sted = ' '.join(sys.argv[1: ])
sted = pyperclip.paste()
webbrowser.open('https://www.google.no/maps/place/'+sted)