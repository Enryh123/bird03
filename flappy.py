import pygame
pygame.init()

width = 288
height = 512

clock = pygame.time.Clock()

FLY = 20001
pygame.time.set_timer(FLY, 200)

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('flappy bird')

bird = [
pygame.image.load('images/bluebird-upflap.png'),
pygame.image.load('images/bluebird-midflap.png'),
pygame.image.load('images/bluebird-downflap.png')
]

index = 0
bird_rect = bird[index].get_rect()
bird_rect.center = (width / 2, height / 2)

bg_image = pygame.image.load('images/background-day.png')

floor_image = pygame.image.load('images/base.png')
floor_rect = floor_image.get_rect()

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            exit()

        if event.type == FLY:
            index = index + 1
            index = index % 3

    window.blit(bg_image, (0, 0))

    window.blit(bird[index], bird_rect)

    floor_rect.y = height*0.8
    floor_rect.x -= 1
    floor_rect.x %= -48
    window.blit(floor_image, floor_rect)

    pygame.display.update()
    clock.tick(30)