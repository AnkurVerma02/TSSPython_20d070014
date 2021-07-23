import pygame, sys, time, random
frame_size_x = 720
frame_size_y = 480

snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction

food_pos = [random.randrange(1, (frame_size_x//10))* 10, random.randrange(1, (frame_size_y//10)-1) * 10]
food_spawn = True

score = 0

pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

fps_controller = pygame.time.Clock()

blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

def check_for_events():
    global direction
    global change_to
    global score
    global food_spawn
    global food_pos
    global snake_body
    global snake_pos
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            sys.exit()
        elif eve.type == pygame.KEYDOWN:
            if eve.key == pygame.K_UP:
                change_to = 'UP'
            if eve.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if eve.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if eve.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'

def update_snake():
    global direction
    global change_to
    global score
    global food_spawn
    global food_pos
    global snake_body
    global snake_pos

    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    create_food()

    for pos in snake_body:
        pygame.draw.rect(game_window, green,pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

def create_food():
    global direction
    global change_to
    global score
    global food_spawn
    global food_pos
    global snake_body
    global snake_pos

    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)-1) * 10]

    food_spawn = True
    game_window.fill(black)

def show_score(pos, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    score_rect.midtop = pos
    game_window.blit(score_surface, score_rect)

def update_screen():
    update_snake()
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score((50,20), white, 'sans serif', 25)
    pygame.display.update()

def game_over():
    global direction
    global change_to
    global score
    global food_spawn
    global food_pos
    global snake_body
    global snake_pos

    font1 = pygame.font.SysFont('sans serif', 80)
    game_over_surface1 = font1.render(
        'YOU DIED', True, red)
    game_over_rectangle1 = game_over_surface1.get_rect()
    game_over_rectangle1.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.blit(game_over_surface1, game_over_rectangle1)

    font2 = pygame.font.SysFont('sans serif', 25)
    game_over_surface2 = font2.render(
        'Score :- ' + str(score), True, red)
    game_over_rectangle2 = game_over_surface2.get_rect()
    game_over_rectangle2.midbottom = (frame_size_x/2, 3*frame_size_y/4)
    game_window.blit(game_over_surface2, game_over_rectangle2)

    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

while True:
    check_for_events()
    update_screen()
    fps_controller.tick(25)
