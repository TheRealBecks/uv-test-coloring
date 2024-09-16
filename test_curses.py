import curses

curses.setupterm()
print(curses.tigetnum("colors"))
