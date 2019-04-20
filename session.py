#!python

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
