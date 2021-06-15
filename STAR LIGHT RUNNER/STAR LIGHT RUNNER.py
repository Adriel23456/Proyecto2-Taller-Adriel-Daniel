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

button_img1 = pygame.image.load(os.path.join(carpeta_botones, 'Boton1.png'))
button_img1 = pygame.transform.scale(button_img1, (600, 113))

button_img2 = pygame.image.load(os.path.join(carpeta_botones, 'Boton2.png'))
button_img2 = pygame.transform.scale(button_img2, (192, 69))

button_img3 = pygame.image.load(os.path.join(carpeta_botones, 'Boton3.png'))
button_img3 = pygame.transform.scale(button_img3, (192, 69))

button_img4 = pygame.image.load(os.path.join(carpeta_botones, 'Boton4.png'))
button_img4 = pygame.transform.scale(button_img4, (108, 69))

button_img5 = pygame.image.load(os.path.join(carpeta_botones, 'Boton5.png'))
button_img5 = pygame.transform.scale(button_img5, (108, 69))

button_img6 = pygame.image.load(os.path.join(carpeta_botones, 'Boton6.png'))
button_img6 = pygame.transform.scale(button_img6, (108, 69))

button_img7 = pygame.image.load(os.path.join(carpeta_botones, 'Boton7.png'))
button_img7 = pygame.transform.scale(button_img7, (108, 69))


# Definir sonidos
PLAYING_GAMEPLAY_MUSIC = pygame.mixer.Sound(os.path.join(carpeta_musica, 'Pantalla-de-Juego.mp3'))
PLAYING_GAMEPLAY_MUSIC2 = pygame.mixer.Sound(os.path.join(carpeta_musica, 'Pantalla-de-Juego2.mp3'))
PLAYING_GAMEPLAY_MUSIC3 = pygame.mixer.Sound(os.path.join(carpeta_musica, 'Pantalla-de-Juego3.mp3'))
MENU_MUSIC = pygame.mixer.Sound(os.path.join(carpeta_musica, 'Menu-Principal.mp3'))
CREDITS_MUSIC = pygame.mixer.Sound(os.path.join(carpeta_musica, 'Creditos.mp3'))
SCORES_MUSIC = pygame.mixer.Sound(os.path.join(carpeta_musica, 'Puntuacion.mp3'))
HIT_SOUND = pygame.mixer.Sound(os.path.join(carpeta_sonidos, 'Hit.wav'))
EXPLOSION1_SOUND = pygame.mixer.Sound(os.path.join(carpeta_sonidos, 'Explosion1.wav'))
EXPLOSION2_SOUND = pygame.mixer.Sound(os.path.join(carpeta_sonidos, 'Explosion2.wav'))
CLICK_SOUND = pygame.mixer.Sound(os.path.join(carpeta_sonidos, 'Click.wav'))

def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(os.path.join(carpeta_font, 'ARCADECLASSIC.TTF'), size)
    text_surface = font.render(text, True, (0,228,54))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def update_background():
    y_relativa =  pantallas.y % background.get_rect().width
    ventana.blit(background,(0,y_relativa - background.get_rect().width))
    if (y_relativa < H):
        ventana.blit(background,(0,y_relativa))
    pantallas.y = pantallas.y + 14

def pantalla_de_juego():
    # Fondo
    update_background()
    # Banner
    ventana.blit(button_img1, (0, 0))
    # Iconos
    ventana.blit(pygame.transform.scale(pygame.image.load(os.path.join(carpeta_personajes,'Jugador.png')), (30, 30)), (470, 55))
    # Vida Jugador
    draw_text(ventana,"x{}".format(str(jugador.vida)), 25, 530, 58)
    # Nombre del Jugador
    draw_text(ventana, pantallas.nombre_jugador, 25, 512, 35)
    # Tiempo
    tiempo = (pygame.time.get_ticks()-pantallas.tiempo_inicial)//1000
    draw_text(ventana, "Tiempo", 25, 90, 35)
    draw_text(ventana, str(tiempo), 30, 90, 55)
    # Puntaje
    if pantallas.pantalla == "Pantalla_1":
        pantallas.score = tiempo
    elif pantallas.pantalla == "Pantalla_2":
        pantallas.score = tiempo*3
    elif pantallas.pantalla == "Pantalla_3":
        pantallas.score = tiempo*5
    draw_text(ventana, str(pantallas.score), 50, 300, 30)

