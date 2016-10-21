
# Módulos
import sys, pygame
from pygame.locals import *

# Constantes
WIDTH = 840
HEIGHT = 580

imagenDisparo = pygame.image.load("disparo.png")
rectanguloDisparo = imagenDisparo.get_rect()
disparoActivo = False


# Clases
# ---------------------------------------------------------------------
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("nave.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 8
        self.rect.centery = HEIGHT / 1.5

    def mover(self,keys):
        if self.rect.top >= 0:
            if keys[K_LEFT]:
                self.rect.centerx -= 1
            if self.rect.bottom <= WIDTH:
                if keys[K_RIGHT]:
                    self.rect.centerx += 1
                if keys[K_DOWN]:
                    self.rect.centery += 1
                if self.rect.bottom <= HEIGHT:
                    if keys[K_UP]:
                        self.rect.centery -= 1



class Alien(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("enemigo.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / x
        self.rect.centery = HEIGHT / y

    def mover(self,nave1):
        if self.rect.top >= 0:
            self.rect.centerx -= 1
            if self.rect.bottom <= WIDTH:
                self.rect.centerx += 15
                if self.rect.bottom <= WIDTH:
                    self.rect.centerx -= 15
                if pygame.sprite.collide_rect(self, nave1):
                    nave1.rect.centerx = 1000
                    nave1.rect.centery = 1000


# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
    image = pygame.image.load(filename)
    image = image.convert()
    if transparent:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image


# ---------------------------------------------------------------------

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pruebas Pygame")

    background_image = load_image('fondo.jpg')
    nave1=Nave()
    alien1=Alien(1.2,1.4)
    alien2=Alien(0.2,1.9)
    alien3=Alien(0.1,1.5)

    while True:
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        screen.blit(background_image, (0, 0))
        screen.blit(alien1.image, alien1.rect)
        screen.blit(alien2.image, alien2.rect)
        screen.blit(alien3.image, alien3.rect)
        alien1.mover(nave1)
        alien2.mover(nave1)
        alien3.mover(nave1)
        nave1.mover(keys)
        screen.blit(nave1.image, nave1.rect)
        pygame.display.flip()
    return 0


if __name__ == '__main__':
    pygame.init()
    main()