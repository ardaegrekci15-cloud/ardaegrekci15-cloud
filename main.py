
import pygame
import asyncio
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Dodge - Arda Is Games")

clock = pygame.time.Clock()

BACKGROUND = (11, 13, 22)
CYAN = (0, 255, 210)
RED = (255, 60, 90)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 28, bold=True)
small_font = pygame.font.SysFont("Arial", 20)

def draw_text(text, selected_font, color, x, y):
    surface = selected_font.render(text, True, color)
    screen.blit(surface, (x, y))

async def main():
    player = pygame.Rect(375, 520, 50, 50)
    obstacles = []

    speed = 7
    obstacle_speed = 5
    spawn_timer = 0
    score = 0
    game_over = False
    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_r and game_over:
                    player.x = WIDTH // 2 - 25
                    obstacles.clear()
                    score = 0
                    obstacle_speed = 5
                    game_over = False

        if not game_over:

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.x -= speed

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.x += speed

            player.x = max(0, min(WIDTH - 50, player.x))

            spawn_timer += 1

            if spawn_timer >= 35:
                x = random.randint(0, WIDTH - 40)
                obstacles.append(pygame.Rect(x, -40, 40, 40))
                spawn_timer = 0

            for obstacle in obstacles:
                obstacle.y += obstacle_speed

                if player.colliderect(obstacle):
                    game_over = True

            obstacles = [
                obstacle for obstacle in obstacles
                if obstacle.y < HEIGHT
            ]

            score += 1
            obstacle_speed = min(12, 5 + score // 1000)

        screen.fill(BACKGROUND)

        pygame.draw.rect(
            screen, CYAN, player, border_radius=10
        )

        for obstacle in obstacles:
            pygame.draw.rect(
                screen, RED, obstacle, border_radius=8
            )

        draw_text(f"SCORE: {score}", font, WHITE, 20, 20)

        if game_over:
            draw_text(
                "GAME OVER", font, RED,
                WIDTH // 2 - 90, HEIGHT // 2 - 50
            )
            draw_text(
                f"Skorun: {score}", small_font, WHITE,
                WIDTH // 2 - 50, HEIGHT // 2
            )
            draw_text(
                "Tekrar icin R tusuna bas",
                small_font, CYAN,
                WIDTH // 2 - 135, HEIGHT // 2 + 40
            )

        pygame.display.flip()
        # Tarayicida bloklayici clock.tick() kullanma; Pygbag olay dongusunu kilitleyebilir.
        await asyncio.sleep(1 / 60)

    pygame.quit()

asyncio.run(main())
