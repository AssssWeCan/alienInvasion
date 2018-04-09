import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并且获得其外接矩形
        self.image = pygame.image.load(r'image\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船属性中存储小数值
        self.center = float(self.rect.centerx)

        #  移动标识
        self.move_right = False
        self.move_left = False

    def update(self):
        """允许根据键盘操纵飞船移动"""
        if self.move_right and self.rect.centerx < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.move_left and self.rect.centerx > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect对像
        self.rect.centerx = self.center

    def blitme(self):
        """在指定地点绘制飞船"""
        self.screen.blit(self.image, self.rect)