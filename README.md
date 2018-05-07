# gamepy
A Python GB emulator (wip)

## Emulator
`python disasemble.py <romname>`

Despite the name, `disassembler.py` is the emulator.  It doesn't work very well, but is can do some simple GBA programs such as the GB BIOS.

## Background frame renderer

`python gbvideo/testrender.py`

Draws the background frame for a `testscreen.dump` GB memeory dump file (one is not provided).

If you want to test this out, you can use BGB or antother emulator that can do memory dumps, 
do a full dump of the memory for a frame to test (i.e. starting from `0x00`)
and save it in the `gbvideo` folder as `testscreen.dump`.
