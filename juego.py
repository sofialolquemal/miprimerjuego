import pygame #importamos la libreria
pygame.init() #Inicializar programa

ANCHO=800 #800 pixeles de ancho
ALTO=600 #600 pixeles de alto
screen= pygame.display.set_mode((ANCHO, ALTO)) #la libreria hace que se reconozcan
#como funciones para abrir una ventana

pygame.display.set_caption("Click fruit")
pera = pygame.image.load("assets/pera.png")
pera = pygame.transform.scale(pera, (145, 145))
x = 350
y = 250
vel_x = 2
vel_y = 1

import random

class Fruta:
    def __init__(self, imagen):
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, (145, 145))
        self.x = random.randint(0, ANCHO - 145)
        self.y = random.randint(0, ALTO - 145)
        self.vel_x = random.choice([-3, 3])
        self.vel_y = random.choice([-2, 2])

running = True
frutas = [Fruta("assets/pera.png", "assets/manzana.png", "assets/fresa.png", "assets/naranja.png", "assets/racimo.uva.png")]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #hacer clic en cerrar ventana
            running = False #cuando eso pasa se cierra
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()  # posición del clic
        print(pos)
    x += vel_x
    y += vel_y
    if x + 150 >= ANCHO or x <= 0:
        vel_x *= -1
    if y + 150 >= ALTO or y <= 0:
        vel_y *= -1

    screen.fill((184, 98, 234)) #El fondo se hace con formato RGB
    screen.blit(pera, (x, y))    
    pygame.display.flip()
pygame.quit() #asi se cierra bien la ventana 
#una variable esta en verdadero (ventana abierta) todo el rato 
# hasta que al apretar la equis, se vuelve falsa y se cierra
pygame.display.flip()