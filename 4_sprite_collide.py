import pygame, random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Sprite Group')

FPS = 60
clock = pygame.time.Clock()


#define classes


class Player(pygame.sprite.Sprite):
    """Simple class for a player that fights monsters"""
    def __init__(self, x, y, monster_group):
        super().__init__()
        self.image = pygame.image.load('knight.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

        self.velocity = 5

        self.monster_group = monster_group

    def update(self):
        self.move()
        self.check_collisions()
    
    def move(self):
        """Move the player continously"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
          self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
           self.rect.x += self.velocity
        if keys[pygame.K_UP]:
           self.rect.y -= self.velocity
        if keys[pygame.K_DOWN]:
           self.rect.y += self.velocity

    def check_collisions(self):
       """check for collisions between player and monsters"""
       if pygame.sprite.spritecollide(self, monster_group, True):
          print(len(monster_group))

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

#create a player group and add a player
#Why a group of 1? Can't draw Sprites to screen, only groups      
player_group = pygame.sprite.Group()
player = Player(500,500, monster_group)
player_group.add(player)


running = True
while running:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #fill the display
  display_surface.fill((0,0,0))

  #draw assets
  player_group.update()
  player_group.draw(display_surface)
  monster_group.update()
  monster_group.draw(display_surface)
  

  pygame.display.update()
  clock.tick(FPS)

pygame.quit()
