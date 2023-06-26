import pygame
import time
import random

pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Snake initial position and size
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Food position
food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
food_spawn = True

# Direction variables
direction = 'RIGHT'
change_to = direction

# Game over flag
game_over = False

# Score
score = 0

# Game loop
game_started = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if not game_started:
                game_started = True
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

    if game_started:
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP] and direction != 'DOWN':
                change_to = 'UP'
            elif keys[pygame.K_DOWN] and direction != 'UP':
                change_to = 'DOWN'
            elif keys[pygame.K_LEFT] and direction != 'RIGHT':
                change_to = 'LEFT'
            elif keys[pygame.K_RIGHT] and direction != 'LEFT':
                change_to = 'RIGHT'

    # Validate direction
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    # Update snake body
    snake_body.insert(0, list(snake_pos))

    # Check if the snake has eaten the food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
        food_spawn = True

    # Clear the game window
    window.fill(black)

    # Draw the snake
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw the food
    pygame.draw.rect(window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Check game over conditions
    if (
        snake_pos[0] < 0
        or snake_pos[0] > width - 10
        or snake_pos[1] < 0
        or snake_pos[1] > height - 10
    ):
        game_over = True

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over = True

    # Display the score
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(f"Score: {score}", True, white)
    score_rect = score_text.get_rect()
    score_rect.topleft = (10, 10)
    window.blit(score_text, score_rect)

    # Display "Game Over" message
    if game_over:
        game_over_font = pygame.font.Font(None, 72)
        game_over_text = game_over_font.render("Game Over", True, red)
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = (width // 2, height // 2)
        window.blit(game_over_text, game_over_rect)

    # Update the game display
    pygame.display.flip()

    # Set the frames per second
    pygame.time.Clock().tick(20)

pygame.quit()
