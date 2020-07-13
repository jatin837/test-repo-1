import pygame
import time
pygame.init()
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
paddle_velocity = 3
initial_pos_of_paddle = 30
initial_x_pos_of_ball=100
initial_y_pos_of_ball=20

ball_x_vel = 3
ball_y_vel = 3
color = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        "blue": (0, 0, 255),
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        }
clock = pygame.time.Clock()
crashed = False

class Ball():
    def __init__(self, cx, cy, vx, vy):
        self.RADIUS = 10
        self.cx = cx
        self.cy = cy
        self.vx = vx
        self.vy = vy
    def draw(self):
        global game_display
        global color
        pygame.draw.circle(game_display,color['green'], (self.cx, self.cy), self.RADIUS)
    def erase(self):
        global game_display
        global color
        pygame.draw.circle(game_display, color['black'], (self.cx, self.cy), self.RADIUS)
    def update_position(self):
        self.cx += self.vx
        self.cy += self.vy

class Paddle():
    def __init__(self, y, vy):
        self.WIDTH = 15
        self.HEIGHT = 60
        self.y = y
        self.vy = vy

    def draw(self):
        global color
        global game_display
        pygame.draw.rect(game_display, color['white'], (display_width-self.WIDTH, self.y, self.WIDTH, self.HEIGHT))

    def erase(self):
        global color
        global game_display
        pygame.draw.rect(game_display, color['black'], (display_width-self.WIDTH, self.y, self.WIDTH, self.HEIGHT))

    def update_position(self):
        self.y += self.vy


paddle = Paddle(initial_pos_of_paddle, paddle_velocity)
#initial_pos_of_paddle = 30, paddle_velocity = 3
ball = Ball(initial_x_pos_of_ball, initial_y_pos_of_ball, ball_x_vel, ball_y_vel)
#initial_x_pos_of_ball = 100, initial_y_pos_of_ball = 200ll_x_vel = 3, ball_y_vel = 3
ball.draw()

paddle.draw()

def text_objects(text, font, colour):
    global color
    textSurface = font.render(text, True, color[colour])#render is a method of font object
    return textSurface, textSurface.get_rect()

def crash(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)#what is this Font object has
    TextSurf, TextRect = text_objects(text, largeText, 'red')
    TextRect.center = ((display_width/2),(display_height/2))
    game_display.blit(TextSurf, TextRect)
    pygame.display.update()
    global clock
    clock.sleep(5)
    global crashed
    crashed = True

def doesCollid(ball, paddle):

    global display_width
    condition1 = (ball.cx == display_width-ball.RADIUS-paddle.WIDTH)
    condition2 = False
    for y in range(paddle.y-ball.RADIUS, paddle.y+paddle.HEIGHT+ball.RADIUS):
        if ball.cy == y:
            condition2 = True
            return (condition1 and condition2)
    return condition1 and condition2
def game_loop():
    global crashed

    while not crashed :

        clock.tick(60)
        keys = pygame.key.get_pressed()
        ball.erase()
        ball.update_position()
        ball.draw()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                crashed = True
        if doesCollid(ball, paddle):
            ball.vx = -ball.vx
            if ball.vy*paddle.vy < 0:
                ball.vy = -ball.vy
        if ball.cx > display_width-ball.RADIUS:#ball approaching extream right
            ball.vx = -ball.vx

        if ball.cx < ball.RADIUS:#ball approaching extream left
            ball.vx = -ball.vx
        if ball.cy > display_height-ball.RADIUS:#ball approaching extream down
            ball.vy = -ball.vy
        if ball.cy < ball.RADIUS:#ball approaching extream up
            ball.vy = -ball.vy


        if keys[pygame.K_UP]:
            if paddle.y <=0:
                paddle.y = 0
            else:
                paddle.vy =-paddle_velocity
                paddle.erase()
                paddle.update_position()
                paddle.draw()
        if keys[pygame.K_DOWN]:
            if paddle.y >= display_height-paddle.HEIGHT:
                paddle.y = display_height-paddle.HEIGHT
            else:
                paddle.vy = paddle_velocity
                paddle.erase()
                paddle.update_position()
                paddle.draw()
        if ball.cx == display_width - ball.RADIUS:
            crash('You Crashed')

game_loop()
print('well played')
pygame.quit()
