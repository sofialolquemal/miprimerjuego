import pygame  # importamos la librería
import random  # para posiciones y direcciones aleatorias

pygame.init()  # inicializar Pygame

# --- Configuración de la pantalla ---
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Click Fruit")

# --- Clase para las frutas ---
class Fruta:
    def __init__(self, imagen):
        # cargar y escalar imagen
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, (145, 145))
        # posición aleatoria dentro de la pantalla
        self.x = random.randint(0, ANCHO - 145)
        self.y = random.randint(0, ALTO - 145)
        # velocidad aleatoria (positivo o negativo para dirección)
        self.vel_x = random.choice([-3, 3])
        self.vel_y = random.choice([-2, 2])

    def mover(self):
        # mover fruta
        self.x += self.vel_x
        self.y += self.vel_y

        # rebotar en los bordes
        if self.x + 145 >= ANCHO or self.x <= 0:
            self.vel_x *= -1
        if self.y + 145 >= ALTO or self.y <= 0:
            self.vel_y *= -1

    def dibujar(self, pantalla):
        pantalla.blit(self.image, (self.x, self.y))

# --- Lista con frutas ---
frutas = [
    Fruta("assets/pera.png"),
    Fruta("assets/pera.png")
]  # puedes duplicar o cambiar por más frutas

# --- Bucle principal ---
running = True
while running:
    # fondo
    screen.fill((184, 98, 234))

    # manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # detectar clic
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for fruta in frutas[:]:  # recorremos copia de la lista
                if fruta.x <= pos[0] <= fruta.x + 145 and fruta.y <= pos[1] <= fruta.y + 145:
                    frutas.remove(fruta)  # eliminar fruta clickeada
                    frutas.append(Fruta("assets/pera.png"))  # crear nueva fruta

    # mover y dibujar frutas
    for fruta in frutas:
        fruta.mover()
        fruta.dibujar(screen)

    # actualizar pantalla
    pygame.display.flip()

pygame.quit()  # cerrar Pygame correctamente