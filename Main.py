import pygame
import random
import sys
import json
from Assets import loadAsset

with open("properties.json", 'r') as prp:
	prop = json.load(prp)

if prop['settings']['default_mode'] == "game":
	game = True
elif prop['settings']['default_mode'] == "infinite":
	game = False
else:
	raise TypeError("No default_mode in properties.json")

try:
	inf = str(sys.argv[1])
	if inf == "infinite":
		game = False
except IndexError:
	game = True

pygame.init()
icon = pygame.Surface((50,50), pygame.SRCALPHA)
pygame.draw.circle(icon, pygame.Color("Yellow"), (23,23), 23, 0)
pygame.display.set_icon(icon)
screen_size = screen_width, screen_height = int(prop['screen']['screen_width']), int(prop['screen']['screen_height'])
scr = 0
lg = int(prop['settings']['guess'])
fnt = prop['settings']['font']
h = loadAsset(fnt, 40, "Guess The Number!")
ctitle = loadAsset(fnt, 40, "Choices:")
c1 = loadAsset(fnt, 50, "1")
c2 = loadAsset(fnt, 50, "2")
c3 = loadAsset(fnt, 50, "3")

rnum = loadAsset.getnum()
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Guess The Number")
running  = True
text_height = 300
clock = pygame.time.Clock()

while running:
	pygame.display.set_icon(icon)

	try:
		screen.fill(pygame.Color("White"))

		if game is True:
			screen.blit(h.text, (screen_width/2-120, 20))
			guessleft = loadAsset(fnt, 30, f"Guess Left: {lg}")
			pts = loadAsset('calibri.ttf', 30, f"Guessed: {scr}")
			screen.blit(guessleft.text, (0, screen_height-20))

		# Displaying Stuff:
		screen.blit(pts.text, (0, 10))
		screen.blit(ctitle.text, (screen_width/2-53, text_height-50))
		c1b = screen.blit(c1.text, (screen_width/3, text_height))
		c2b = screen.blit(c2.text, (screen_width/2-0.5, text_height))
		c3b = screen.blit(c3.text, (screen_width/3+screen_width/3, text_height))

		# Getting Events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: running = False
			# If Mouse Click
			if event.type == pygame.MOUSEBUTTONDOWN:
				true = True
				false = False
				# If Mouse clicked in options:
				if c1b.collidepoint(pygame.mouse.get_pos()):
					if rnum == 1 and not lg < 1:
						# If The Random Number Matches 1(and so on):
						print({"type": true, "TA": rnum, "GSD": scr})
						loadAsset.num(screen, rnum, lg,True)
						if not lg < 1:
							scr += 1
						rnum = loadAsset.getnum()
						lg += 1
					else:
						# If The Random Number Didn't Match 1:
						print({"type": false, "TA": rnum, "GSD": scr})
						loadAsset.num(screen, rnum, lg,False)
						rnum = loadAsset.getnum()
						if not lg < 1:
							lg -= 1
				if c2b.collidepoint(pygame.mouse.get_pos()):
					if rnum == 2 and not lg < 1:
						print({"type": true, "TA": rnum, "GSD": scr})
						loadAsset.num(screen, rnum, lg,True)
						if not lg < 1:
							scr += 1
						rnum = loadAsset.getnum()
						lg += 1
					else:
						print({"type": false, "TA": rnum, "GSD": scr})
						loadAsset.num(screen, rnum, lg,False)
						rnum = loadAsset.getnum()
						if not lg < 1:
							lg -= 1
				if c3b.collidepoint(pygame.mouse.get_pos()):
					if rnum == 3 and not lg < 1:
						print({"type": true, "TA": rnum, "GSD": scr})
						loadAsset.num(screen, rnum, lg,True)
						if not lg < 1:
							scr += 1
						rnum = loadAsset.getnum()
						lg += 1
					else:
						print({"type": false, "TA": rnum, "GSD": scr})
						loadAsset.num(screen, rnum, lg,False)
						rnum = loadAsset.getnum()
						if not lg < 1:
							lg -= 1
		pygame.display.flip()
		clock.tick(60)
	except pygame.error:
		print("Exit")
		running = False

pygame.quit()
sys.exit()