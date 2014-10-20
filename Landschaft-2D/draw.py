import pygame  # import and init pygame
import pygame.gfxdraw
from random import randint
import time


pygame.init()

# create the screen
# ,pygame.FULLSCREEN
height = 1000
width = 1800
window = pygame.display.set_mode((width, height))
weiss = randint(50, 200)
window.fill((weiss, 255, weiss))

img = pygame.image.load('baum_mies_mit_rahmen.png')
img = pygame.transform.scale(img, (60, 130))
pygame.display.flip()

def pilz(x, y):
	w = randint(200, 255)
	# pygame.draw.pie(window,x,y,40,1,200, )
	p_r = randint(200, 255)
	p_and = randint(0, 50)
	rand = randint(1, 2)
	if(rand == 1):
		pygame.draw.polygon(window, (p_r, p_and, p_and), [[x + 10, y + 10], [x, y + 20], [x + 20, y + 20]], 0)
	else:
		pygame.draw.arc(window, (p_r, p_and, p_and), (x, y + 10, 20, 20), 0, 3.1415, 10)
	pygame.draw.rect(window, (w, w, w), (x + 7, y + 20, 6, 10))
	pygame.display.flip()

# Muster START
y = 0
wh = randint(15, 30) + randint(15, 30)
while y < height:
	n = 0
	while n < wh:
		x = randint(-10, width + 10)
		r = randint(0, 170)
		g = randint(50, 255)
		sz = randint(2, 6)
		pygame.draw.circle(window, (r, g, 0), (x, y), sz)
		n += 1
	pygame.display.flip()
	y += 1
# time.sleep(5)

# Pilze START
n = 0
wh = 1000.1
y = height / 2 + (randint(0, height / 4) - randint(0, height / 4))
x = width / 2 + (randint(0, width / 4) - randint(0, width / 4))
wars = randint(5, 12)
print(wars)
while n < wh:
	x += randint(-50, 50)
	y += randint(-50, 50)
	zufall = randint(1, wars + 1)
	if(zufall == 1):
		pilz(x, y)
	pygame.display.flip()
	n += 1
# time.sleep(5)


# Baum START
n = 1
wh = 1000.1
y = 0.1
wars = randint(5, 12)
while n < wh:
	y = y + ((height - 134) / wh)
	zufall = randint(1, wars + 1)
	if(zufall == 1):
		x = randint(-64, width + 64)
		window.blit(img, (x, y))
	pygame.display.flip()
	n += 1

time.sleep(5)
