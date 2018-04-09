import sys

import pygame


def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False


def check_events(ship):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
        # 允许飞船向左右移动
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
def update_screen(ai_setting, ship, screen):
    """实时绘制屏幕，并把最新的展现出来"""
    screen.fill(ai_setting.bg_color)
    ship.blitme()
    pygame.display.flip()