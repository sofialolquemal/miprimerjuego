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
        self.x = random.randint(100, ANCHO - 200) 
        self.y = ALTO - 80                          
        self.vel_x = random.uniform(-3, 3)          
        self.vel_y = random.uniform(-10, -6)       
        self.gravedad = 0.4

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += self.gravedad  # gravedad

    # si sale de la pantalla (cayó), eliminarla
        if self.y > ALTO + 100:
            return False  # fruta muerta (ya cayó)
        return True

    def dibujar(self, pantalla):
        pantalla.blit(self.image, (self.x, self.y))

# --- Lista con frutas ---
frutas = [
    Fruta("assets/pera.png"),
    Fruta("assets/naranja.png"),
    Fruta("assets/manzana.png"),
    Fruta("assets/fresa.png"),
    Fruta("assets/racimo.uva.png")
]  # puedes duplicar o cambiar por más frutas

running = True
while running:
    screen.fill((184, 98, 234))
    for fruta in frutas[:]:
        viva = fruta.mover()
        if not viva:
            frutas.remove(fruta)  # si cayó, eliminarla
        else:
            fruta.dibujar(screen)
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

    if random.random() < 0.02:  # probabilidad de aparición
        frutas.append(Fruta("assets/pera.png"))
    # actualizar pantalla
    pygame.display.flip()

pygame.quit()  # cerrar Pygame correctamente