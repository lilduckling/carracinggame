import pygame, random, sys, time
from pygame.base import *
from pygame.locals import *

width = 446
height = 590
carwidth = 80
carheight = 144

carimg = pygame.image.load("car.png").convert_alpha()
blockimg = pygame.image.load("block.png").convert_alpha()
bgimg = pygame.image.load("background.png").convert_alpha()
explosioneffect = pygame.image.load("explode.png").convert_alpha()
gamedisplay = pygame.display.set_mode((width, height))

def pressanykey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                return
            
def textobjects(text,font):
	textSurface = font.render(text, True, (255, 0, 0))
	return textSurface,textSurface.get_rect()
            
def messagedisplay(text,size,x,y):
    font = pygame.font.Font("freesansbold.ttf",size)
    textsurface , textrectangle = textobjects(text,font)
    textrectangle.center =(x,y)
    gamedisplay.blit(textsurface,textrectangle)
	
            
def drawtext(text, font, surface, x, y):
    textobj = font.render(text, 1, (255, 255, 255))
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def lose(x, y):
    gamedisplay.blit(explosioneffect, (x, y))
    messagedisplay("YOU LOSE", 48, width / 2, height / 2)
    pygame.display.update()
    time.sleep(2)
    mainloop()

def highscore(count):
	font = pygame.font.SysFont(None,20)
	text = font.render("Score : "+str(count), True, (255, 0, 0) )
	gamedisplay.blit(text,(0,0))
	
pygame.init()
mainclock = pygame.time.Clock()
windowsurface = pygame.display.set_mode((width, height))
pygame.display.set_caption('GAME')
pygame.mouse.set_visible(False)
font = pygame.font.SysFont(None, 48)


drawtext('RACINGAJAX', font, windowsurface, width / 5 + 20, height / 3)
drawtext('press any key to start', font, windowsurface, width / 5 - 30, height /3 - 50)
pygame.display.update()
pressanykey()

def mainloop():
    bgx1 = 0
    bgx2 = 446
    bgy1 = 0
    bgy2 = -590
    bgspeed = 6
    bgspeedchange = 0
    carx = width / 2 - carwidth / 2
    cary = height - carheight
    carxchange = 0 
    roadstartx = 0
    roadendx = 446

    blockstartx = random.randrange (roadstartx, roadendx - carwidth)
    blockstarty = - 590
    blockw = 80
    blockh = 144
    blockspeed = 3
    count = 0
    gameexit = False

    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    carxchange = -5
                elif event.key == pygame.K_RIGHT:
                    carxchange = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    carxchange = 0
        carx += carxchange            
        if carx > roadendx - carwidth:
            lose(carx, cary)
        if carx < roadstartx:
            lose(carx - carwidth, cary)

        if cary < blockstarty + blockh:
            if carx >= blockstartx and carx <= blockstartx + blockw:
                lose(carx - 25, cary - carheight / 2)
            if (carx + carwidth) >= blockstartx and (carx + carwidth) <= (blockstartx + blockw):
                lose(carx, cary - carheight / 2)
        
            

        gamedisplay.blit(bgimg, (bgx1, bgy1))
        gamedisplay.blit(bgimg, (bgx2, bgy2))
        gamedisplay.blit(carimg, (carx, cary))
        gamedisplay.blit(blockimg, (blockstartx, blockstarty))
        highscore(count)
        count+=1
        blockstarty += blockspeed

        if blockstarty > height:
            blockstartx = random.randrange(roadstartx,roadendx - carwidth)
            blockstarty = -200

        bgy1 += bgspeed
        bgy2 += bgspeed

        if bgy1 >= height:
            bgy1 = -600

        if bgy2 >= height:
            bgy2 = -600

        pygame.display.update()
  
mainloop()        
