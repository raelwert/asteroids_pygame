import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dtForFrame):
        self.rotation += PLAYER_TURN_SPEED * dtForFrame

    def update(self, dtForFrame):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dtForFrame)
        if keys[pygame.K_d]:
            self.rotate(dtForFrame)
        if keys[pygame.K_w]:
            self.move(dtForFrame)
        if keys[pygame.K_s]:
            self.move(-dtForFrame)

    def move(self, dtForFrame):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dtForFrame