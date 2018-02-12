import render

fh = open('testscreen.dump', 'rb')
mem = bytearray(fh.read())

render.renderGBScreen(mem)