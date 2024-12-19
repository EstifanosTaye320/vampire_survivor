from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join('images','player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center=pos)
        
        # movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 400

    def input(self):
        keys = pygame.key.get_pressed()

        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

        self.direction = self.direction.normalize() if self.direction else self.direction

    def move(self):
        self.rect.center += self.direction*self.speed*dt

    def update(self, dt, *args, **kwargs):
        self.input()
        self.move(dt)

        return super().update(*args, **kwargs)