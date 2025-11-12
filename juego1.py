import pygame  # importamos la librería
import random  # para posiciones y direcciones aleatorias

pygame.init()  # inicializar Pygame
clock = pygame.time.Clock()
# --- Configuración de la pantalla ---
ANCHO = 800
ALTO = 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Click Fruit")

# --- Clase para las frutas ---
class Fruta:
    def __init__(self, imagen, tipo):
        self.tipo = tipo
        self.image = pygame.image.load(imagen)
        if tipo == "mini_uva":
            self.image = pygame.transform.scale(self.image, (40, 40))
        else:
            self.image = pygame.transform.scale(self.image, (145, 145))
        self.image = pygame.transform.scale(self.image, (145, 145))
        self.x = random.randint(100, ANCHO - 200) 
        self.y = ALTO - 400                         
        self.vel_x = random.uniform(-3, 3)          
        self.vel_y = random.uniform(-8, 5)       
        self.gravedad = 0.25

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += 0.5  # gravedad
        if self.vel_y > 10:
            self.vel_y = 10
        if self.y > ALTO + 2:
            self.active = False
        if self.y > ALTO + 100:
            return False  # fruta muerta (ya cayó)
        return True

    def dibujar(self, pantalla):
        pantalla.blit(self.image, (self.x, self.y))

frutas = []
def crear_fruta_aleatoria():
    tipo = random.choice(["pera", "manzana", "naranja", "fresa", "uva"])
    if tipo == "pera":
        return Fruta("assets/pera.png", "pera")
    elif tipo == "manzana":
        return Fruta("assets/manzana.png", "manzana")
    elif tipo == "naranja":
        return Fruta("assets/naranja.png", "naranja")
    elif tipo == "fresa":
        return Fruta("assets/fresa.png", "fresa")
    elif tipo == "uva":
        return Fruta("assets/racimo.uva.png", "uva")

frutas.append(crear_fruta_aleatoria())

running = True
while running:
    clock.tick(60)
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
            for fruta in frutas[:]:
                # Detectar si se hizo clic sobre una fruta
                rect = pygame.Rect(fruta.x, fruta.y, fruta.image.get_width(), fruta.image.get_height())
                if rect.collidepoint(pos):
                    # Si es racimo de uva → explota en mini uvas 🍇💥
                    if fruta.tipo == "uva":
                        for i in range(5):
                            mini = Fruta("assets/uva.png", "mini_uva")
                            mini.x = fruta.x + random.randint(-20, 20)
                            mini.y = fruta.y + random.randint(-20, 20)
                            mini.vel_x = random.uniform(-4, 4)
                            mini.vel_y = random.uniform(-8, -4)
                            frutas.append(mini)
                    # Eliminar la fruta clickeada
                    frutas.remove(fruta)

    for fruta in frutas[:]:
        viva = fruta.mover()
        if viva:
            fruta.dibujar(screen)
        else:
            frutas.remove(fruta)

    if random.random() < 0.02:  # probabilidad de aparición
        frutas.append(Fruta("assets/pera.png"))
    # actualizar pantalla
    pygame.display.flip()

pygame.quit()  # cerrar Pygame correctamente