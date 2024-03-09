import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


class Bird:
    def __init__(self, godown=False, goright=False):
        self.velocity = random.choice([0.89, 0.65, 1.1, 1.3, 0.84])
        self.birdPos = pygame.Vector2(random.randint(0, 200), random.randint(0, 200))
        self.godown = godown
        self.goright = goright

    def fly(self):
        self.velocity = random.choice([0.89, 0.65, 1.1, 1.3, 0.84])
        if self.godown:
            self.birdPos.y += 3*self.velocity
        else:
            self.birdPos.y -= 3*self.velocity
        if self.goright:
            self.birdPos.x += 3*self.velocity
        else:
            self.birdPos.x -= 3*self.velocity
        pygame.draw.circle(screen, "black", self.birdPos, 5)

    def direction(self):
        if self.birdPos.y > 700:
            self.godown = False
        if self.birdPos.y < 20:
            self.godown = True

        if self.birdPos.x > 1200:
            self.goright = False
        if self.birdPos.x < 20:
            self.goright = True


birds = [Bird() for i in range(20)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    for bird in birds:
        bird.direction()
        bird.fly()
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()



