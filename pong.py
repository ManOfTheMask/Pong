import pygame

pygame.init()

# global variables
WIDTH = 640
HEIGHT = 480

window = pygame.display.set_mode((WIDTH, HEIGHT))
IsOpen = True
cir = [185, 135, 15, 15]
sqr1 = [75, 240, 10, 60]
sqr2 = [565, 240, 10, 60]

font = pygame.font.Font("ARCADECLASSIC.TTF", 100)

ScoreOne = "0"
ScoreTwo = "0"

FPS = 200

left = False
right = True
up = True
down = False
sqr1up = False
sqr1down = False
sqr2up = False
sqr2down = False
clock = pygame.time.Clock()

# checks for pressed keys or done anything to the window
def Events():
    global IsOpen, up, down, left, right, sqr1up, sqr1down, sqr2up, sqr2down

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IsOpen = False

        # control the paddles
        if event.type == pygame.QUIT:
            IsOpen = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                sqr1up = False
            if event.key == pygame.K_DOWN:
                sqr1down = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                sqr1up = True
            if event.key == pygame.K_DOWN:
                sqr1down = True

# affects the paddle on the left
def Updatesqr1():
    global sqr1up, sqr1down
    if sqr1up:
        sqr1[1] += 1
    if sqr1down:
        sqr1[1] -= 1
    if sqr1[1] > HEIGHT - 50:
        sqr1[1] = HEIGHT - 50
    if sqr1[1] < 0:
        sqr1[1] = 0

# affects the paddle on the right
def Updatesqr2():
    global sqr2up, sqr2down
    if sqr2up:
        sqr2[1] -= .8
    if sqr2down:
        sqr2[1] += .8
    if cir[1] < sqr2[1] + 10:
        sqr2up = True
        sqr2down = False
    else:
        sqr2up = False
        sqr2down = True

# effects the ball
def UpdateCircle():
    global up, down, left, right

    if right:
        cir[0] += 1
    elif left:
        cir[0] -= 1
    if up:
        cir[1] -= 1
    elif down:
        cir[1] += 1

    if cir[0] >= WIDTH - cir[2]:
        right = False
        left = True
    if cir[0] <= 0 + cir[2]:
        right = True
        left = False
    if cir[1] >= HEIGHT - cir[2]:
        up = True
        down = False
    if cir[1] <= 0 + cir[2]:
        up = False
        down = True

    if cir[0] + cir[3] > sqr2[0]:
        if sqr2[1] + sqr2[3] >= cir[1] > sqr2[1]:
            right = False
            left = True

            if sqr2down == True:
                up = False
                right = False
                left = True
                down = True

            if sqr2up == True:
                up = True
                right = False
                left = True
                down = False

    if cir[0] - cir[3] - sqr1[2] < sqr1[0]:
        if sqr1[1] + sqr1[3] >= cir[1] > sqr1[1]:
            right = True
            left = False

            if sqr1down == True:
                up = False
                right = True
                left = False
                down = True

            if sqr1up == True:
                up = True
                right = True
                left = False
                down = False

# Resets the ball after scoring
def scoring():
    global left, right, down, up, ScoreOne, ScoreTwo
    if cir[0] <= 65:
        cir[0] = WIDTH // 2
        cir[1] = HEIGHT // 2
        right = False
        left = True
        up = False
        down = False
        ScoreOne = int(ScoreOne)
        ScoreOne += 1
        ScoreOne = str(ScoreOne)

    if cir[0] >= WIDTH - 65:
        cir[0] = WIDTH // 2
        cir[1] = HEIGHT // 2
        right = True
        left = False
        up = False
        down = False
        ScoreTwo = int(ScoreTwo)
        ScoreTwo += 1
        ScoreTwo = str(ScoreTwo)

# to render stuff
def Render():
    window.fill((0, 0, 0))

    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(sqr1))
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(sqr2))
    pygame.draw.circle(window, (255, 255, 255), [cir[0], cir[1]], cir[3])
    window.blit(font.render(ScoreOne, False, (0, 0, 255)), (150, 10))
    window.blit(font.render(ScoreTwo, False, (0, 0, 255)), (350, 10))
    pygame.display.update()

# to keep stuff running
while IsOpen:
    clock.tick(FPS)
    Events()
    UpdateCircle()
    Render()
    Updatesqr1()
    Updatesqr2()
    scoring()

pygame.quit()
