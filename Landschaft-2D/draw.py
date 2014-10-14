import sys
import time
from random import randint 
import pygame #import and init pygame
import pygame.gfxdraw
pygame.init() 

# create the screen
# ,pygame.FULLSCREEN
height = 1000
width = 1800
window = pygame.display.set_mode((width, height))

window.fill((255, 255, 255))

img = pygame.image.load('baum_mies_mit_rahmen.png')
img = pygame.transform.scale(img, (60, 130))
pygame.display.flip()

def pilz(x,y):
	w=randint(200,255)
	#pygame.draw.pie(window,x,y,40,1,200, )
	p_r=randint(200,255)
	p_and=randint(0,50)
	pygame.draw.polygon(window,(p_r,p_and,p_and),[[x+10, y+10], [x, y+20], [x+20, y+20]], 0)
	pygame.draw.rect(window,(w,w,w),(x+7,y+20,6,10))
	pygame.display.flip()

n=1
wh=1000.1
y=0.1
wars=10
while n < wh:
	x = randint(-64,width+64)
	y = y + ((height-134)/wh)
	zufall= randint(1,wars+1)
	if(zufall==1):
#		print "zufall"
#		print(c)
		window.blit(img,(x,y))
		pilz(x,y)
	pygame.display.flip()
# 	time.sleep(1/wh)
	n += 1

n = 1
wh = 1000.1
y = 0.1
wars = 10
while n < wh:
# 	a=randint(0,100)
# 	pygame.draw.circle(window, (a, randint(100,255), a), (40,40), 40)
	y = y + ((height - 134) / wh)
	zufall = randint(1, wars + 1)
	if(zufall == 1):
# 		print "zufall"
# 		print(c)
		x = randint(-64, width + 64)
		window.blit(img, (x, y))
	pygame.display.flip()
# 	time.sleep(1/wh)
	n += 1

# draw it to the screen

time.sleep(5)
