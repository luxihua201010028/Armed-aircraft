import sys
import pygame


def check_events(ship):
    # 监视键盘和鼠标状态
    for event in pygame.event.get():
        # 如果单击关闭按钮，退出游戏
        if event.type == pygame.QUIT:
            # 退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 检测到键盘事件
            if event.type == pygame.K_RIGHT:  # 检测到是向右的键
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship, back_ground_image):
    """更新屏幕上的图像，并切换到新图像"""
    # 每次循环都重新绘制屏幕
    screen.fill(ai_settings.bg_color)
    # 缓冲区中绘制图像
    screen.blit(back_ground_image, (0, 0))
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()