import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, game_settings, screen, ship, bullets):
    """Check key down events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    if event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Check key up events"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(game_settings, screen, ship, bullets):
    """Check keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(game_settings, screen, ship, aliens, bullets):
    """Update image on screen and draw new screen"""
    # add screen background
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # add ship to screen
    ship.blitme()
    # add alien to screen
    aliens.draw(screen)
    # display the last screen
    pygame.display.flip()

def update_bullets(bullets):
    """Update bullets position and remove old bullets"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def create_fleet(game_settings, screen, aliens):
    """Create alien fleet"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    avaliable_screen_width = game_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(avaliable_screen_width / (2 * alien_width))
    #create first fleet
    for alien_number in range(number_aliens_x):
        alien = Alien(game_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
        #create alien
