import pygame
import random

pygame.init()
clock = pygame.time.Clock()

ANCHO, ALTO = 800, 600
screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Click Fruit")

# --- Clase Fruta ---
class Fruta:
    def __init__(self, imagen, tipo):
        self.tipo = tipo
        self.image = pygame.image.load(imagen)
        if tipo == "mini_uva":
            self.image = pygame.transform.scale(self.image, (40, 40))
        else:
            self.image = pygame.transform.scale(self.image, (145, 145))
        self.x = random.randint(100, ANCHO - 200)
        self.y = ALTO
        self.vel_x = random.uniform(-3, 3)
        self.vel_y = random.uniform(-18, -12)
        self.gravedad = 0.5

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += self.gravedad
        return self.y < ALTO + 100

    def dibujar(self, pantalla):
        pantalla.blit(self.image, (self.x, self.y))

# --- Generar frutas ---
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
        return Fruta("assets/uva.png", "uva")

frutas.append(crear_fruta_aleatoria())

# --- Loop principal ---
running = True
while running:
    clock.tick(60)
    screen.fill((184, 98, 234))

    # Mover y dibujar frutas
    for fruta in frutas[:]:
        if fruta.mover():
            fruta.dibujar(screen)
        else:
            frutas.remove(fruta)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for fruta in frutas[:]:
                rect = pygame.Rect(fruta.x, fruta.y, fruta.image.get_width(), fruta.image.get_height())
                if rect.collidepoint(pos):
                    # Si es racimo de uva → explota en mini uvas
                    if fruta.tipo == "uva":
                        for i in range(5):
                            mini = Fruta("assets/uva.png", "mini_uva")
                            mini.x = fruta.x + random.randint(-20, 20)
                            mini.y = fruta.y + random.randint(-20, 20)
                            mini.vel_x = random.uniform(-4, 4)
                            mini.vel_y = random.uniform(-8, -4)
                            frutas.append(mini)
                    frutas.remove(fruta)

    # Aparición aleatoria de nuevas frutas
    if random.random() < 0.02:
        frutas.append(crear_fruta_aleatoria())

    pygame.display.flip()

pygame.quit()