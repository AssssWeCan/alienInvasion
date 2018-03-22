import sys
import pygame
from settingsCLS import Settings
from ship import Ship

def ran_game():
    # 初始化并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #实例化一艘飞船
    ship = Ship(screen)

    # 进入程序主循环
    while True:

        # 监视鼠标和键盘的事件
        for event in pygame.event.get():
            if event == pygame.QUIT:
                sys.exit()

        # 每次循环都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # 让最近绘制的屏幕可见
        pygame.display.flip()

ran_game()