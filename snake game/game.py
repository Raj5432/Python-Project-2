import pygame
import random

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = (0, 1)  # right initially
        self.food = self.place_food()
        self.score = 0

    def place_food(self):
        while True:
            x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return x, y

    def draw_grid(self):
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (WIDTH, y))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.direction = (0, -1)
            elif keys[pygame.K_DOWN]:
                self.direction = (0, 1)
            elif keys[pygame.K_LEFT]:
                self.direction = (-1, 0)
            elif keys[pygame.K_RIGHT]:
                self.direction = (1, 0)

            head_x, head_y = self.snake[0]
            dx, dy = self.direction
            new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

            if new_head in self.snake:
                pygame.quit()
                return

            self.snake.insert(0, new_head)

            if new_head == self.food:
                self.score += 1
                self.food = self.place_food()
            else:
                self.snake.pop()

            self.screen.fill(BLACK)
            self.draw_grid()

            for segment in self.snake:
                pygame.draw.rect(self.screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

            pygame.draw.rect(self.screen, RED, (self.food[0] * GRID_SIZE, self.food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
            
            pygame.display.set_caption(f"Snake Game - Score: {self.score}")

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
 