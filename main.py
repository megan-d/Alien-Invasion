
import asyncio
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

async def main():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make a ship, a group to store bullets in, and a group of aliens
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens) 
    
    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(aliens)
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets, aliens=aliens)

asyncio.run(main())
