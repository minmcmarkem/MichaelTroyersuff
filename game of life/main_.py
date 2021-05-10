import pygame
import time
import globals_
import tile_
import map_

pygame.init()



red_space = pygame.image.load("red_square.png")
blue_space = pygame.image.load("red_square.png")
white_space = pygame.image.load("red_square.png").convert_alpha
#.convert_alpha(
running=1
'''
tile_.Tile_Tile(10,10,"white",1,1)
tile_.Tile_Tile(10,70,"white",2,1)
tile_.Tile_Tile(10,130,"white",3,1)
tile_.Tile_Tile(70,10,"white",1,2)

tile_.Tile_Tile(70,130,"white",3,2)
tile_.Tile_Tile(130,10,"white",1,3)
tile_.Tile_Tile(130,70,"white",2,3)
tile_.Tile_Tile(130,130,"white",3,3)
tile_.Tile_Tile(70,70,"red",2,2)
'''






#tile_.make_tiles(1)

def move(start_x,start_y):
    pass


class Point(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = ("MOUSE.png")
        globals_.clicks_list.add(self)
        
        self.rect = (pygame.image.load(self.image)).get_rect()
        self.rect.x=x
        self.rect.y=y
        self.image=(pygame.image.load(self.image)).convert_alpha()
        self.t=0
        

    def update(self):
        b=pygame.sprite.spritecollide(self, globals_.tiles_list, False)
        for Tile_Tile in b:
            Tile_Tile.clicked(self)
        
        globals_.win.blit(self.image, (self.rect.x, self.rect.y))
        self.t+=1
        if self.t>globals_.time_multi:
            globals_.clicks_list.remove(self)
            self.kill()

        


        #globals_.clicks_list.remove(self)

        
#collisions = pygame.sprite.collide(Point(my_x, my_y), my_group, False)


def run ():
    global x
    global y
    global clicked
    global unclicked
    global middle
    global at
    global ut
    global rt
    

    font = pygame.font.Font('freesansbold.ttf', 12)
    text = font.render('GeeksForGeeks', True,(100,100,100))
    textRect = text.get_rect()
    textRect.center = (1100, 750)
    clock= pygame.time.Clock()
    while running==1:
        


        
        keys = pygame.key.get_pressed()
        ggg=pygame.mouse.get_pressed()
        if ggg== (1,0,0):
            if clicked==0 and unclicked==1:
                pos = pygame.mouse.get_pos()
                #print(repr(pos))
                b=pygame.mouse.get_pos()
                Point(b[0],b[1])
                clicked=1
                unclicked=0

        if ggg== (0,1,0):
            print ("middel")
            pos = pygame.mouse.get_pos()
            # print(repr(pos))
            b = pygame.mouse.get_pos()
            #move(b[0], b[1])
            middle=1
            map_.move()




        if ggg== (0,0,0):
            unclicked=1
            clicked=0
            middle=0

        
        ut=0
        pt = clock.tick()
        globals_.rt = globals_.rt + pt
        globals_.rt2 = globals_.rt2 + pt

        if globals_.rt>globals_.time_multi:

           globals_.rt=globals_.rt-globals_.time_multi
           if globals_.rt>globals_.time_multi*2:
               globals_.rt=globals_.time_multi*2
           text = font.render(repr(globals_.ut), True,(100,100,100))
           globals_.ut=globals_.ut+1
           for Tile_Tile in globals_.tiles_list:
               Tile_Tile.recount()



        if globals_.rt2>30:
            globals_.rt2=globals_.rt2-30
            if globals_.rt2>globals_.rt2*2:
                globals_.rt2=globals_.rt2*2

            globals_.win.fill((30, 150, 50))
            globals_.tiles_list.update()
            globals_.win.blit(text, textRect)
            #pygame.display.update()
        #print (clock.tick())
        #print (globals_.rt)
        #clock.tick()
        #globals_.tiles_list.update()
        globals_.clicks_list.update()
        pygame.display.update()


        pygame.event.get ()
        globals_.at+=1
        globals_.rt+=1

        #print (globals_.rt2)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
           map_.move(3,0)

        if keys[pygame.K_d]:
            map_.move(-3, 0)
        if keys[pygame.K_w]:
            map_.move(0, 3)
        if keys[pygame.K_s]:
            map_.move(0, -3)
        if keys[pygame.K_e]:
            tile_.make_tiles(1)


run ()
