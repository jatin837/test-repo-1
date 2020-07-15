import pygame
import time
pygame.init()
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
paddle_velocity = 3
initial_pos_of_paddle = 10
initial_x_pos_of_ball=60
initial_y_pos_of_ball=100

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

#pong_file = open('pong.csv', 'a')

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
    def update_position(self, vx, vy):
        self.vx = vx
        self.vy = vy
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

    def update_position(self, vy):
        self.vy = vy
        self.y += self.vy


paddle = Paddle(initial_pos_of_paddle, paddle_velocity)
#initial_pos_of_paddle = 30, paddle_velocity = 3
ball = Ball(initial_x_pos_of_ball, initial_y_pos_of_ball, ball_x_vel, ball_y_vel)
#initial_x_pos_of_ball = 100, initial_y_pos_of_ball = 200ll_x_vel = 3, ball_y_vel = 3
ball.draw()

paddle.draw()
pygame.display.update()
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

def game_loop():
    global crashed
    global ball_x_vel
    global ball_y_vel
    global ball
    global paddle
    global clock




    while not crashed :
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                crashed = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if paddle.y <=0 :
                paddle_velocity = 0
            else:
                paddle_velocity =-3
        elif keys[pygame.K_DOWN]:
            if paddle.y >= display_height-paddle.HEIGHT:
                paddle_velocity = 0
            else:
                paddle_velocity = 3
        else:
            paddle_velocity = 0
        c1 = (ball.cx >= display_width-ball.RADIUS-paddle.WIDTH)
        c2 = (ball.cy < paddle.y + paddle.HEIGHT and ball.cy > paddle.y)
        print(f"{c1}, {c2}")
        paddle.erase()
        paddle.update_position(paddle_velocity)
        paddle.draw()
        if c1 and c2:
            ball_x_vel = -3
            #if ball.vy*paddle.vy < 0:
            #    ball_y_vel = -ball_y_vel
        if ball.cx > display_width-ball.RADIUS :#ball approaching extream right
            ball_x_vel = -3
        #else:
        #    ball_x_vel = 3

        if ball.cx < ball.RADIUS:#ball approaching extream left
            ball_x_vel = 3
        #else:
        #    ball_x_vel = -3
        if ball.cy > display_height-ball.RADIUS:#ball approaching extream down
            ball_y_vel = -3
        #else:
        #    ball_y_vel = 3
        if ball.cy < ball.RADIUS:#ball approaching extream up
            ball_y_vel = 3
        #else:
        #    ball_y_vel = -3

            #ball.erase()
        ball.erase()
        ball.update_position(ball_x_vel, ball_y_vel)
        ball.draw()



        pygame.display.update()
        #print(f"{ball.cx}, {ball.cy}, {ball.vx}, {ball.vy}, {paddle.y}, {paddle.vy}", file = pong_file)
        #if ball.cx == display_width - ball.RADIUS:
        #    crash('You Crashed')

game_loop()
print('well played')
pygame.quit()
