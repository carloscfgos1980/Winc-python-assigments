# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

import this
import time
import math
from datetime import datetime
import sys
import greet

# Part 1
print(this)

# Part 2


def wait(sec):
    time.sleep(sec)
    return 'nothing'


print('Wait and see', wait(3))


# Part 3
def my_sin(x):
    return math.sin(x)


print('sin:\n', my_sin(10.5))

# Part 4


def iso_now():
    current_dateTime = datetime.now().isoformat()
    return current_dateTime[:-10]


print('datetime:\n', iso_now())

# Part 5


def plaform():
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows'
    }
    if sys.platform not in platforms:
        return sys.platform

    return platforms[sys.platform]


print(plaform())


# Part 6. Import a module that I create
print(greet.supergreeting('Bob'))
