import pygame #importamos la libreria
pygame.init()

WIDTH=800 #800 pixeles de ancho
HEIGHT=600 #600 pixeles de alto
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mi primer jueguito")

runing = True
while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    pygame.display.flip()
pygame.quit()