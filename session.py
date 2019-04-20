#!python
import time
import sys

class Session(object):

    def __init__(self):
        self.subject = input('Enter the subject you\'re working on today: ')
        self.pomodoro = 0
        self.hours = 0

    def print_update(self):
        """Print Current pomodoro's and subject."""
        i = 0
        print("\033[H\033[J")
        print('Keep focused on: ' + self.subject)
        print('You\'ve been focused for ' + str(self.hours) + ' hours.')
        while i < self.pomodoro:
            print('|', end='')
            i += 1

    def update(self):

    def timer(self):
        """Keep track of 25 minute intervals"""
        time_start = time.time()
        seconds = 0
        minutes = 0

        while minutes < 25:
            try:
                sys.stdout.flush()
                time.sleep(1)
                seconds = int(time.time() - time_start) - minutes * 60
                if seconds >= 60:
                    minutes += 1
                    seconds = 0
            except KeyboardInterrupt, e:
                break
        return self.update()
