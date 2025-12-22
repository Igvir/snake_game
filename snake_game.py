import pygame
import random
import sys

pygame.init()

# Game settings
WINDOW_SIZE = 600
CELL_SIZE = 20
CELLS = WINDOW_SIZE // CELL_SIZE

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Font
font = pygame.font.Font(None, 36)

class Snake:
    def __init__(self):
        self.body = [(CELLS//2, CELLS//2)]
        self.direction = (1, 0)
    
    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        return self.body.pop()
    
    def grow(self):
        self.body.append(self.body[-1])
    
    def check_collision(self):
        head = self.body[0]
        return (head[0] < 0 or head[0] >= CELLS or 
                head[1] < 0 or head[1] >= CELLS or 
                head in self.body[1:])

def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    
    snake = Snake()
    food = (random.randint(0, CELLS-1), random.randint(0, CELLS-1))
    score = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_game_over(screen, score)
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != (0, 1):
                    snake.direction = (0, -1)
                elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                    snake.direction = (0, 1)
                elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                    snake.direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                    snake.direction = (1, 0)
        
        tail = snake.move()
        
        if snake.body[0] == food:
            snake.body.append(tail)
            food = (random.randint(0, CELLS-1), random.randint(0, CELLS-1))
            score += 10
        
        if snake.check_collision():
            show_game_over(screen, score)
            pygame.quit()
            sys.exit()
        
        screen.fill(BLACK)
        
        # Draw snake
        for segment in snake.body:
            pygame.draw.rect(screen, GREEN, 
                           (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, 
                            CELL_SIZE, CELL_SIZE))
        
        # Draw food (circle/apple)
        center_x = food[0] * CELL_SIZE + CELL_SIZE // 2
        center_y = food[1] * CELL_SIZE + CELL_SIZE // 2
        pygame.draw.circle(screen, RED, (center_x, center_y), CELL_SIZE // 2)
        
        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        pygame.display.flip()
        clock.tick(10)

def show_game_over(screen, score):
    screen.fill(BLACK)
    game_over_text = font.render("Game Over!", True, WHITE)
    final_score_text = font.render(f"Final Score: {score}", True, WHITE)
    
    screen.blit(game_over_text, (WINDOW_SIZE//2 - 80, WINDOW_SIZE//2 - 40))
    screen.blit(final_score_text, (WINDOW_SIZE//2 - 100, WINDOW_SIZE//2))
    
    pygame.display.flip()
    pygame.time.wait(3000)

if __name__ == "__main__":
    main()
