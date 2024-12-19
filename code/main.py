from settings import *
from Player import *
from sprites import *

from random import randint

class Game:
    def __init__(self):
        # setup
        pygame.init()
        pygame.display.set_caption('Vampire Survivor')
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all_sprites = pygame.sprite.Group()

        # sprites
        self.player = Player((WINDOW_WIDTH/2, WINDOW_HEIGHT/2) ,self.all_sprites)
        for i in range(6):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(60, 100), randint(60, 100)
            CollisionSprite((x, y), (w, h), self.all_sprites)

    def run(self):
        while self.running:
            dt = self.clock.tick()/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.display_surface.fill((0,0,0))
            self.all_sprites.update(dt)
            
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()

        pygame.quit()
        exit()

if __name__ == '__main__':
    game = Game()
    game.run()
