'''

@author: Brian Jimenez-Garcia
@contact: brian.jimenez@bsc.es
'''

from gui import Color
from gui.ColorMap import ColorMap

class Uniform(ColorMap):
    
    def __init__(self, color):
        super(Uniform, self).__init__()
        self.color = color
    
    def get_color(self):
        return self.color
