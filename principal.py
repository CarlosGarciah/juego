# Módulos
import sys, pygame
from pygame.locals import *

# Constantes
WIDTH = 840
HEIGHT = 580


# Clases
# ---------------------------------------------------------------------
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("nave.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 8
        self.rect.centery = HEIGHT / 1.5
        self.velocidad = 5

    def mover(self, keys):
        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= self.velocidad
        if keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.centerx += self.velocidad
        if keys[K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.centery += self.velocidad
        if keys[K_UP] and self.rect.top > 0:
            self.rect.centery -= self.velocidad

    def posicion_disparo(self):
        return self.rect.midright


class Alien(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("enemigo.png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / x
        self.rect.centery = HEIGHT / y

    def mover(self, nave1):
        if self.rect.top >= 0:
            self.rect.centerx -= 1
            if self.rect.bottom <= WIDTH:
                self.rect.centerx += 15
                if self.rect.bottom <= WIDTH:
                    self.rect.centerx -= 15
                if pygame.sprite.collide_rect(self, nave1):
                    nave1.rect.centerx = 1000
                    nave1.rect.centery = 1000


class Disparo(pygame.sprite.Sprite):
    def __init__(self, posicion):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("disparo.png", True)
        self.rect = self.image.get_rect()
        self.rect.midleft = posicion
        self.velocidad = 10

    def update(self):
        self.rect.centerx += self.velocidad
        if self.rect.left > WIDTH:
            self.kill()


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
    nave1 = Nave()
    aliens = pygame.sprite.Group(
        Alien(1.2, 1.4),
        Alien(0.4, 1.9),
        Alien(0.2, 1.5),
        Alien(0.1, 1.5)
    )
    disparos = pygame.sprite.Group()
    pygame.mixer.music.load("sonido.mp3")
    pygame.mixer.music.play(2)

    while True:

        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)
            if eventos.type == KEYDOWN and eventos.key == K_SPACE:
                disparos.add(Disparo(nave1.posicion_disparo()))

        screen.blit(background_image, (0, 0))
        for alien in list(aliens):
            alien.mover(nave1)
            screen.blit(alien.image, alien.rect)
        nave1.mover(keys)

        disparos.update()
        pygame.sprite.groupcollide(disparos, aliens, True, True)
        for disparo in disparos:
            screen.blit(disparo.image, disparo.rect)

        screen.blit(nave1.image, nave1.rect)
        pygame.display.flip()
    return 0


if __name__ == '__main__':
    pygame.init()
    main()
