import os
if 'MainDrive' not in os.listdir():
    os.system('pip install -r req.txt')
    os.system('pip3 install -r req.txt')
    os.system('python -m pip install -r req.txt')
    os.system('python3 -m pip install -r req.txt')
from curses import *
from colorama import Fore
from colorama import init
import time
import random
import sys

w, h = os.get_terminal_size()
targets = [
    'O Create System Users.',
    'O Entropy Daemon based on the HAVEGE algorithm.',
    '# Starting Rule-based Manager for Device Events and Files.',
    'O Reached target Encrypting Volumes.',
    'O Listening on Process Core Dump Socket.',
    'O Reached target Remote File Systems.',
    'O Started Create list of required static device nodes.',
    'O Waiting for udev To Complete Device Initialization.',
    'O Monitoring of LVM2 mirrors, etc. using dmeventd or progress polling.',
    'O Started Apply Kernel Variables.',
    'O Mounted Debug File System.',
    'O Mounted Configuration File System.',
    'O Mount POSIX Message Queue File System.',
    'O Started Journal service.',
    'O Started Remount Root and Kernel File Systems.',
    '# Starting udev Coldplug all Devices...',
    '# Starting Flush Journal to Persistent Storage...',
    '# Starting Create Static Device Nodes in /dev...',
    '# Starting Load/Save Random Seed...',
    'O Started Load/Save Random Seed.',
    'O Started udev Coldplug all Devices.',
    'O Started Create Static Device Nodes in /dev.',
    '# Starting udev Kernel Device Manager...',
    'O Reached target Local File Systems (Pre).',
    'O Started Flush Journal to Persistent Storage.',
    'O Started udev Kernel Device Manager.',
    'O Found device Samsung_SSD_850_PRO_512GB SYSTEM.',
    '# Mounting /boot...',
]

def fancyboot():
    for target in targets:
        _ = target.split(' ')[0]
        if _ == 'O':
            print(f'[  {Fore.GREEN}' + 'OK' + f'{Fore.WHITE}  ] ' + target[2:])
        elif _ == '#':
            print(' '*9 + str(target[2:]))
        elif _ == 'F':
            print(f'[{Fore.RED}' + 'FAILED' + f'{Fore.WHITE}]' + target[2:])
        time.sleep(random.uniform(0.05, 0.07))
    time.sleep(0.07)
    
clear_command = 'clear'
if os.name == 'nt':  # If Machine is running on Windows, use cls
    clear_command = 'cls'

if '--noboot' not in sys.argv:

    data = open('sys_settings.cfg', 'r').readlines()
    for i in range(len(data)):
        if data[i].split('=')[0] == 'phaseboot':
            if data[i].split('=')[1] == 'True':
                os.system(clear_command)

                fancyboot()
                def cprint(r, g, b, text):
                    print("\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text))

                a = 1
                v = 0

                for i in range(255):
                    os.system('cls')
                    if v%255 == 0:
                        if a == 1:
                            a = 0
                        else:
                            a = 1
                    if a == 1:
                        v -= 3
                    else:
                        v += 3
                    for i in range(h//2-3):
                        print()
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██╗███╗  ██╗ █████╗ ██████╗ ██╗  ██╗       █████╗  ██████╗')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██║████╗ ██║██╔══██╗██╔══██╗██║ ██╔╝      ██╔══██╗██╔════╝')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██║██╔██╗██║███████║██████╔╝█████═╝ █████╗██║  ██║╚█████╗ ')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██║██║╚████║██╔══██║██╔══██╗██╔═██╗ ╚════╝██║  ██║ ╚═══██╗')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '██║██║ ╚███║██║  ██║██║  ██║██║ ╚██╗      ╚█████╔╝██████╔╝')
                    cprint(0, 0, v, ' '*((w//2)-(58//2)) + '╚═╝╚═╝  ╚══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚════╝ ╚═════╝ ')
                    for i in range(h//2-4):
                        print()
            else:
                init()

                os.system(clear_command)

                fancyboot()

                try:
                    win = initscr()
                    start_color()
                    curs_set(0)

                    y, x = win.getmaxyx()
                    y = y // 2
                    x = x // 2
                    scl = 20
                    offset = 3
                    yoffset = y - 15


                    init_pair(1, COLOR_CYAN, COLOR_BLACK)

                    win.attron(color_pair(1))
                    win.addstr(y + yoffset - 5 - offset, x - 27, "██████╗  █████╗ ██████╗ ██╗  ██╗       █████╗  ██████╗")
                    win.addstr(y + yoffset - 4 - offset, x - 27, "██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝      ██╔══██╗██╔════╝")
                    win.addstr(y + yoffset - 3 - offset, x - 27, "██║  ██║███████║██████╔╝█████═╝ █████╗██║  ██║╚█████╗ ")
                    win.addstr(y + yoffset - 2 - offset, x - 27, "██║  ██║██╔══██║██╔══██╗██╔═██╗ ╚════╝██║  ██║ ╚═══██╗")
                    win.addstr(y + yoffset - 1 - offset, x - 27, "██████╔╝██║  ██║██║  ██║██║ ╚██╗      ╚█████╔╝██████╔╝")
                    win.addstr(y + yoffset - 0 - offset, x - 27, "╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝       ╚════╝ ╚═════╝ ")

                    for i in range(scl + 1):
                        win.addstr(y + 8, x - round(scl / 2) - 2, "[" + "#" * i + "-" * (scl - i) + ']')
                        win.addstr(y + 10, x - round(scl / 2) - 2 + 6, "Booting...")
                        win.refresh()
                        time.sleep(0.07)

                    time.sleep(0.6)
                    win.attroff(color_pair(1))
                    endwin()
                except:
                    pass

os.system(clear_command)

if '--nologin' in sys.argv:
    os.system("python3 init.py --bcomp --nologin")
else:
    os.system('python3 init.py --bcomp')