import pygame
import random

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, image):
    super(GameObject, self).__init__()
    self.surf = pygame.image.load(image)
    self.x = x
    self.y = y
    self.speed = 1

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))

class Ghost(GameObject):
  def __init__(self):
    self.imgIndex = 0
    self.images = ['ghost/frame_0.gif','ghost/frame_1.gif','ghost/frame_2.gif','ghost/frame_3.gif']
    super(Ghost, self).__init__(0, 0, self.images[self.imgIndex])
    self.dx = 0
    self.dy = (random.randint(0, 200) / 100) + 1
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def update(self):
    if self.imgIndex < len(self.images)-1:
      self.imgIndex += 1
    else:
      self.imgIndex = 0
    self.surf = pygame.image.load(self.images[self.imgIndex])

  def move(self):
    self.x += self.dx
    self.y -= self.dy
    if self.y < 0: 
      self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def reset(self):
    self.x = random.randint(50, 400)
    self.y = random.randint(50, 400)
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

class Ghost2(GameObject):
  def __init__(self):
    self.imgIndex = 0
    self.images = ['ghost/frame_0.gif','ghost/frame_1.gif','ghost/frame_2.gif','ghost/frame_3.gif']
    super(Ghost2, self).__init__(0, 0, self.images[self.imgIndex])
    self.dx = 0
    self.dy = (random.randint(0, 200) / 100) + 1
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def update(self):
    if self.imgIndex < len(self.images)-1:
      self.imgIndex += 1
    else:
      self.imgIndex = 0
    self.surf = pygame.image.load(self.images[self.imgIndex])

  def move(self):
    self.x += self.dx
    self.y -= self.dy
    if self.y < 0: 
      self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def reset(self):
    self.x = random.randint(50, 400)
    self.y = random.randint(50, 400)
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

class Apple1(GameObject):
  def __init__(self):
    self.imgIndex = 0
    self.images = ['apple.png']
    super(Apple1, self).__init__(0, 0, self.images[self.imgIndex])
    self.dx = (random.randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def update(self):
    if self.imgIndex < len(self.images)-1:
      self.imgIndex += 1
    else:
      self.imgIndex = 0
    self.surf = pygame.image.load(self.images[self.imgIndex])

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500: 
      self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def reset(self):
    self.dx = ((random.randint(0, 200) / 100) + 1) * self.speed
    self.x = -64
    self.y = random.randint(50, 400)

class Apple2(GameObject):
  def __init__(self):
    self.imgIndex = 0
    self.images = ['apple.png']
    super(Apple2, self).__init__(0, 0, self.images[self.imgIndex])
    self.dx = 0
    self.dy = (random.randint(0, 200) / 100) + 1
    self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def update(self):
      if self.imgIndex < len(self.images)-1:
        self.imgIndex += 1
      else:
        self.imgIndex = 0
      self.surf = pygame.image.load(self.images[self.imgIndex])

  def move(self):
    self.x += self.dx
    self.y -= self.dy
    if self.y < 0: 
      self.reset()
    self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

  def reset(self):
    self.dy = ((random.randint(0, 200) / 100) + 1) * self.speed
    self.x = random.randint(50, 400)
    self.y = 550

class Player(GameObject):
    def __init__(self):
      self.imgIndex = 0
      self.images = ['Pacman/pac0.gif','Pacman/pac1.gif']
      super(Player, self).__init__(0,0, self.images[self.imgIndex])
      self.dx = 30
      self.dy = 30
      self.x = 250
      self.y = 250
      self.reset()
      self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

    def update(self):
      if self.imgIndex < len(self.images)-1:
        self.imgIndex += 1
      else:
        self.imgIndex = 0
      self.surf = pygame.image.load(self.images[self.imgIndex])

    def left(self):
        self.x -= self.dx
        self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))
    
    def right(self):
        self.x += self.dx
        self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

    def up(self):
        self.y -= self.dy
        self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

    def down(self):
        self.y += self.dy
        self.rect = pygame.Rect((self.x, self.y), (self.surf.get_width(), self.surf.get_height()))

    def reset(self):
        self.x = 250 - 32
        self.y = 250 - 32