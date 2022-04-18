import pygame
from parameters import *

pygame.init()

background = pygame.image.load('backgrounds/background.png')

bullet_img = pygame.image.load('sprites/bullet.png')
bullet_img = pygame.transform.scale(bullet_img, (20, 10))
bullet_img2 = pygame.image.load('sprites/bullet2.png')
bullet_img2 = pygame.transform.scale(bullet_img2, (20, 10))

player = pygame.image.load('players/player1.png')
player = pygame.transform.scale(player, (usr_height, usr_width))

player2 = pygame.image.load('players/player2.png')
player2 = pygame.transform.scale(player2, (usr_height2, usr_width2))

bot = pygame.image.load('players/bot.png')
bot = pygame.transform.scale(bot, (usr_height2, usr_width2))
# растительность
kust = pygame.image.load('sprites/kust.png')
kust = pygame.transform.scale(kust, (100, 70))
kust1 = pygame.image.load('sprites/kust.png')
kust1 = pygame.transform.scale(kust1, (100, 70))
kust2 = pygame.image.load('sprites/kust.png')
kust2 = pygame.transform.scale(kust2, (100, 70))
kust3 = pygame.image.load('sprites/kust.png')
kust3 = pygame.transform.scale(kust3, (100, 70))

# хп
health_img = pygame.image.load('sprites/heart.png')
health_img = pygame.transform.scale(health_img, (30, 30))
