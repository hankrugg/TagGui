'''
 Hank Rugg, Jan 18

 Map Class for Hide and Seek Tag, console based version. This is the base class for the map.

'''


class Map:
    def __init__(self):
        self.rows = 10
        self.columns = 10
        self.array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                      ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', 'x'],
                      ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
                      ['x', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
                      ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

    def resetMap(self):
        # used to reset the actual array
        self.array = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                      ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', 'x'],
                      ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
                      ['x', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
                      ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
                      ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

    def drawMap(self):
        # used for game play to actually print the map
        for i in self.array:
            print(i)