def colisiones():
    colision = pygame.sprite.spritecollide(jugador, Enemigos, True)
    if colision:
        HIT_SOUND.play()
        HIT_SOUND.set_volume(0.1)
        jugador.vida -= 1
        #pantallas.score -= 1

#Aqui se define la aplicacion de quicksort
def quicksort(lista):
    if len(lista) == 0:
        return lista
    else:
        pivote = lista[len(lista)//2]
        listaMenor = []
        listaMedio = []
        listaMayor = []
        for x in lista:
            if x<pivote:
                listaMenor.append(x)
            elif x==pivote:
                listaMedio.append(x)
            else:
                listaMayor.append(x)
        return quicksort(listaMayor) + listaMedio + quicksort(listaMenor)

#Aqui se define la aplicacion de la funcion que va a acomodar las puntuaciones
def scores_quicksort(Points, player_name, lista):
    #Añadir a la lista ya existente los nuevos valores de nombre de jugador y sus puntos al final, remplazando los que antes estaban colocados
    lista[14] = "{}\n".format(player_name)
    lista[15] = "{}\n".format(Points)
    #Dejar esta lista intacta y luego crear una nueva lista pero que sea de solamente los valores numericos, antes representados:
    num1 = int(lista[1].rstrip("\n"))
    num2 = lista[3].rstrip("\n")
    num3 = lista[5].rstrip("\n")
    num4 = lista[7].rstrip("\n")
    num5 = lista[9].rstrip("\n")
    num6 = lista[11].rstrip("\n")
    num7 = lista[13].rstrip("\n")
    num8 = lista[15].rstrip("\n")
    Nueva_lista = [int(num1) , int(num2) , int(num3) , int(num4) , int(num5) , int(num6) , int(num7) , int(num8)]
    #Aplicar quicksort en esta nueva lista, y despues sacar esa nueva lista como quicksort_lista:
    quicksort_lista = quicksort(Nueva_lista)
    #Crear la lista final a mostrar con el orden correcto de los nombres y puntuaciones creados con el codigo de quicksort
    if quicksort_lista[0] != Nueva_lista[0]:
        Lista_Final = [lista[14]  ,  lista[15]  , lista[0] , lista[1] , lista[2] , lista[3] , lista[4] , lista[5] , lista[6] , lista[7] , lista[8] , lista[9] , lista[10] , lista[11] , lista[12] , lista[13] ]
    elif quicksort_lista[1] != Nueva_lista[1]:
        Lista_Final = [lista[0]  ,  lista[1]  , lista[14] , lista[15] , lista[2] , lista[3] , lista[4] , lista[5] , lista[6] , lista[7] , lista[8] , lista[9] , lista[10] , lista[11] , lista[12] , lista[13] ]
    elif quicksort_lista[2] != Nueva_lista[2]:
        Lista_Final = [lista[0]  ,  lista[1]  , lista[2] , lista[3] , lista[14] , lista[15] , lista[4] , lista[5] , lista[6] , lista[7] , lista[8] , lista[9] , lista[10] , lista[11] , lista[12] , lista[13] ]
    elif quicksort_lista[3] != Nueva_lista[3]:
        Lista_Final = [lista[0]  ,  lista[1]  , lista[2] , lista[3] , lista[4] , lista[5] , lista[14] , lista[15] , lista[6] , lista[7] , lista[8] , lista[9] , lista[10] , lista[11] , lista[12] , lista[13] ]
    elif quicksort_lista[4] != Nueva_lista[4]:
        Lista_Final = [lista[0]  ,  lista[1]  , lista[2] , lista[3] , lista[4] , lista[5] , lista[6] , lista[7] , lista[14] , lista[15] , lista[8] , lista[9] , lista[10] , lista[11] , lista[12] , lista[13] ]
    elif quicksort_lista[5] != Nueva_lista[5]:
        Lista_Final = [lista[0]  ,  lista[1]  , lista[2] , lista[3] , lista[4] , lista[5] , lista[6] , lista[7] , lista[8] , lista[9] , lista[14] , lista[15] , lista[10] , lista[11] , lista[12] , lista[13] ]
    elif quicksort_lista[6] != Nueva_lista[6]:
        Lista_Final = [lista[0]  ,  lista[1]  , lista[2] , lista[3] , lista[4] , lista[5] , lista[6] , lista[7] , lista[8] , lista[9] , lista[10] , lista[11] , lista[14] , lista[15] , lista[12] , lista[13] ]
    else:
        Lista_Final = lista
    return Lista_Final

def Cambio_Musica_Menu():
    PLAYING_GAMEPLAY_MUSIC.stop()
    PLAYING_GAMEPLAY_MUSIC2.stop()
    PLAYING_GAMEPLAY_MUSIC3.stop()
    MENU_MUSIC.stop()
    CREDITS_MUSIC.stop()
    SCORES_MUSIC.stop()
    MENU_MUSIC.play(-1)
    MENU_MUSIC.set_volume(0.2)

def Cambio_Musica_Level1():
    PLAYING_GAMEPLAY_MUSIC.stop()
    PLAYING_GAMEPLAY_MUSIC2.stop()
    PLAYING_GAMEPLAY_MUSIC3.stop()
    MENU_MUSIC.stop()
    CREDITS_MUSIC.stop()
    SCORES_MUSIC.stop()
    PLAYING_GAMEPLAY_MUSIC.play(-1)
    PLAYING_GAMEPLAY_MUSIC.set_volume(0.09)

def Cambio_Musica_Level2():
    PLAYING_GAMEPLAY_MUSIC.stop()
    PLAYING_GAMEPLAY_MUSIC2.stop()
    PLAYING_GAMEPLAY_MUSIC3.stop()
    MENU_MUSIC.stop()
    CREDITS_MUSIC.stop()
    SCORES_MUSIC.stop()
    PLAYING_GAMEPLAY_MUSIC2.play(-1)
    PLAYING_GAMEPLAY_MUSIC2.set_volume(0.09)

def Cambio_Musica_Level3():
    PLAYING_GAMEPLAY_MUSIC.stop()
    PLAYING_GAMEPLAY_MUSIC2.stop()
    PLAYING_GAMEPLAY_MUSIC3.stop()
    MENU_MUSIC.stop()
    CREDITS_MUSIC.stop()
    SCORES_MUSIC.stop()
    PLAYING_GAMEPLAY_MUSIC3.play(-1)
    PLAYING_GAMEPLAY_MUSIC3.set_volume(0.09)

def Cambio_Musica_Creditos():
    PLAYING_GAMEPLAY_MUSIC.stop()
    PLAYING_GAMEPLAY_MUSIC2.stop()
    PLAYING_GAMEPLAY_MUSIC3.stop()
    MENU_MUSIC.stop()
    CREDITS_MUSIC.stop()
    SCORES_MUSIC.stop()
    CREDITS_MUSIC.play(-1)
    CREDITS_MUSIC.set_volume(0.09)

def Cambio_Musica_Scores():
    PLAYING_GAMEPLAY_MUSIC.stop()
    PLAYING_GAMEPLAY_MUSIC2.stop()
    PLAYING_GAMEPLAY_MUSIC3.stop()
    MENU_MUSIC.stop()
    CREDITS_MUSIC.stop()
    SCORES_MUSIC.stop()
    SCORES_MUSIC.play(-1)
    SCORES_MUSIC.set_volume(0.07)

def read_write_txt():
    with open(r"STAR LIGHT RUNNER/high_scores.txt", "r") as high_scores:
        lista = high_scores.readlines()
    Nueva_Lista = scores_quicksort(pantallas.score, pantallas.nombre_jugador, lista)

    with open(r"STAR LIGHT RUNNER/high_scores.txt", "w") as high_scores:
        high_scores.writelines(Nueva_Lista)

def new_highscore():
    with open(r"STAR LIGHT RUNNER/high_scores.txt", "r") as high_scores:
        lista = high_scores.readlines()

        if pantallas.score > int(lista[1]):
            return True
        elif pantallas.score > int(lista[3]):
            return True
        elif pantallas.score > int(lista[5]):
            return True
        elif pantallas.score > int(lista[7]):
            return True
        elif pantallas.score > int(lista[9]):
            return True
        else:
            return False

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
        # Verificación de la vida del jugador
        if self.vida <= 0:
            EXPLOSION1_SOUND.play()
            EXPLOSION1_SOUND.set_volume(0.1)
            if new_highscore():
                Cambio_Musica_Scores()
                pantallas.pantalla = "high_scores"
                pantallas.new_highscore = True
            else:
                Cambio_Musica_Menu()
                pantallas.pantalla = "Pantalla_de_inicio"
            read_write_txt()
            pantallas.nueva_pantalla = True
            self.rect.center = (300, 700)
            self.vida = 3
            Enemigos.empty()

class enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        num1 = random.randrange(3)
        if num1 == 0:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_personajes,'Meteor.png')), (100, 100))
        elif num1 == 1:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_personajes,'Meteor2.png')), (100, 100))
        else:
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(carpeta_personajes,'Meteor3.png')), (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(W - self.rect.width)
        self.rect.y = 0
        self.velocidad_x = random.randrange(-4,4)
        self.velocidad_y = random.randrange(1,4)

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        # Limites de movimiento en la ventana
        if self.rect.x <= 0:
            EXPLOSION2_SOUND.play()
            EXPLOSION2_SOUND.set_volume(0.09)
            self.velocidad_x = random.randrange(1,4)
            self.velocidad_y = random.randrange(-4,4)
        elif self.rect.x >= 510:
            EXPLOSION2_SOUND.play()
            EXPLOSION2_SOUND.set_volume(0.09)
            self.velocidad_x = random.randrange(-4,-1)
            self.velocidad_y = random.randrange(-4,4)
        if self.rect.y <= 0:
            EXPLOSION2_SOUND.play()
            EXPLOSION2_SOUND.set_volume(0.09)
            self.velocidad_x = random.randrange(-4,4)
            self.velocidad_y = random.randrange(1,4)
        elif self.rect.y >= 710:
            EXPLOSION2_SOUND.play()
            EXPLOSION2_SOUND.set_volume(0.09)
            self.velocidad_x = random.randrange(-4,4)
            self.velocidad_y = random.randrange(-4,-1)

class pantallas():
    def __init__(self):
        self.pantalla = "Pantalla_de_inicio"
        self.running = True
        # Click
        self.click = False
        # Nombre del jugador
        self.text_input = pygame_textinput.TextInput()
        self.nombre_jugador = ""
        # Puntaje
        self.score = 0
        # Variable para el tiempo inicial
        self.tiempo_inicial = 0
        # Variable para saber si la función que llama el nivel se hace por primera vez
        self.nueva_pantalla = True
        # Variable para saber si hay un nuevo puntaje
        self.new_highscore = False
        # Variable para el movimiento del fondo
        self.y = 0

    def cambio_pantalla(self):
        if self.pantalla == "Pantalla_de_inicio":
            self.Pantalla_de_inicio()
        elif self.pantalla == "Pantalla_1":
            if self.nueva_pantalla:
                self.tiempo_inicial = pygame.time.get_ticks()
                self.nueva_pantalla = False
                for x in range(4):
                    meteoritos = enemigos()
                    Enemigos.add(meteoritos)
            self.Pantalla_1()
        elif self.pantalla == "Pantalla_2":
            if self.nueva_pantalla:
                self.tiempo_inicial = pygame.time.get_ticks()
                self.nueva_pantalla = False
                for x in range(6):
                    meteoritos = enemigos()
                    Enemigos.add(meteoritos)
            self.Pantalla_2()
        elif self.pantalla == "Pantalla_3":
            if self.nueva_pantalla:
                self.tiempo_inicial = pygame.time.get_ticks()
                self.nueva_pantalla = False
                for x in range(8):
                    meteoritos = enemigos()
                    Enemigos.add(meteoritos)
            self.Pantalla_3()
        elif self.pantalla == "about":
            self.about()
        elif self.pantalla == "high_scores":
            self.high_scores()

    def Pantalla_de_inicio(self):
        events = pygame.event.get()
        for event in events:
            # Cerrar ventana
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
        mouse = pygame.mouse.get_pos()
        # Animación de botones y clicks
        button_1 = pygame.Rect(80, 500, 192, 69)
        button_2 = pygame.Rect(400, 720, 192, 69)
        button_3 = pygame.Rect(10, 10, 192, 69)
        button_4 = pygame.Rect(290, 500, 108, 69)
        button_5 = pygame.Rect(410, 500, 108, 69)
        button_list = [button_1, button_2, button_3, button_4, button_5]

        button_ = button_img2
        button1 = button_img2
        button2 = button_img2
        button3 = button_img2
        button4 = button_img4
        button5 = button_img5

        for button in button_list:
            if button.collidepoint(mouse):
                if button == button_1:
                    button1 = button_img3
                elif button == button_2:
                    button2 = button_img3
                elif button == button_3:
                    button3 = button_img3
                elif button == button_4:
                    button4 = button_img6
                elif button == button_5:
                    button5 = button_img7
                
                if self.click:
                    if button == button_1:
                        CLICK_SOUND.play()
                        CLICK_SOUND.set_volume(0.1)
                        Cambio_Musica_Level1()
                        self.pantalla = "Pantalla_1"
                    elif button == button_2:
                        CLICK_SOUND.play()
                        CLICK_SOUND.set_volume(0.1)
                        Cambio_Musica_Creditos()
                        self.pantalla = "about"
                    elif button == button_3:
                        CLICK_SOUND.play()
                        CLICK_SOUND.set_volume(0.1)
                        Cambio_Musica_Scores()
                        self.pantalla = "high_scores"
                    elif button == button_4:
                        CLICK_SOUND.play()
                        CLICK_SOUND.set_volume(0.1)
                        Cambio_Musica_Level2()
                        self.pantalla = "Pantalla_2"
                    elif button == button_5:
                        CLICK_SOUND.play()
                        CLICK_SOUND.set_volume(0.1)
                        Cambio_Musica_Level3()
                        self.pantalla = "Pantalla_3"          

        self.click = False
        # Fondo
        ventana.blit(background, (0, 0))
        # Botones
        ventana.blit(button_, (10, 720))
        ventana.blit(button1, (80, 500))
        ventana.blit(button2, (400, 720))
        ventana.blit(button3, (10, 10))
        ventana.blit(button4, (290, 500))
        ventana.blit(button5, (410, 500))
        # Texto
        draw_text(ventana, "play", 40, 180, 515)
        draw_text(ventana, "2", 40, 345, 515)
        draw_text(ventana, "3", 40, 465, 515)
        draw_text(ventana, "about", 40, 500, 735)
        draw_text(ventana, "scores", 40, 110, 25)
        # Input nombre del jugador
        self.text_input.update(events)
        # Blit its surface onto the screen
        ventana.blit(self.text_input.get_surface(), (50, 738))
        self.nombre_jugador = self.text_input.get_text()
    
    def about(self):
        for event in pygame.event.get():
            # Cerrar ventana
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                # Regreso al menú principal
                if event.key == pygame.K_ESCAPE:
                    Cambio_Musica_Menu()
                    self.pantalla = "Pantalla_de_inicio"
        ventana.blit(background, (0, 0))
        draw_text(ventana, "ABOUT", 60, 300, 50)
        draw_text(ventana, "Costa   Rica", 40, 300, 200)
        draw_text(ventana, "Instituto   Tecnologico   de   Costa   Rica", 20, 300, 250)
        draw_text(ventana, "Ingenieria   en   computadores", 20, 300, 300)
        draw_text(ventana, "Introduccion   a   la   programacion", 20, 300, 350)
        draw_text(ventana, "2021", 20, 300, 400)
        draw_text(ventana, "GR   3", 20, 300, 450)
        draw_text(ventana, "Profesor   Leonardo   Araya   Martinez", 20, 300, 500)
        draw_text(ventana, "Daniel   Cob   Beirute Y Adriel Chaves Salazar", 20, 300, 550)
        draw_text(ventana, "Pygame   text   input         Silas Gyger", 20, 300, 600)
        draw_text(ventana, "Usa   las   teclas   UP  DOWN  LEFT  RIGHT   para   moverte", 20, 300, 650)
        draw_text(ventana, "Presiona   la   tecla   de   ESC   en   cualquier   momento", 20, 300, 700)
        draw_text(ventana, "para   volver   al   menu   principal", 20, 300, 720)

    def high_scores(self):
        for event in pygame.event.get():
            # Cerrar ventana
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                # Regreso al menú principal
                if event.key == pygame.K_ESCAPE:
                    Cambio_Musica_Menu()
                    self.pantalla = "Pantalla_de_inicio"
                    self.new_highscore = False
        ventana.blit(background, (0, 0))
        draw_text(ventana, "High   Scores", 60, 300, 50)
        with open(r"STAR LIGHT RUNNER/high_scores.txt", "r") as high_scores:
            lista = high_scores.readlines()
            #Lista_Final = scores_quicksort(pantallas.score, pantallas.nombre_jugador, lista)
            draw_text(ventana, "1         {}   {}".format(lista[0].rstrip(), lista[1].rstrip()), 60, 300, 150)
            draw_text(ventana, "2         {}   {}".format(lista[2].rstrip(), lista[3].rstrip()), 60, 300, 200)
            draw_text(ventana, "3         {}   {}".format(lista[4].rstrip(), lista[5].rstrip()), 60, 300, 250)
            draw_text(ventana, "4         {}   {}".format(lista[6].rstrip(), lista[7].rstrip()), 60, 300, 300)
            draw_text(ventana, "5         {}   {}".format(lista[8].rstrip(), lista[9].rstrip()), 60, 300, 350)
            draw_text(ventana, "6         {}   {}".format(lista[10].rstrip(), lista[11].rstrip()), 60, 300, 400)
            draw_text(ventana, "7         {}   {}".format(lista[12].rstrip(), lista[13].rstrip()), 60, 300, 450)
        
        if self.new_highscore == True:
            draw_text(ventana, "New   High   Score!", 60, 300, 550)

    def Pantalla_1(self):
        for event in pygame.event.get():
                # Cerrar ventana
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    # Regreso al menú principal
                    if event.key == pygame.K_ESCAPE:
                        Cambio_Musica_Menu()
                        Enemigos.empty()
                        self.pantalla = "Pantalla_de_inicio"
                        jugador.vida = 3
                        pantallas.nueva_pantalla = True
        if (pygame.time.get_ticks()-pantallas.tiempo_inicial)//1000 == 60:
            Cambio_Musica_Level2()
            pantallas.pantalla = "Pantalla_2"
            pantallas.nueva_pantalla = True
            jugador.rect.center = (300, 700)
            jugador.vida = 3
            Enemigos.empty()
        all_sprites.update()
        Enemigos.update()
        pantalla_de_juego()
        colisiones()
        all_sprites.draw(ventana)
        Enemigos.draw(ventana)

    def Pantalla_2(self):
        for event in pygame.event.get():
                # Cerrar ventana
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    # Regreso al menú principal
                    if event.key == pygame.K_ESCAPE:
                        Cambio_Musica_Menu()
                        Enemigos.empty()
                        self.pantalla = "Pantalla_de_inicio"
                        jugador.vida = 3
                        pantallas.nueva_pantalla = True
        if (pygame.time.get_ticks()-pantallas.tiempo_inicial)//1000 == 60:
            Cambio_Musica_Level3()
            pantallas.pantalla = "Pantalla_3"
            pantallas.nueva_pantalla = True
            jugador.rect.center = (300, 700)
            jugador.vida = 3
            Enemigos.empty()
        all_sprites.update()
        Enemigos.update()
        pantalla_de_juego()
        colisiones()
        all_sprites.draw(ventana)
        Enemigos.draw(ventana)

    def Pantalla_3(self):
        for event in pygame.event.get():
                # Cerrar ventana
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    # Regreso al menú principal
                    if event.key == pygame.K_ESCAPE:
                        Cambio_Musica_Menu()
                        Enemigos.empty()
                        self.pantalla = "Pantalla_de_inicio"
                        jugador.vida = 3
                        pantallas.nueva_pantalla = True
        if (pygame.time.get_ticks()-pantallas.tiempo_inicial)//1000 == 60:
            if new_highscore():
                Cambio_Musica_Scores()
                pantallas.pantalla = "high_scores"
                pantallas.new_highscore = True
            else:
                Cambio_Musica_Menu()
                pantallas.pantalla = "Pantalla_de_inicio"
            pantallas.nueva_pantalla = True
            jugador.rect.center = (300, 700)
            jugador.vida = 3
            Enemigos.empty()
        all_sprites.update()
        Enemigos.update()
        pantalla_de_juego()
        colisiones()
        all_sprites.draw(ventana)
        Enemigos.draw(ventana)


# función para elección de pantallas
pantallas = pantallas()


jugador = jugador()
all_sprites = pygame.sprite.Group(jugador)


Enemigos = pygame.sprite.Group()


MENU_MUSIC.play(-1)
MENU_MUSIC.set_volume(0.2)


while pantallas.running:
    pantallas.cambio_pantalla()
    pygame.display.update()