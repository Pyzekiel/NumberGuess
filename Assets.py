import pygame
import random
import sys
import json

with open("properties.json", 'r') as prp:
	prop = json.load(prp)

class loadAsset():

	def __init__(self, fon, sz, t):
		super(loadAsset, self).__init__()
		font = pygame.font.SysFont(fon, sz)
		self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
		self.text = font.render(t, True, pygame.Color("Black"))
		pygame.draw.circle(self.image, pygame.Color("Grey"), (sz/2, sz/2), 20)
		self.rect = self.image.get_rect()

	def num(screen, n, lg, result=False):
		icon = pygame.Surface((50,50), pygame.SRCALPHA)
		if result is True:
			pygame.draw.circle(icon, pygame.Color("Blue"), (23,23), 23, 0)
		elif result is False:
			pygame.draw.circle(icon, pygame.Color("Red"), (23,23), 23, 0)
		pygame.display.set_icon(icon)

		if lg < 1:
			print("No More Guess Left")
		else:
			screen_width = int(prop['screen']['screen_width'])
			screen_height = int(prop['screen']['screen_height'])
			font = pygame.font.SysFont('calibri', 100)
			realnum = font.render(f"{n}", True, pygame.Color("Black"))
			if result is True:
				bg = 'lightblue'
			elif result is False:
				bg = 'red'
			pygame.draw.circle(screen, pygame.Color(bg), (screen_width/2, screen_height/2-100), 50, 0)
			running = int(prop['settings']['ans_timeout'])
			while running > 0:
				for event in pygame.event.get():
					if event.type == pygame.MOUSEBUTTONDOWN:
						running -= running
					if event.type == pygame.QUIT:
						running -= running
					if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
						pygame.quit()
						running = False
				screen.blit(realnum, (screen_width/2-23, screen_height/2-143))
				pygame.display.flip()
				running -= 0.01
		pass

	def getnum():
		return random.randint(1, 3)