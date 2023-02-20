import pygame
import random

pygame.init()

# 游戏窗口的宽度和高度
width = 640
height = 480

# 创建游戏窗口
screen = pygame.display.set_mode((width, height))

# 设置游戏窗口的标题
pygame.display.set_caption("贪吃蛇小游戏")

# 定义贪吃蛇类
class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [(100, 100)]
        self.dx = 0
        self.dy = 0
    
    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, (0, 255, 0), (element[0], element[1], 20, 20))
    
    def move(self):
        for i in range(len(self.elements) - 1, 0, -1):
            self.elements[i] = (self.elements[i - 1][0], self.elements[i - 1][1])
        self.elements[0] = (self.elements[0][0] + self.dx, self.elements[0][1] + self.dy)

# 定义食物类
class Food:
    def __init__(self):
        self.x = random.randrange(0, width, 20)
        self.y = random.randrange(0, height, 20)
    
    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 20, 20))

# 创建贪吃蛇和食物实例
snake = Snake()
food = Food()

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 处理用户输入
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.dx = -20
        snake.dy = 0
    elif keys[pygame.K_RIGHT]:
        snake.dx = 20
        snake.dy = 0
    elif keys[pygame.K_UP]:
        snake.dx = 0
        snake.dy = -20
    elif keys[pygame.K_DOWN]:
        snake.dx = 0
        snake.dy = 20

    # 绘制游戏场景
    screen.fill((0, 0, 0))
    snake.move()
    snake.draw()
    food.draw()

    # 判断贪吃蛇是否吃到食物
    if snake.elements[0][0] == food.x and snake.elements[0][1] == food.y:
        snake.size += 1
        snake.elements.append((0, 0))
        food = Food()

    # 判断贪吃蛇是否撞到边界或自己
    if snake.elements[0][0] < 0 or snake.elements[0][0] >= width or snake.elements[0][1] < 0 or snake.elements[0][1] >= height:
        running = False
    for i in range(1, len(snake.elements)):
        if snake.elements[0] == snake.elements[i]:
            running = False

    # 刷新屏幕
    pygame.display.flip()

    # 设置游戏帧率
    pygame.time.Clock().tick(10)

# 退出游戏
pygame.quit()
