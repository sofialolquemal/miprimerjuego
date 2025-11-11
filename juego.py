import pygame #importamos la libreria
pygame.init() #Inicializar programa


ANCHO=800 #800 pixeles de ancho
ALTO=600 #600 pixeles de alto
screen= pygame.display.set_mode((ANCHO, ALTO)) #la libreria hace que se reconozcan
#como funciones para abrir una ventana


pygame.display.set_caption("Click fruit")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #hacer clic en cerrar ventana
            running = False #cuando eso pasa se cierra
    pygame.display.flip() #se guardan los cambios hechos
pygame.quit() #asi se cierra bien la ventana
#una variable esta en verdadero (ventana abierta) todo el rato hasta que
#al apretar la equis, se vuelve falsa y se cierra

screen.fill((134,2,225))
pygame.display.flip()