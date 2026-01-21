import pygame
import math
import sys
import random

# 初始化 Pygame
pygame.init()
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("同向运动：高亮随快球增长")

# 颜色定义
WHITE, RED, GREEN, GRAY = (255, 255, 255), (255, 0, 0), (0, 255, 0), (220, 220, 220)
HIGHLIGHT = (255, 165, 0) 
ARROW_COLOR = (30, 30, 30)

# 圆环参数
CENTER = (WIDTH // 2, HEIGHT // 2)
RING_RADIUS = 200
RING_WIDTH = 6
BALL_RADIUS = 12

# 1. 速度逻辑与两行打印
base_speed = 0.04
speed_red = base_speed * random.uniform(0.95, 1.05)
speed_green = base_speed * random.uniform(0.95, 1.05)

print(f"红色小球运行速度: {speed_red:.6f}")
print(f"绿色小球运行速度: {speed_green:.6f}")

# 判定谁是持续领先的快球
is_green_faster = speed_green > speed_red

# 初始角度
angle_red = 0.0
angle_green = 0.5
clock = pygame.time.Clock()

def draw_arrow_head(surface, color, pos, angle, size=15):
    """绘制指向运动方向的箭头"""
    p1 = (pos[0] + size * math.cos(angle), pos[1] + size * math.sin(angle))
    p2 = (pos[0] + size * 0.6 * math.cos(angle + 2.6), pos[1] + size * 0.6 * math.sin(angle + 2.6))
    p3 = (pos[0] + size * 0.6 * math.cos(angle - 2.6), pos[1] + size * 0.6 * math.sin(angle - 2.6))
    pygame.draw.polygon(surface, color, [p1, p2, p3])

# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    
    # 2. 更新角度 (确保在 0 到 2pi 之间)
    angle_red = (angle_red + speed_red) % (2 * math.pi)
    angle_green = (angle_green + speed_green) % (2 * math.pi)

    # 3. 绘制底色圆环
    pygame.draw.circle(screen, GRAY, CENTER, RING_RADIUS, RING_WIDTH)

    # 4. 确定快慢球角色
    if is_green_faster:
        fast_a, slow_a = angle_green, angle_red
    else:
        fast_a, slow_a = angle_red, angle_green

    # 5. 绘制高亮弧线 (核心：消除突变逻辑)
    # 映射到 Pygame 的逆时针坐标系
    p_fast = -fast_a
    p_slow = -slow_a
    
    # 在 Pygame arc 中，从 start 到 end 是逆时针画的
    # 数学上 slow 到 fast 是顺时针，等同于 Pygame 里 fast 到 slow 是逆时针
    # 我们固定从 p_fast 开始画，画到 p_slow
    start_draw = p_fast
    end_draw = p_slow
    
    # 如果起始角度大于结束角度，增加 2pi 确保顺着圆周画过去
    if start_draw > end_draw:
        end_draw += 2 * math.pi

    rect = (CENTER[0]-RING_RADIUS, CENTER[1]-RING_RADIUS, RING_RADIUS*2, RING_RADIUS*2)
    pygame.draw.arc(screen, HIGHLIGHT, rect, start_draw, end_draw, RING_WIDTH + 2)

    # 6. 绘制箭头 (紧跟在快球后面)
    arrow_gap = (BALL_RADIUS + 8) / RING_RADIUS
    arrow_a = fast_a - arrow_gap
    ax = CENTER[0] + RING_RADIUS * math.cos(arrow_a)
    ay = CENTER[1] + RING_RADIUS * math.sin(arrow_a)
    draw_arrow_head(screen, ARROW_COLOR, (ax, ay), fast_a + math.pi/2)

    # 7. 绘制小球坐标
    rx, ry = CENTER[0] + RING_RADIUS * math.cos(angle_red), CENTER[1] + RING_RADIUS * math.sin(angle_red)
    gx, gy = CENTER[0] + RING_RADIUS * math.cos(angle_green), CENTER[1] + RING_RADIUS * math.sin(angle_green)
    
    pygame.draw.circle(screen, RED, (int(rx), int(ry)), BALL_RADIUS)
    pygame.draw.circle(screen, GREEN, (int(gx), int(gy)), BALL_RADIUS)

    pygame.display.flip()
    clock.tick(60)
