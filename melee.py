# Programmed by:
# Mr. Gilder (corporate entity)
# JJ (the resident president)
# and Rydog (Hyaaaaah) Agundez
# Smite is a bad game.

import pygame
WHITE = (255, 255, 255)
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("World Meme Database")

done = False
clock = pygame.time.Clock()
pygame.movie.Movie(falco.mpg)
while not done:
    screen.fill(WHITE)
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True
      elif event.type == pypgame.KEYDOWN:
        pygame.movie.Movie.play(1)
pygame.quit()
