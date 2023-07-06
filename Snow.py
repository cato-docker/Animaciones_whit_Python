import pygame, sys, random
#Inicializamos pygame

pygame.init()

#Crear la ventana (Definimos tamaño, tiempo y inicializamos la ventana)
size = (500,300)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
titulo = pygame.display.set_caption("Snow")

#Creamos los colores
RED = (255 ,0 ,0)
GREEN = (0, 255 ,0)
BLUE = (0, 0 ,255)
BLACK = (0 , 0, 0)
WHITE = (255 ,255 , 255)

coord_list =[]

for i in range(60):
        x = random.randint(0,500)
        y = random.randint(0,300)
        coord_list.append([x,y])
        pygame.draw.circle(screen,RED,(x,y),10)

#Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #Color de fondo
    screen.fill(BLACK)

    #Logica del juego
    for coord in coord_list:
        x = coord [0]
        y = coord [1]
        pygame.draw.circle(screen,WHITE,coord,2)
        coord[1] += 1
        if coord[1] > 300: # Chequeamos los puntos, para que se muestren en pantalla de nuevo
            coord[1]= 0
            
    
    

    

    #Actualizar pantalla y tiempo
    pygame.display.flip()
    clock.tick(20)



pygame.display.update()