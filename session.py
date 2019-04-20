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
        self.short_dia = ['Grab some water.', 'Stand and stretch.',
        'Make a tea.', 'Eat a fruit.', 'Draw a small doodle.',
        'Text a friend to have a good day.', 'Text your mom.',
        'Practice gratitude: write down what you\'re thankful for right now.',
        'Mini-meditation.', 'Visualize nice things.',
        'Listen to music and take a quick stroll.']
        self.long_dia = ['Walk to the park.', 'Go get a coffee.', 'Meditate.',
         'Ask someone to to go on a walk.', 'Get a pastry and walk around.',
         'Play ping-pong.', 'Draw.', 'Close your eyes.']

    def print_update(self):
        """Print Current pomodoro's and subject."""
        i = 0
        print("\033[H\033[J")
        print('Keep focused on: ' + '\x1b[36m' + self.subject + '\x1b[0m')
        print('You\'ve been focused for ' + '\x1b[35m' + str(self.hours) +
        ' hours' + '\x1b[0m')
        while i < self.pomodoro:
            print('\x1b[33m' + '|' + '\x1b[0m', end='')
            i += 1
        print('')

    def print_dialogue(self, tim):
        if tim == 0:
            num = random.randint(0,len(self.short_dia) - 1)
            messagebox.showinfo("Break time!", "5 minute break: " + self.short_dia[num])
        else:
            num = random.randint(0,len(self.long_dia) - 1)
            messagebox.showinfo("Break time!", "30 minute break: " + self.long_dia[num])

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
        self.timer()

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
        self.update()
