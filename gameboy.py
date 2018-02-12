class Gameboy:
    r = {
        'A': 0,
        'B': 0,
        'D': 0,
        'H': 0,
        'C': 0,
        'E': 0,
        'L': 0
    }
    f = {
        'Z': 0,
        'N': 0,
        'H': 0,
        'C': 0,
    }
    sp = 0
    pc = 0

    # screen
    scrollx = 0
    scrolly = 0
    wndposx = 0
    wndposy = 0

    mem = bytearray(65535)

    def memwrite(self, addr, val):
        pass
    def memread(self, addr):
        pass
    def getscreen(self):
        