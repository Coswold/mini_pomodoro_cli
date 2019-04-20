#!python
import time
import sys
from tkinter import messagebox
import random

class Session(object):

    def __init__(self):
        self.subject = input('Enter the subject you\'re working on today: ')
        self.pomodoro = 0
        self.hours = 0.0

    def print_update(self):
        """Print Current pomodoro's and subject."""
        i = 0
        print("\033[H\033[J")
        print('Keep focused on: ' + self.subject)
        print('You\'ve been focused for ' + str(self.hours) + ' hours.')
        while i < self.pomodoro:
            print('|', end='')
            i += 1
        print('')

    def print_dialogue(self, tim):
        if tim == 0:
            random = random.randint(0,len(short_dia) - 1)
            print('Take a short break!')
            messagebox.showinfo("Break time!", "5 minute break: " + short_dia[random])
        else:
            random = random.randint(0,len(long_dia) - 1)
            print('Take a long break!')
            messagebox.showinfo("Break time!", "30 minute break: " + long_dia[random])

    def rest(self, tim):
        self.print_dialogue(tim)
        enter = True
        while enter == True:
            enter = input("Press [Enter] when you\'re ready to focus again.")

    def update(self):
        self.pomodoro += 1
        self.hours += 0.5
        if self.pomodoro > 3:
            self.pomodoro = 0
            self.rest(1)
        else:
            self.rest(0)
        self.print_update()
        return self.timer()

    def timer(self):
        """Keep track of 25 minute intervals"""
        time_start = time.time()
        seconds = 0
        minutes = 0

        while seconds < 25:
            try:
                sys.stdout.flush()
                time.sleep(1)
                seconds = int(time.time() - time_start) - minutes * 60
                if seconds >= 60:
                    minutes += 1
                    seconds = 0
            except KeyboardInterrupt:
                raise KeyError('You have finished the session.')
        return self.update()
