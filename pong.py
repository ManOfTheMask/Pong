#todo add collison to pattles, add collison for scoring, and add controls for the second pattle
import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480

window = pygame.display.set_mode((WIDTH, HEIGHT))
IsOpen = True
cir = [185, 135, 15, 15]
sqr1 = [75, 240, 10, 50]
sqr2 = [565, 240, 10, 50]

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

# where you control the ball
def Updatesqr1():
    global sqr1up, sqr1down
    if sqr1up:
        sqr1[1] += 1
    if sqr1down:
        sqr1[1] -= 1

def Updatesqr2(): #remember to call this function later
    global sqr2up, sqr2down
    if sqr2up:
        sqr2[1] += 1
    if sqr1down:
        sqr2[1] -= 1

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

    """if cir[0] == sqr2[0]: # this condition doesn't work right
        right = False
        left = True
        """
# to render stuff
def Render():
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(sqr1))
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(sqr2))
    pygame.draw.circle(window, (255, 255, 255), [cir[0], cir[1]], cir[3])
    pygame.display.update()

# to keep stuff running
while IsOpen:
    clock.tick(FPS)
    Events()
    UpdateCircle()
    Render()
    Updatesqr1()
    #remember to call UpdateSqr2

pygame.quit()