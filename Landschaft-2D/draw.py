import pygame  # import and init pygame
from random import randint
import sys
import time
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
