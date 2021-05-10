import pygame
import globals_

def move(ax,ay):
    dif_x=globals_.last_x-globals_.this_x
    dif_y=globals_.last_y-globals_.this_y

    for Tile_Tile in globals_.tiles_list:
        Tile_Tile.rect.x+=ax
        Tile_Tile.rect.y += ay
        globals_.rel_x+ax
        globals_.rel_y + ay