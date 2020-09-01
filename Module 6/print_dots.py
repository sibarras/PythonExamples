#! /usr/bin/python
from time import sleep


class screen:
    def __init__(self, dimensions=tuple):
        self.dimensions = dimensions
    
    def __str__(self):
        return str(self.dimensions)

    def output(self, snakebody):
        pass
