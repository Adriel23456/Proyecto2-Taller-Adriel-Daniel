import pygame
import pygame_textinput
import random
import os

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Configuración de la ventana
W, H = 600, 800
ventana = pygame.display.set_mode((W, H))
pygame.display.set_caption("STAR LIGHT RUNNER")

#Rutas para los archivos
carpeta_juego = os.path.dirname(__file__)
carpeta_assets = os.path.join(carpeta_juego, "Assets")
carpeta_botones = os.path.join(carpeta_assets, "Botones")
carpeta_fondos = os.path.join(carpeta_assets, "Fondos")
carpeta_musica = os.path.join(carpeta_assets, "Musica")
carpeta_personajes = os.path.join(carpeta_assets, "Personajes")
carpeta_sonidos = os.path.join(carpeta_assets, "Sonidos")
carpeta_font = os.path.join(carpeta_assets, "Font")

# Definir imágenes
background = pygame.image.load(os.path.join(carpeta_fondos, 'Background.png'))


# Definir sonidos
PLAYING_GAMEPLAY_MUSIC = pygame.mixer.Sound(os.path.join(carpeta_musica, 'Pantalla-de-Juego.mp3'))

class jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_personajes,'Jugador.png')), (70, 70))
        self.rect = self.image.get_rect()
        self.rect.centerx = 300
        self.rect.bottom = 700
        self.vida = 3
    
    def update(self):
        # Velocidad de movimiento
        self.jugadorX_vel = 0
        self.jugadorY_vel = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.jugadorX_vel = -3
        if keystate[pygame.K_RIGHT]:
            self.jugadorX_vel = 3
        if keystate[pygame.K_DOWN]:
            self.jugadorY_vel = 3
        if keystate[pygame.K_UP]:
            self.jugadorY_vel = -3
        self.rect.x += self.jugadorX_vel
        self.rect.y += self.jugadorY_vel
        # Limites de movimiento en la ventana
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 530:
            self.rect.x = 530
        if self.rect.y <= 104:
            self.rect.y = 104
        elif self.rect.y >= 730:
            self.rect.y = 730
            

running = True

jugador = jugador()
all_sprites = pygame.sprite.Group(jugador)

PLAYING_GAMEPLAY_MUSIC.play(-1)
PLAYING_GAMEPLAY_MUSIC.set_volume(0.2)

y = 0

while running:
    for event in pygame.event.get():
                # Cerrar ventana
                if event.type == pygame.QUIT:
                    running = False
    all_sprites.update()

    y_relativa =  y % background.get_rect().width
    ventana.blit(background,(0,y_relativa - background.get_rect().width))
    if (y_relativa < H):
        ventana.blit(background,(0,y_relativa))
    y = y + 1

    all_sprites.draw(ventana)
    pygame.display.update()