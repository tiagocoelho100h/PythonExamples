import pygame
from pygame.locals import *

pygame.init()

tela = pygame.display.set_mode([640, 480])
pygame.display.set_caption('Detecta Colisão')
clock = pygame.time.Clock()

img1 = pygame.image.load('img1.png')
img2 = pygame.image.load('img2.png')

running = True
x, y = 0, 0

# Manter tecla pressionada
pygame.key.set_repeat(1, 1)

while running == True:
	clock.tick(60)

	for a in pygame.event.get():
		if a.type == pygame.QUIT:
			running = False
			print('Bye, Bye!')

		if a.type == pygame.KEYDOWN:
			if a.key == pygame.K_w:
				y -= 20

			if a.key == pygame.K_s:
				y += 20

			if a.key == pygame.K_a:
				x -= 20

			if a.key == pygame.K_d:
				x += 20
	
	area_img1 = pygame.Rect(x, y, 100, 100)
	area_img2 = pygame.Rect(200, 200, 50, 50)

	if area_img1.colliderect(area_img2):
		pygame.time.wait(2000)
		running = False
		print('Game over!')

	# Colisão limete tela
	if y <= 0:
		y = 0

	elif y >= 480:
		y = 380

	if x <= 0:
		x = 0

	elif x >= 540:
		x = 540
	
	# Imprime objetos na tela
	tela.fill([0, 0, 0])
	tela.blit(img1, area_img1)
	tela.blit(img2, [200, 200])
	pygame.display.update()

pygame.quit()