import random
from dino_runner.components.obstacle.obstacle import Obstacle

class Bird(Obstacle):
    def __init__(self, image):
        ranHeight = random.randint(0, 1)
        self.type = 0
        self.image = image
        super().__init__(self.image, self.type)
        self.step_index = 0
        self.rect.y = 250
        self.rect.y = 250 if ranHeight == 1 else 200
        
    def draw(self, screen):
        if self.step_index >= 10:
            self.step_index = 0

        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1