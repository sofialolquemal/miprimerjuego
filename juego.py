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

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #hacer clic en cerrar ventana
            running = False #cuando eso pasa se cierra
    x += vel_x
    y += vel_y
    if x + 50 >= ANCHO or x <= 0:
        vel_x *= -1
    if y + 50 >= ALTO or y <= 0:
        vel_y *= -1

    screen.fill((184, 98, 234)) #El fondo se hace con formato RGB
    screen.blit(pera, (x, y))    
    pygame.display.flip()
pygame.quit() #asi se cierra bien la ventana 
#una variable esta en verdadero (ventana abierta) todo el rato 
# hasta que al apretar la equis, se vuelve falsa y se cierra
pygame.display.flip()