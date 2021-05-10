import pygame
import globals_

#global make
#make=11

global tx
tx=10
global ty
ty=10
global tiles_x
tiles_x=0
global tiles_y
tiles_y=0

global amountt
amountt=0

global aty
global atx

aty=0
atx=0

global goingx
global goingy

goingx=0
goingy=0
def make_tiles(j):
    #global make
    global tx
    global ty
    global tiles_x
    global tiles_y
    global aty
    global atx
    global amountt
    global goingx
    global goingy

    make=j

    #print ("good")
    #take = (make / 2) - .5
    while make>0:

        tx=(tiles_x*70)+globals_.rel_x
        ty=(tiles_y*70)+globals_.rel_y

        Tile_Tile(tx, ty, "white", tiles_x, tiles_y)

        if make>0:

            print("#### tiles #####")
            print(tiles_x, tiles_y)
            print("##### ats ######")
            print(atx, aty)

            if atx> tiles_y and goingx==0 and goingy==1:
                if aty <= tiles_y:
                    tiles_y+=1
                    aty=tiles_y
                    print ("1y")
                else:
                    tiles_y+=1
                    print("2y")

                print ("fisrt y")

            if atx> aty and goingx==1 and goingy==0:
                tiles_y=0
                tiles_x=atx
                goingx=0
                goingy=1

                print("fisrt step y")

            #######################

            if aty > tiles_x and goingy == 0 and goingx == 1:
                if atx <= tiles_x:
                    tiles_x += 1
                    atx = tiles_x
                    print ("1x")
                else:
                    tiles_x += 1
                    print("2x")
                print ("fisrt x")

            if aty > atx and goingy == 1 and goingx == 0:
                tiles_x = 0
                aty=tiles_y
                goingy = 0
                goingx = 1

                print("fisrt step x")

            if atx==aty:
                if goingx==1:
                    goingx=1
                    goingy=0
                    aty+=1
                if goingy==1:
                    goingx=0
                    goingy=1
                    atx+=1
                else:
                    goingx = 0
                    goingy = 1
                    atx += 1
                print ("FFFFFFF")

        make -= 1




    for Tiles_Tiles in globals_.tiles_list:
        Tiles_Tiles.first_date()

class Tile_Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, color,tile_x,tile_y):
        super().__init__()

        """                  \/     """
        self.done=0
        self.c_color=color
        self.color="none"
        
        self.neighbor=pygame.sprite.Group()
        if self.c_color=="red":
            self.image = ("red_square.png")
        if self.c_color=="blue":
            self.image = ("blue_square.png")
        if self.c_color=="white":
            self.image =  ("white_square.png")

        else:
            pass
        self.rect = (pygame.image.load(self.image)).get_rect()
        self.rect.x = x
        self.rect.y = y
        globals_.tiles_list.add(self)
        self.tile_x=tile_x
        self.tile_y=tile_y

        self.image=(pygame.image.load(self.image)).convert_alpha()






        #complex things

        self.population=100
        self.economics=100
        self.wealth=100
        self.ta=0
        self.t=0

    def first_date (self):
        #if self.done==1:
            #self.done=1
        for Tile_Tile in globals_.tiles_list:

            if Tile_Tile.tile_x==self.tile_x-1 and Tile_Tile.tile_y==self.tile_y+1:
                self.neighbor.add(Tile_Tile)
                #print ("Good")
                #Tile_Tile.color="blue"
            if Tile_Tile.tile_x==self.tile_x and Tile_Tile.tile_y==self.tile_y+1:
                self.neighbor.add(Tile_Tile)
                #print ("Good")
                #Tile_Tile.color="blue"
            if Tile_Tile.tile_x==self.tile_x+1 and Tile_Tile.tile_y==self.tile_y+1:
                self.neighbor.add(Tile_Tile)
                #print ("Good")
                #Tile_Tile.color="blue"
            if Tile_Tile.tile_x == self.tile_x-1 and Tile_Tile.tile_y == self.tile_y:
                self.neighbor.add(Tile_Tile)
                # print ("Good")
                #Tile_Tile.color = "blue"
            if Tile_Tile.tile_x==self.tile_x+1 and Tile_Tile.tile_y==self.tile_y:
                self.neighbor.add(Tile_Tile)
                #print ("Good")
                #Tile_Tile.color="blue"
            if Tile_Tile.tile_x == self.tile_x-1 and Tile_Tile.tile_y == self.tile_y -1:
                self.neighbor.add(Tile_Tile)
                # print ("Good")
                #Tile_Tile.color = "blue"
            if Tile_Tile.tile_x == self.tile_x and Tile_Tile.tile_y == self.tile_y -1:
                self.neighbor.add(Tile_Tile)
                # print ("Good")
                #Tile_Tile.color = "blue"
            if Tile_Tile.tile_x == self.tile_x+1 and Tile_Tile.tile_y == self.tile_y - 1:
                self.neighbor.add(Tile_Tile)
                # print ("Good")
                #Tile_Tile.color = "blue"
    #else:
        #pass


    def update(self):

        if self.c_color=="red":

            for Tile_Tile in self.neighbor:
                Tile_Tile.color="red"

        if not self.rect.x > 1500 and not self.rect.x < -100 and not self.rect.y >900 and not self.rect.y < -100 :

            globals_.win.blit(self.image, (self.rect.x, self.rect.y))



    def clicked(self,thing):
        print (self.population)
        print (self.tile_x, ",",self.tile_y)

        globals_.clicks_list.remove(thing)
        thing.kill()

    def recount(self):
        self.population = ((self.population * 1.5)//1)
        if self.c_color != self.color:
            if self.color == "red":
                # self.image = ("red_square.png")
                self.image = (pygame.image.load("red_square.png")).convert_alpha()
                self.c_color = "red"
            if self.color == "blue":
                # self.image = ("blue_square.png")
                self.image = (pygame.image.load("blue_square.png")).convert_alpha()
                self.c_color = "blue"
            if self.color == "white":
                # self.image = ("white_square.png")
                self.image = (pygame.image.load("white_square.png")).convert_alpha()
                self.c_color = "white"





