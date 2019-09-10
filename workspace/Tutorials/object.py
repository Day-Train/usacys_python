#!/usr/bin/env python3

class balloon:
    def __init__(self):
        self.altitude = 0

    def climb(self):
        self.altitude = += 1

    def dive(self):
        if self.altitude > 0
            self.altitude -= 1

    def crashland(self):
        self.altitude = 0

    def setaltitude(self, newaltitude):
        if newaltitude >= 0:
            self.altitude = newaltitude

    def getaltitude(self):
        return self.altitude

    def __str__(self):
        return 'Current altitude: {}'.format(self.altitude)


