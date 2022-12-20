import pygame
import random

WIDTH = 1600
HEIGHT = 800
FPS = 60
G = 0.2
PIPE_WIDTH = 60
MIN_PIPE_HEIGHT = 20
pipe_speed = 6


# функции генерации препятствий
def generate_void():
    void_width = PIPE_WIDTH
    void_height = 100
    void_x = WIDTH
    void_y = random.randint(MIN_PIPE_HEIGHT, HEIGHT - void_height - MIN_PIPE_HEIGHT)
    return pygame.Rect(void_x, void_y, void_width, void_height)


def make_pipe(void):
    top_pipe = pygame.Rect(void.x, 0, void.width, void.y)
    bottom_pipe = pygame.Rect(void.x, void.bottom, void.width, HEIGHT - void.bottom)
    return [top_pipe, bottom_pipe]


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bird1 = pygame.image.load("fpbs1.png")
bird2 = pygame.image.load("fpbs2.png")
bird3 = pygame.image.load("fpbs3.png")
pipes = pygame.image.load("obstacles.png")

bird = [bird1, bird2, bird3, bird2]
animation_speed = 10
current_bird = 0

player = bird1.get_rect(x=50, y=50)
player_speed = 0
voids =[generate_void()]
pipes = make_pipe(voids[0])


void = generate_void()
pipes = make_pipe(generate_void())
# основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            if event.type == pygame.K_ESCAPE:
                if event.key == pygame.K_ESCAPE:
                    running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_speed = -8


    current_bird = (current_bird + 1) % (len(bird) * animation_speed)

    screen.fill((205, 255, 255))
    player_speed += G

    player.y += int(player_speed)
    for pipe in pipes[:]:
        pipe.x -= pipe_speed
        pygame.draw.rect(screen, (0, 255, 0), pipe)
        if pipe.colliderect(player):
            running = False
        if pipe.right < 0:
            pipes.remove(pipe)
    if pipes[-1].x < WIDTH // 6 * 4:
        voids.append(generate_void())
        pipes += make_pipe(voids[-1])


    screen.blit(bird[current_bird // animation_speed], player)


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
