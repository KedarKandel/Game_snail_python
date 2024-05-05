


import pygame

from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("fighter")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf",50)

sky_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My Game", False, "Green").convert()
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 800


while True:
    for event in pygame.event.get():
        if(event.type== pygame.QUIT):
            pygame.quit()
            exit()
    pygame.display.update()
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, ( snail_x_pos, 250))
    snail_x_pos -= 3
   
    if snail_x_pos < -100 : snail_x_pos = 800
    
    clock.tick((60))

