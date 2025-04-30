# are image the render in the screen
import pygame

sprites = []
loaded = {}

class Sprites:
    def __init__(self, image, x , y):
        self.x = x
        self.y = y

        if image in loaded:
            self.image = loaded[image]

        else:
            self.image = pygame.image.load(image)
            loaded[image] = self.image

        sprites.append(self)
    def delete(self):
        sprites.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

