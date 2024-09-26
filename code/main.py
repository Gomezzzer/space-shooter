import pygame
import random
from os.path import join 

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock() 

# plain surface 
surf = pygame.Surface((100, 200))
surf.fill('orange') 
x = 100

# imports
player_surf = pygame.image.load(join('../images/player.png')).convert_alpha() 
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))  
player_direction = pygame.math.Vector2(2,-1)
player_speed = 10  

star_surf = pygame.image.load(join('../images/star.png')).convert_alpha() 
star_positions = [(random.randint(0, WINDOW_WIDTH - star_surf.get_width()), 
                   random.randint(0, WINDOW_HEIGHT - star_surf.get_height())) 
                  for _ in range(20)]

meteor_surf = pygame.image.load(join('../images/meteor.png')).convert_alpha() 
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)) 

laser_surf = pygame.image.load(join('../images/laser.png')).convert_alpha() 
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))  


while running:
    clock.tick(10)  
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game 
    display_surface.fill('darkgrey') 
    # Draw stars at their random positions
    for pos in star_positions: 
        display_surface.blit(star_surf, pos) 
            
    display_surface.blit(meteor_surf, ( meteor_rect))   
    display_surface.blit(laser_surf, ( laser_rect))   
    
    #player movement 
    player_rect.center += player_direction * player_speed  
    display_surface.blit(player_surf, ( player_rect)) 
    
    
    pygame.display.update()      

pygame.quit()

