import pygame
import random
from os.path import join 

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# plain surface 
surf = pygame.Surface((100, 200))
surf.fill('orange') 
x = 100

# importing an image 
player_surf = pygame.image.load(join('../images/player.png')).convert_alpha() 
star_surf = pygame.image.load(join('../images/star.png')).convert_alpha() 

# Generate random positions for 20 stars
star_positions = [(random.randint(0, WINDOW_WIDTH - star_surf.get_width()), 
                   random.randint(0, WINDOW_HEIGHT - star_surf.get_height())) 
                  for _ in range(20)]

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game 
    display_surface.fill('darkgrey') 
    # Draw stars at their random positions
    for pos in star_positions:
        display_surface.blit(star_surf, pos)
    x += 0.1
    display_surface.blit(player_surf, (x, 150))  
    

    
    pygame.display.update()      

pygame.quit()

