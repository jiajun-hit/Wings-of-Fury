import pygame
from random import *

class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
                    pygame.image.load("images/enemy1_down1.png").convert_alpha(), \
                    pygame.image.load("images/enemy1_down2.png").convert_alpha(), \
                    pygame.image.load("images/enemy1_down3.png").convert_alpha(), \
                    pygame.image.load("images/enemy1_down4.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                    randint(0, self.width - self.rect.width), \
                    randint(-5 * self.height, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
        self.down_sound.set_volume(0.1)
        self.destroy_index = 0
        self.speed = 2
        self.active = True

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
                    randint(0, self.width - self.rect.width), \
                    randint(-5 * self.height, 0)

class MidEnemy(pygame.sprite.Sprite):
    energy = 8
    
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy2_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
                    pygame.image.load("images/enemy2_down1.png").convert_alpha(), \
                    pygame.image.load("images/enemy2_down2.png").convert_alpha(), \
                    pygame.image.load("images/enemy2_down3.png").convert_alpha(), \
                    pygame.image.load("images/enemy2_down4.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                    randint(0, self.width - self.rect.width), \
                    randint(-10 * self.height, -self.height)
        self.mask = pygame.mask.from_surface(self.image)
        self.down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
        self.down_sound.set_volume(0.2)
        self.destroy_index = 0
        self.speed = 1
        self.active = True
        self.energy = MidEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def draw_plane(self, screen):
        if self.hit == True:
            screen.blit(self.image_hit, self.rect)
            self.hit = False
        else:
            screen.blit(self.image, self.rect)

    def reset(self):
        self.active = True
        self.energy = MidEnemy.energy
        self.rect.left, self.rect.top = \
                    randint(0, self.width - self.rect.width), \
                    randint(-10 * self.height, -self.height)
        
class LargeEnemy(pygame.sprite.Sprite):
    energy = 20

    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        self.image_hit = pygame.image.load("images/enemy3_hit.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
                    pygame.image.load("images/enemy3_down1.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down2.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down3.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down4.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down5.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down6.png").convert_alpha()])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 1
        self.active = True
        self.rect.left, self.rect.top = \
                    randint(0, self.width - self.rect.width), \
                    randint(-15 * self.height, -5 * self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.energy = LargeEnemy.energy
        self.destroy_images = []
        self.destroy_images.extend([\
                    pygame.image.load("images/enemy3_down1.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down2.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down3.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down4.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down5.png").convert_alpha(), \
                    pygame.image.load("images/enemy3_down6.png").convert_alpha()])
        self.rect = self.image1.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.rect.left, self.rect.top = \
                    randint(0, self.width - self.rect.width), \
                    randint(-15 * self.height, -5 * self.height)
        self.mask = pygame.mask.from_surface(self.image1)
        self.fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
        self.fly_sound.set_volume(0.2)
        self.down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
        self.down_sound.set_volume(0.5)
        self.destroy_index = 0
        self.speed = 1
        self.active = True
        self.energy = LargeEnemy.energy
        self.hit = False

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def draw_plane(self, switch_image, screen):
        if self.hit == True:
            screen.blit(self.image_hit, self.rect)
            self.hit = False
        else:
            if switch_image:
                screen.blit(self.image1, self.rect)
            else:
                screen.blit(self.image2, self.rect)

    def reset(self):
        self.active = True
        self.energy = LargeEnemy.energy
        self.rect.left, self.rect.top = \
                    randint(0, self.width - self.rect.width), \
                    randint(-15 * self.height, -5 * self.height)
        self.fly_sound.stop()
