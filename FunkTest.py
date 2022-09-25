import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Velkommen til Hurtigtest")
    stdscr.addstr("\nTrykk på en tast for å starte")
    stdscr.refresh()
    stdscr.getkey()

def dispay_tekst(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    for i, char in  enumerate(current):
        stdscr.addstr(0,i,char,curses.color_pair(1))

def wpm_test(stdscr):
    target_text = "Hallo dette er teksten du skal bruke i hurtig testen"
    current_text = []
    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()
    while True:
        stdscr.clear()
        dispay_tekst(stdscr, target_text, current_text)
        stdscr.refresh()
        key = stdscr.getkey()

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
            else:
                current_text.append(key)
        stdscr.clear()
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))
        stdscr.refresh()

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
