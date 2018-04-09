#pygame打飞机小游戏的部分功能总结
* 首先装好`pygame`，然后在游戏运行的函数开始一定要进行pygame的初始化，即`pygame.init`
* 窗口用`pygame.display.set_mode((1200,800))`进行绘制
* 窗口名称，使用`pygame.display.set_caption("INVASION")`表述
* 可用`pygame.event.get()`监视键盘和鼠标事件，配合`sys.exit()`退出程序
```python
import sys
import pygame
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
```
* 可用`screen.fill(230, 230, 230)`绘制窗口背景色
* `image = pygame.image.load('images/ship.bmp)`得到图像，`image.rect = image.get_rect()`可以把图像像矩形那样处理。设定`image.rect.bottom`可以确定图像的位置，bottom可以替换为top、left、right、center,中心也可用centerx(X轴中心)、centery(Y轴中心)。
* 飞船的左右移动可以用`image.rect.centerx`的加减控制
