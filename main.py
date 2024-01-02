
import asyncio
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

async def main():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    ship = Ship(screen, ai_settings)
    # Make a group to store bullets in
    bullets = Group()
    
    # Make an alien
    alien = Alien(ai_settings=ai_settings, screen=screen)
    
    # Start the main loop for the game
   
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets, alien=alien)

asyncio.run(main())
