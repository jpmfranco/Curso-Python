import pygame
import random
import math

#Inicializa pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))


#configurar titulo e icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load("dia 10\\ovni.png")
pygame.display.set_icon(icono)
backgro = pygame.image.load("dia 10\\fondo.jpg")


# Jugador

# Variables jugador
player = pygame.image.load("dia 10\\cohete.png")
player_x = 368
player_y = 500
player_change_x = 0

# variables de Enemigo
enemy = []
enemy_x = []
enemy_y = []
enemy_change_x = []
enemy_change_y = []
cantEnemy = 8

for e in range(cantEnemy):
    enemy.append(pygame.image.load("dia 10\\enemigo.png"))
    enemy_x.append(random.randint(0,736))
    enemy_y.append(random.randint(50,200))
    enemy_change_x.append(0.3)
    enemy_change_y.append(50)

# variables de la bala
bullet = pygame.image.load("dia 10\\bala.png")
bullet_x = 0
bullet_y = 500
bullet_change_x = 0
bullet_change_y = 0.3
bullet_visible = False

#Puntaje
points = 0
fuente = pygame.font.Font('freesansbold.ttf',32)
p_x = 10
p_y = 10


# funcion mostrar puntaje


# funcion jugador
def player1(x, y):
    pantalla.blit(player,(x,y))

# funcion enemigo
def enemy1(x, y, ene):
    pantalla.blit(enemy[ene],(x,y))

# funcion bala
def bullet1(x, y):
    global bullet_visible
    bullet_visible = True
    pantalla.blit(bullet,(x+16, y+10))

def collition(x1,y1,x2,y2):
    distance = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 -y1,2))
    if distance < 27:
        return True
    else:
        return False


#Loop del juego
se_ejecuta  = True
while se_ejecuta:
    #IMG
    pantalla.blit(backgro,(0,0))
    
    # iterar eventos
    for evento in pygame.event.get():

        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_change_x = -0.2
            if evento.key == pygame.K_RIGHT:
                player_change_x = 0.2
            if evento.key == pygame.K_SPACE:
                if not bullet_visible:
                    bullet_x = player_x
                    bullet1(bullet_x,bullet_y)
            

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                player_change_x = 0

    # Modificar ubicacion del jugador
    player_x += player_change_x
    

    #Mantener dentro de bordes al jugador
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

     # Modificar ubicacion del enemigo
    for e in range(cantEnemy):
        enemy_x[e] += enemy_change_x[e]

    

        #Mantener dentro de bordes del enemigo
        if enemy_x[e] <= 0:
            enemy_change_x[e] = 0.2
            enemy_y[e] += enemy_change_y[e]
        elif enemy_x[e] >= 736:
            enemy_change_x[e] = -0.2
            enemy_y[e] += enemy_change_y[e]

        # Verificar colision
        colison = collition(enemy_x[e],enemy_y[e],bullet_x,bullet_y)
        if colison:
            bullet_y = 500
            bullet_visible = False
            points += 1
            enemy_x[e] = random.randint(0,736)
            enemy_y[e] = random.randint(50,200)
        enemy1(enemy_x[e],enemy_y[e], e)

    # Movimiento bala
    if bullet_y <= -64:
        bullet_y = 500
        bullet_visible = False
    if bullet_visible:
        bullet1(bullet_x,bullet_y)
        bullet_y -= bullet_change_y

    


    player1(player_x,player_y)
    


    # Actualiacion de pantalla
    pygame.display.update()