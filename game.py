import pygame
from sys import exit

pygame.init()

# creating screen
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('SUPER GIOCO')

clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame_test/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('pygame_test/graphics/Sky.png')
ground_surface = pygame.image.load('pygame_test/graphics/ground.png')
text_surface = test_font.render('OH YEAH!!', False, 'Black')

enemy_surface = pygame.image.load('pygame_test/graphics/snail/snail1.png')
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()
    
    #screen.blit(sky_surface, (0,0))
    #screen.blit(ground_surface, (0, 300))
    #screen.blit(text_surface, (300, 50))
    screen.blit(enemy_surface, (snail_x_pos, 265))
    snail_x_pos -= 4

    if snail_x_pos < -100:
        snail_x_pos = 800

    pygame.display.update()
    clock.tick(60)  
