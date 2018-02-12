import sys
import code
import pygame
import math
import pygame.surfarray as surfarray
import numpy as np

pygame.init()
pygame.display.set_mode((256,256))

gbcolors = list()
gbcolors.append((15, 56, 16))
gbcolors.append((49, 97, 48))
gbcolors.append((136, 173, 17))
gbcolors.append((151, 187, 17))


def renderGBScreen(mem):
    # Each screen is comprised of 32x32 tiles.
    # Each tile is comprised of 8x8 pixels.
    # The screen is comprised of the background (32 rows in VRAM, each 32 bytes long)
    # which says what background tiles to render.

    # There are two different Background Tile Maps. One is
    # located from $9800-9Bff. The other from $9C00-9FFF.

    # These two tile maps show where the tiles should be placed.
    bgtm1 = mem[0x9800:0x9C00]
    bgtm2 = mem[0x9C00:0xA000]
    
    
    # These are the actual tiles, stored in the Tile pattern Tables
    # ($8000-8FFF) and ($8800-97FF) 
    tpt1 = mem[0x8000:0x9000]
    tpt2 = mem[0x8800:0x9800]
    
    pos = 0
    tiles1 = list()
    while (pos < 0x1000):
        # Each tile in the list is 16 bytes.
        # Every two bytes represent a 8-pixel line.
        tile = np.zeros((8,8,3))
        i = pos
        while i < pos + 16:
            a = bin(tpt1[i])[2:].zfill(8)         
            b = bin(tpt1[i+1])[2:].zfill(8)
            # code.interact(local=locals())
            line = int((i%16)/2)
            for j in range(8):
                color = int(a[j]) + int(b[j])
                tile[line, j] = gbcolors[color]
            i += 2
        tiles1.append(tile)
        pos += 16
    
    tiles2 = list()
    pos = 0
    while (pos < 0x1000):
        # Each tile in the list is 16 bytes.
        # Every two bytes represent a 8-pixel line.
        tile = np.zeros((8,8,3))
        i = pos
        while i < pos + 16:
            a = bin(tpt2[i])[2:].zfill(8)         
            b = bin(tpt2[i+1])[2:].zfill(8)
            # code.interact(local=locals())
            line = int((i%16)/2)
            for j in range(8):
                color = int(a[j]) + int(b[j])
                tile[line, j] = gbcolors[color]
            i += 2
        tiles2.append(tile)
        pos += 16
    
    # Tiles is now the background sprites.
    # Render the background.

    screen = pygame.surface.Surface((256, 256))
    screen.fill((0,0,0))

    for i in range(32):
        for j in range(32):
            tilenum = bgtm1[32*i + j]
            if (tilenum < 0):
                tile = tiles1[tilenum]
            else:
                tile = tiles2[tilenum - 128]
            # print(tile)
            tile_surf = pygame.surface.Surface((8, 8))
            pygame.surfarray.blit_array(tile_surf, tile)
            tile_surf_rect = tile_surf.get_rect()
            tile_surf_rect.x = i*8
            tile_surf_rect.y = j*8
            screen.blit(tile_surf, tile_surf_rect)

    screen = pygame.transform.rotate(screen, 270)
    screen =  pygame.transform.flip(screen, 1, 0)
    pygame.image.save(screen, "test.png")
    
