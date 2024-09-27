import pygame
import random
from os.path import join 

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(join('../images/player.png')).convert_alpha() 
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))  

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

player = Player()

# imports
# player_surf = pygame.image.load(join('../images/player.png')).convert_alpha() 
# player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))  
# player_direction = pygame.math.Vector2() 
# player_speed = 300  

star_surf = pygame.image.load(join('../images/star.png')).convert_alpha() 
star_positions = [(random.randint(0, WINDOW_WIDTH - star_surf.get_width()), 
                   random.randint(0, WINDOW_HEIGHT - star_surf.get_height())) 
                  for _ in range(20)]

meteor_surf = pygame.image.load(join('../images/meteor.png')).convert_alpha() 
meteor_rect = meteor_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)) 

laser_surf = pygame.image.load(join('../images/laser.png')).convert_alpha() 
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT - 20))  


while running:
    dt = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
       # if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
       #     print(1) 
       # if event.type == pygame.MOUSEMOTION:  
       #     player_rect.center = event.pos   
       
    # input 
    # pygame.mouse.get_pos() 
    # keys = pygame.key.get_pressed()
    # player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])  
    # player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP]) 
    # player_direction = player_direction.normalize() if player_direction else player_direction
    # player_rect.center += player_direction * player_speed * dt 
    
    recent_keys = pygame.key.get_just_pressed()
    if recent_keys[pygame.K_SPACE]:
        print('fire laser')
               
    # Draw the game 
    display_surface.fill('darkgrey') 
    # Draw stars at their random positions
    for pos in star_positions: 
      display_surface.blit(star_surf, pos) 
            
    display_surface.blit(meteor_surf, ( meteor_rect))   
    display_surface.blit(laser_surf, ( laser_rect))   
    # display_surface.blit(player_surf, ( player_rect)) 
    
    
    
    
    pygame.display.update()      

pygame.quit()

