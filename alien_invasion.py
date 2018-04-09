import pygame
import game_functions

from settingsCLS import Settings
from ship import Ship


def ran_game():
    # 初始化并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #实例化一艘飞船
    ship = Ship(ai_settings, screen)

    # 进入程序主循环
    while True:
        game_functions.check_events(ship)
        ship.update()
        game_functions.update_screen(ai_settings, ship, screen)

ran_game()