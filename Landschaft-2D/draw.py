import sys
import time
from random import randint 
import pygame #import and init pygame
pygame.init() 

#create the screen
#,pygame.FULLSCREEN
height=480
width=1000
window = pygame.display.set_mode((width, height)) 

#draw a line - see http://www.pygame.org/docs/ref/draw.html for more 
window.fill((255, 255, 255))
#pygame.draw.line(window, (0, 0, 0), (0, 0), (30, 50))
img = pygame.image.load('baum_mies_mit_rahmen.png')
img = pygame.transform.scale(img, (60, 130))
pygame.display.flip() 
x=1
wh=1000.1
c=0.1
wars=10
while x < wh:
#	a=randint(0,100)
#	pygame.draw.circle(window, (a, randint(100,255), a), (40,40), 40)
	b = randint(-64,width+64)
	c = c + ((height-134)/wh)
	zufall= randint(1,wars+1)
	if(zufall==1):
#		print "zufall"
#		print(c)
		window.blit(img,(b,c))
	pygame.display.flip()
#	time.sleep(1/wh)
	x+=1

#draw it to the screen

time.sleep(5)
