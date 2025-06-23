import pygame

#Inicializa pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))


#configurar titulo e icono
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load("dia 10\\ovni.png")
pygame.display.set_icon(icono)


# Jugador

# Variables jugador
player = pygame.image.load("dia 10\\cohete.png")
player_x = 368
player_y = 536
player_change_x = 0

#funcion jugador
def player1(x, y):
    pantalla.blit(player,(x,y))

#Loop del juego
se_ejecuta  = True
while se_ejecuta:
    #RGB
    pantalla.fill((205,144,228))
    
    # iterar eventos
    for evento in pygame.event.get():

        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                player_change_x = -0.1
            if evento.key == pygame.K_RIGHT:
                player_change_x = 0.1

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                player_change_x = 0

    # Modificar ubicacion
    player_x += player_change_x

    #Mantener dentro de bordes
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    player1(player_x,player_y)



    # Actualiacion de pantalla
    pygame.display.update()