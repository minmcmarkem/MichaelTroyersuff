import pygame

############################################    LISTS
tiles_list=pygame.sprite.Group()
clicks_list=pygame.sprite.Group()


#############################################    INTS
clicked=0
unclicked=1
middle=0

# absulute time
at=0

# unit time
ut=0

# refresh time
rt=0

rt2=0

# time multiplier
time_multi=10000

#the frames per second
fps=20

####camera

rel_x=0
rel_y=0

this_x=0
this_y=0

last_x=0
last_y=0

############################################ importat

clock = pygame.time.Clock()
win=pygame.display.set_mode((1200, 800))

