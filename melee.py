# Programmed by:
# Mr. Gilder (corporate entity)
# JJ (the resident president)
# and Rydog (Hyaaaaah) Agundez
# Smite is a bad game.

import pygame
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("World Meme database")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
movie = pygame.movie.Movie(falco.mpg) 
  
# tell the movie to render onto the surface
movie.set_display( 700,500 )
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            movie.play()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
