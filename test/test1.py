import pygame
import sys

# 初始化pygame
pygame.init()

# 设置窗口大小
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Victory Screen Example')

# 设置颜色
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# 加载字体
font = pygame.font.Font(None, 74)

# 游戏主循环
running = True
victory = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 模拟胜利条件
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            victory = True

    # 填充背景色
    screen.fill(white)

    if victory:
        # 绘制胜利画面
        victory_text = font.render('Victory!', True, green)
        screen.blit(victory_text, (window_size[0] // 2 - victory_text.get_width() // 2, window_size[1] // 2 - victory_text.get_height() // 2))
    else:
        # 绘制游戏画面
        message_text = font.render('Press SPACE to win!', True, black)
        screen.blit(message_text, (window_size[0] // 2 - message_text.get_width() // 2, window_size[1] // 2 - message_text.get_height() // 2))

    # 更新屏幕显示
    pygame.display.flip()

# 退出pygame
pygame.quit()
sys.exit()