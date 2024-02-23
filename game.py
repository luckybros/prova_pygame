import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks()/1000 - start_time)
    score_surf = test_font.render(f'{current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

pygame.init()

# creating screen
screen = pygame.display.set_mode((800,400)) 
pygame.display.set_caption('SUPER GIOCO')

clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame_test/font/Pixeltype.ttf', 50)
game_active = False
start_time = 0

sky_surf = pygame.image.load('pygame_test/graphics/Sky.png').convert()
ground_surf = pygame.image.load('pygame_test/graphics/ground.png').convert()

end_game_surf = test_font.render('CIAO', True, (255,255,255))
end_game_rect = end_game_surf.get_rect(center = (400, 200))

enemy_surf = pygame.image.load('pygame_test/graphics/snail/brie.png').convert_alpha()
enemy_rect = enemy_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('pygame_test/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   
                exit()
            if game_active:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player_rect.bottom == 300:
                        player_gravity = -20
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
            
    if game_active:        
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surf, score_rect)
        
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0, 300))
        screen.blit(enemy_surf, enemy_rect)
        screen.blit(player_surf, player_rect)

        display_score()

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 300

        # enemy
        enemy_rect.left -= 8
        if enemy_rect.left < -100: enemy_rect.left = 800 

        # ends the game if the enemy is touched
        if enemy_rect.colliderect(player_rect):
            enemy_rect.left = 800
            game_active = False
            start_time = int(pygame.time.get_ticks()/1000)
    
    else:
        screen.fill('Black')
        screen.blit(end_game_surf, end_game_rect)

    pygame.display.update()
    clock.tick(60)  
