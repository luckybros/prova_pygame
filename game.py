import pygame
from sys import exit

pygame.init()

# creating screen
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('SUPER GIOCO')

clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame_test/font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('pygame_test/graphics/Sky.png').convert()
ground_surf = pygame.image.load('pygame_test/graphics/ground.png').convert()

text_surf = test_font.render('OH YEAH!!', True, 'Black')
text_rect = text_surf.get_rect(midbottom = (400, 50))

enemy_surf = pygame.image.load('pygame_test/graphics/snail/brie.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('pygame_test/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()   
            exit()
        #if event.type == pygame.MOUSEMOTION:
        #    if(player_rect.collidepoint(event.pos)): print('mouse colliding with player')
    
    screen.blit(sky_surf, (0,0))
    screen.blit(ground_surf, (0, 300))
    screen.blit(text_surf, text_rect)
    screen.blit(enemy_surf, enemy_rect)
    screen.blit(player_surf, player_rect)

    enemy_rect.left -= 4
    player_rect.left += 1

    if enemy_rect.left < -100: enemy_rect.left = 800

    #if player_rect.colliderect(enemy_rect):
    #    print('collision')

    #mouse_pos = pygame.mouse.get_pos()

    #if player_rect.collidepoint(mouse_pos):
    #    print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)  
