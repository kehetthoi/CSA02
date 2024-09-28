import pygame
import random
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game Cầu Lông')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
class Paddle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 100
        self.color = color
        self.speed = 10
        self.score = 0

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < screen_height - self.height:
            self.y += self.speed

class Ball:
    def __init__(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = 15
        self.speed_x = 5 * random.choice([-1, 1])
        self.speed_y = 5 * random.choice([-1, 1])
        self.color = BLACK

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.speed_y = -self.speed_y

    def reset(self):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.speed_x *= random.choice([-1, 1])
        self.speed_y *= random.choice([-1, 1])

# Lớp Game (Trò chơi)
class Game:
    def __init__(self):
        self.paddle1 = Paddle(50, screen_height // 2 - 50, BLUE)
        self.paddle2 = Paddle(screen_width - 70, screen_height // 2 - 50, RED)
        self.ball = Ball()
        self.winning_score = 10
        self.game_over = False
        self.paused = False
        self.reset_button_width = 200
        self.reset_button_height = 50
        self.stop_button_width = 100
        self.stop_button_height = 50
        self.reset_button_rect = pygame.Rect(screen_width - self.reset_button_width - 20, 20, self.reset_button_width, self.reset_button_height)
        self.stop_button_rect = pygame.Rect(screen_width - self.stop_button_width - 20, 80, self.stop_button_width, self.stop_button_height)
        self.start_time = pygame.time.get_ticks()
        self.game_duration = 300000  # 300 giây = 5 phút

    def draw(self):
        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (screen_width // 2, 0), (screen_width // 2, screen_height), 5)
        self.paddle1.draw()
        self.paddle2.draw()
        self.ball.draw()

        font = pygame.font.Font(None, 74)
        score1_text = font.render(str(self.paddle1.score), True, BLUE)
        score2_text = font.render(str(self.paddle2.score), True, RED)
        screen.blit(score1_text, (screen_width // 4, 20))
        screen.blit(score2_text, (screen_width * 3 // 4, 20))

        # Hiển thị tên người chơi với kích thước nhỏ hơn
        label_font = pygame.font.Font(None, 40)
        player1_label = label_font.render("Player 1", True, BLUE)
        player2_label = label_font.render("Player 2", True, RED)

        # Vị trí ngay giữa khu vực của họ
        player1_label_rect = player1_label.get_rect(center=(screen_width // 4, 70))
        player2_label_rect = player2_label.get_rect(center=(screen_width * 3 // 4, 70))

        screen.blit(player1_label, player1_label_rect)
        screen.blit(player2_label, player2_label_rect)

        if self.game_over:
            winner_text = "Player 1 Wins!" if self.paddle1.score == self.winning_score else "Player 2 Wins!"
            game_over_text = font.render(winner_text, True, BLACK)
            screen.blit(game_over_text, (screen_width // 2 - 200, screen_height // 2 - 50))

            # Vẽ nút chơi lại ở góc trên cùng bên phải
            pygame.draw.rect(screen, GREEN, self.reset_button_rect)
            reset_font = pygame.font.Font(None, 50)  # Kích thước font nhỏ hơn
            reset_text = reset_font.render("Play Again", True, WHITE)
            reset_text_rect = reset_text.get_rect(center=self.reset_button_rect.center)
            screen.blit(reset_text, reset_text_rect)

        if self.paused:
            paused_text = font.render("Paused", True, BLACK)
            screen.blit(paused_text, (screen_width // 2 - 100, screen_height // 2 - 50))
        else:
            # Vẽ nút dừng ở góc trên cùng bên phải
            pygame.draw.rect(screen, RED, self.stop_button_rect)
            stop_font = pygame.font.Font(None, 40)  # Kích thước font nhỏ hơn
            stop_text = stop_font.render("Stop", True, WHITE)
            stop_text_rect = stop_text.get_rect(center=self.stop_button_rect.center)
            screen.blit(stop_text, stop_text_rect)

        # Hiển thị thời gian ở góc trên cùng bên trái
        elapsed_time = pygame.time.get_ticks() - self.start_time
        remaining_time = max(0, (self.game_duration - elapsed_time) // 1000)
        timer_font = pygame.font.Font(None, 36)
        timer_text = timer_font.render(f"Time: {remaining_time}s", True, BLACK)
        screen.blit(timer_text, (20, 20))

    def handle_collision(self):
        if (self.paddle1.x < self.ball.x - self.ball.radius < self.paddle1.x + self.paddle1.width and 
            self.paddle1.y < self.ball.y < self.paddle1.y + self.paddle1.height):
            self.ball.speed_x = -self.ball.speed_x
        
        if (self.paddle2.x < self.ball.x + self.ball.radius < self.paddle2.x + self.paddle2.width and 
            self.paddle2.y < self.ball.y < self.paddle2.y + self.paddle2.height):
            self.ball.speed_x = -self.ball.speed_x

        if self.ball.x - self.ball.radius <= 0:
            self.paddle2.score += 1
            self.ball.reset()

        if self.ball.x + self.ball.radius >= screen_width:
            self.paddle1.score += 1
            self.ball.reset()

        if self.paddle1.score == self.winning_score or self.paddle2.score == self.winning_score:
            self.game_over = True

    def handle_input(self):
        if not self.paused:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddle1.move_up()
            if keys[pygame.K_s]:
                self.paddle1.move_down()
            if keys[pygame.K_UP]:
                self.paddle2.move_up()
            if keys[pygame.K_DOWN]:
                self.paddle2.move_down()

    def update(self):
        if not self.paused and not self.game_over:
            self.ball.move()
            self.handle_collision()
        
        # Dừng trò chơi khi thời gian hết
        if pygame.time.get_ticks() - self.start_time >= self.game_duration:
            self.game_over = True

    def reset_game(self):
        self.paddle1 = Paddle(50, screen_height // 2 - 50, BLUE)
        self.paddle2 = Paddle(screen_width - 70, screen_height // 2 - 50, RED)
        self.ball = Ball()
        self.game_over = False
        self.start_time = pygame.time.get_ticks()  # Đặt lại thời gian bắt đầu

# Vòng lặp chính
game = Game()
running = True
while running:
    game.draw()
    game.handle_input()
    game.update()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if game.reset_button_rect.collidepoint(mouse_pos) and game.game_over:
                game.reset_game()
            if game.stop_button_rect.collidepoint(mouse_pos):
                game.paused = not game.paused  # Chuyển đổi trạng thái dừng

    pygame.time.Clock().tick(60)

pygame.quit()













            
           



