import pygame, random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Group Collide')

FPS = 60
clock = pygame.time.Clock()


class Game(pygame.sprite.Sprite):
    """A class to help manage our game"""
    def __init__(self, monster_group, knight_group):
       self.monster_group = monster_group
       self.knight_group = knight_group

    def update(self):
       self.check_collisions()

    def check_collisions(self):
       pygame.sprite.groupcollide(self.monster_group, self.knight_group, True, False)
          




class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('monster.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        """update and move monster"""
        self.rect.y += self.velocity

class Knight(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('knight.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.velocity = random.randint(1, 5)

    def update(self):
        """update and move monster"""
        self.rect.y -= self.velocity


#create a monster group and add 10 monsters
monster_group = pygame.sprite.Group()
for i in range(12):
  monster = Monster(i * 64, 10)
  monster_group.add(monster)

#create a knight group
knight_group = pygame.sprite.Group()
for i in range(12):
    knight = Knight(i*64, WINDOW_HEIGHT-64)
    knight_group.add(knight)

#create a game object
my_game = Game(monster_group, knight_group)



running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #fill the display
  display_surface.fill((0,0,0))

  #update and draw sprite groups
  knight_group.update()
  knight_group.draw(display_surface)
  monster_group.update()
  monster_group.draw(display_surface)

  my_game.update()
  

  pygame.display.update()
  clock.tick(FPS)

pygame.quit()
