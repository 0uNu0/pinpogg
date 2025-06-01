import pygame

pygame.init()
class Area:
    def __init__(self, x, y, w, h, fill_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.fill_color = fill_color
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Sprite(Area):
    def __init__(self, x, y, w, h, ing_name):
        super().__init__( x, y, w, h, None)
        self.image = pygame.image.load(ing_name)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = Sprite(250, 250, 50, 50, 'ball.png')
platform = Sprite(300, 420, 99, 25, 'platform.png')
platform2 = Sprite(300, 120, 99, 25, 'platform.png')
pygame.init()
window = pygame.display.set_mode((500,500))
game = True
move_left = False
move_right = False
speed_x = 2
speed_y = 2
clock = pygame.time.Clock()
while game :
    ball.rect.x += speed_x
    ball.rect.y += speed_y
    window.fill((193, 247, 199))
    ball.draw()
    platform.draw()
    platform2.draw()
    # Ограничение движения

    if platform.rect.x < 0:
        platform.rect.x = 0
    if platform.rect.x > 400:
        platform.rect.x = 400
    
    if platform2.rect.x < 0:
        platform2.rect.x = 0
    if platform2.rect.x > 400:
        platform2.rect.x = 400
  




# ОТСКОКИ
    if platform.colliderect(ball.rect):
        speed_y = -abs(speed_y)
    if platform2.colliderect(ball.rect):
        speed_y = -abs(speed_y)
    if ball.rect.x >= 450:
        speed_x *= -1

    if ball.rect.x <= 0:
        speed_x *= -1
       
    # ОБРАБОТКА КЛАВИШ
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_a:
                move_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_a:
                move_left = False
    if move_right:
        platform.rect.x += 3
    if move_left:
        platform.rect.x -= 3
    for event in pygame.event.get():    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
    if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    if move_right:
        platform2.rect.x += 3
    if move_left:
        platform2.rect.x -= 3
    pygame.display.update()
    clock.tick(40)

