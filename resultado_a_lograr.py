import pygame
import random
import math
import sys

# Inicializar pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Fruit Ninja")

# Colores
WHITE = (255, 134, 25)
RED = (255, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Reloj
clock = pygame.time.Clock()

# Clase Fruta
class Fruit:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT + 2
        self.radius = 30
        self.color = random.choice([(255, 100, 100), (100, 255, 100), (100, 100, 255)])
        self.vel_y = random.uniform(-15, -10)
        self.vel_x = random.uniform(-3, 3)
        self.active = True

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += 0.5  # gravedad
        if self.y > HEIGHT + 2:
            self.active = False

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

# Variables del juego
fruits = []
score = 0
mouse_positions = []

# Loop principal
running = True
while running:
    screen.fill((30, 30, 30))
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Registrar movimiento del ratón
    mouse_positions.append(pygame.mouse.get_pos())
    if len(mouse_positions) > 15:
        mouse_positions.pop(0)

    # Generar nuevas frutas
    if random.random() < 0.02:
        fruits.append(Fruit())

    # Mover y dibujar frutas
    for fruit in fruits[:]:
        fruit.move()
        fruit.draw(screen)
        if not fruit.active:
            fruits.remove(fruit)

    # Dibujar el "corte" del ratón
    if len(mouse_positions) > 1:
        pygame.draw.lines(screen, WHITE, False, mouse_positions, 3)

    # Detectar colisiones (corte de frutas)
    for fruit in fruits[:]:
        for pos in mouse_positions:
            if math.hypot(fruit.x - pos[0], fruit.y - pos[1]) < fruit.radius:
                score += 1
                fruits.remove(fruit)
                break

    # Mostrar puntaje
    score_text = font.render(f"Puntaje: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()