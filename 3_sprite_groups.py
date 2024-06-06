import pygame, random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Sprite Group')

FPS = 60
clock = pygame.time.Clock()


#define classes
class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('monster.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 10)

    def update(self):
        """update and move monster"""
        self.rect.y += self.velocity


#create a monster group and add 10 monsters
monster_group = pygame.sprite.Group()
for i in range(10):
  monster = Monster(i * 64, 10)
  monster_group.add(monster)

running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #fill the display
  display_surface.fill((0,0,0))

  #draw assets
  monster_group.update()
  monster_group.draw(display_surface)
  

  pygame.display.update()
  clock.tick(FPS)

pygame.quit()
