import pygame  # import and init pygame
import pygame.gfxdraw
from random import randint
import sys
import time


pygame.init()

# create the screen
# ,pygame.FULLSCREEN
height = 1000
width = 1800
window = pygame.display.set_mode((width, height))

window.fill((150, 255, 150))

img = pygame.image.load('baum_mies_mit_rahmen.png')
img = pygame.transform.scale(img, (60, 130))
pygame.display.flip()

def pilz(x, y):
	w = randint(200, 255)
	# pygame.draw.pie(window,x,y,40,1,200, )
	p_r = randint(200, 255)
	p_and = randint(0, 50)
	pygame.draw.polygon(window, (p_r, p_and, p_and), [[x + 10, y + 10], [x, y + 20], [x + 20, y + 20]], 0)
	pygame.draw.rect(window, (w, w, w), (x + 7, y + 20, 6, 10))
	pygame.display.flip()

n = 0
wh = 1000.1
y = height / 2 + (randint(0, height / 4) - randint(0, height / 4))
print(randint(-height / 4, height / 4))
x = width / 2 + (randint(0, width / 4) - randint(0, width / 4))
wars = 10
while n < wh:
	x += randint(-50, 50)
	y += randint(-50, 50)
	zufall = randint(1, wars + 1)
	if(zufall == 1):
		pilz(x, y)
	pygame.display.flip()
	n += 1

n = 1
wh = 1000.1
y = 0.1
wars = 10
while n < wh:
	y = y + ((height - 134) / wh)
	zufall = randint(1, wars + 1)
	if(zufall == 1):
		x = randint(-64, width + 64)
		window.blit(img, (x, y))
	pygame.display.flip()
	n += 1

time.sleep(5)
