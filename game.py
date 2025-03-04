# import pygame
# import random
# from datetime import datetime

# # Initialize Pygame
# pygame.init()

# # Window setup
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Asteroid Game")

# # Load sprites (replace with your actual image files)
# player_img = pygame.image.load("spaceship.png").convert_alpha()  # 60x60 px recommended
# bullet_img = pygame.image.load("big_bullet.png").convert_alpha()  # 20x40 px recommended
# asteroid_img = pygame.image.load("asteroid.png").convert_alpha()  # 50x50 px recommended
# player_img = pygame.transform.scale(player_img, (60, 60))
# bullet_img = pygame.transform.scale(bullet_img, (20, 40))
# asteroid_img = pygame.transform.scale(asteroid_img, (50, 50))

# # Load sound (replace with your Super Mario theme file)
# pygame.mixer.music.load("super_mario.mp3")
# pygame.mixer.music.play(-1)  # -1 means loop forever

# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)

# # Player properties
# PLAYER_SPEED = 5
# player_x = WINDOW_WIDTH // 2 - 30
# player_y = WINDOW_HEIGHT - 70

# # Bullet properties
# BULLET_SPEED = 8
# bullets = []

# # Asteroid properties
# ASTEROID_SPEED = 3
# asteroids = []

# # Game variables
# clock = pygame.time.Clock()
# running = True
# game_over = False
# score = 0
# player_name = input("Enter your name: ")  # Get player name at start

# # Score tracking
# try:
#     with open("high_scores.txt", "r") as f:
#         high_scores = eval(f.read())  # Dictionary of {name: [score, datetime]}
# except:
#     high_scores = {}

# # Font
# font = pygame.font.Font(None, 36)

# # Game loop
# while running:
#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN and not game_over:
#             if event.key == pygame.K_SPACE and len(bullets) < 5:
#                 bullets.append([player_x + 20, player_y - 40])

#     if not game_over:
#         # Player movement
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_LEFT] and player_x > 0:
#             player_x -= PLAYER_SPEED
#         if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - 60:
#             player_x += PLAYER_SPEED

#         # Update bullets
#         for bullet in bullets[:]:
#             bullet[1] -= BULLET_SPEED
#             if bullet[1] < -40:
#                 bullets.remove(bullet)

#         # Spawn asteroids
#         if random.randint(1, 60) == 1:
#             asteroids.append([random.randint(0, WINDOW_WIDTH - 50), -50])

#         # Update asteroids
#         for asteroid in asteroids[:]:
#             asteroid[1] += ASTEROID_SPEED
#             if asteroid[1] > WINDOW_HEIGHT:
#                 asteroids.remove(asteroid)

#         # Collision detection
#         for bullet in bullets[:]:
#             bullet_rect = pygame.Rect(bullet[0], bullet[1], 20, 40)
#             for asteroid in asteroids[:]:
#                 asteroid_rect = pygame.Rect(asteroid[0], asteroid[1], 50, 50)
#                 if bullet_rect.colliderect(asteroid_rect):
#                     bullets.remove(bullet)
#                     asteroids.remove(asteroid)
#                     score += 10
#                     break

#         # Check for asteroid hitting player
#         player_rect = pygame.Rect(player_x, player_y, 60, 60)
#         for asteroid in asteroids:
#             asteroid_rect = pygame.Rect(asteroid[0], asteroid[1], 50, 50)
#             if player_rect.colliderect(asteroid_rect):
#                 game_over = True
#                 # Save score
#                 current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 high_scores[player_name] = [score, current_time]
#                 with open("high_scores.txt", "w") as f:
#                     f.write(str(high_scores))

#     # Drawing
#     screen.fill(BLACK)
    
#     if not game_over:
#         # Draw player
#         screen.blit(player_img, (player_x, player_y))
        
#         # Draw bullets
#         for bullet in bullets:
#             screen.blit(bullet_img, (bullet[0], bullet[1]))

#         # Draw asteroids
#         for asteroid in asteroids:
#             screen.blit(asteroid_img, (asteroid[0], asteroid[1]))
        
#         # Draw score and date
#         score_text = font.render(f"Score: {score}", True, WHITE)
#         date_text = font.render(datetime.now().strftime("%Y-%m-%d %H:%M"), True, WHITE)
#         screen.blit(score_text, (10, 10))
#         screen.blit(date_text, (10, 50))
#     else:
#         # Game over screen with scores
#         game_over_text = font.render('GAME OVER', True, WHITE)
#         score_text = font.render(f'Your Score: {score}', True, WHITE)
#         screen.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, 200))
#         screen.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, 300))
        
#         # Show high scores
#         y_pos = 400
#         high_score_text = font.render('High Scores:', True, WHITE)
#         screen.blit(high_score_text, (WINDOW_WIDTH//2 - high_score_text.get_width()//2, y_pos))
#         y_pos += 40
#         sorted_scores = sorted(high_scores.items(), key=lambda x: x[1][0], reverse=True)[:5]
#         for name, (high_score, time) in sorted_scores:
#             score_entry = font.render(f"{name}: {high_score} ({time})", True, WHITE)
#             screen.blit(score_entry, (WINDOW_WIDTH//2 - score_entry.get_width()//2, y_pos))
#             y_pos += 40

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()



import pygame # Importing Pygame library - the backbone of our game
import random # Importing random library for random number of asteroids
from datetime import datetime # its intutive right... right? 

# Initialize Pygame - this is required before any other Pygame functions aka critical step
pygame.init()

# Default Window setup
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Asteroid Game") 

# Load assets, fallback to colors if images not found
try:
    player_img = pygame.image.load("spaceship.png").convert_alpha() 
    # Loading images, convert_alpha() to transparency in the images - recommended for PNGs aka life saver 🦸‍♂️
    bullet_img = pygame.image.load("big_bullet.png").convert_alpha()
    asteroid_img = pygame.image.load("asteroid.png").convert_alpha()
    player_img = pygame.transform.scale(player_img, (60, 60)) # Resizing images to fit the game
    bullet_img = pygame.transform.scale(bullet_img, (20, 40))
    asteroid_img = pygame.transform.scale(asteroid_img, (50, 50))
except pygame.error as e:
    print(f"Error loading sprites: {e}")
    pygame.quit() # Bye 👋
    exit()

try:
    pygame.mixer.music.load("super_mario.mp3") # Loading epic Super Mario theme
    pygame.mixer.music.play(-1) # Loop forever 🔄
except pygame.error as e:
    print(f"Error loading MP3: {e}") 
    try: # Fallback to WAV - wavelength audio files are generally more reliable 
        pygame.mixer.music.load("super_mario.wav")
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print(f"Error loading WAV: {e}")
        print("Continuing without music...") # No music, no problem 🤷‍♂️ - true gamers hear music in their heads 😎

# Colors since we're not using images
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Font - None
font = pygame.font.Font(None, 36)

# Game function - secret sauce
def run_game():
    global WINDOW_WIDTH, WINDOW_HEIGHT, screen  # Allow modifying global window size as you please
    
    # Game variables
    PLAYER_SPEED = 5
    BULLET_SPEED = 8
    ASTEROID_SPEED = 3
    
    player_x = WINDOW_WIDTH // 2 - 30 # Player position
    player_y = WINDOW_HEIGHT - 70 # same as above
    bullets = [] # List of bullet positions [x, y]
    asteroids = [] # List of asteroid positions [x, y]
    score = 0 # Player score
    game_over = False # does this need explanation? 🤔
    entering_name = True  # Flag for name entry state
    player_name = "" # Player name  
    fullscreen = False # Default state of Fullscreen flag
    
    clock = pygame.time.Clock() # Game clock 
    running = True
    
    # Load high scores from file
    try:
        with open("high_scores.txt", "r") as f:
            high_scores = eval(f.read())
    except:
        high_scores = {} # No file or is empty

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Close window, ❌ button
                return False
            if event.type == pygame.VIDEORESIZE:
                # Handling window maximize/resize ⏹️
                WINDOW_WIDTH, WINDOW_HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
            if event.type == pygame.KEYDOWN: # Key press event
                if entering_name:
                    # Name entry logic
                    if event.key == pygame.K_RETURN and player_name: # Enter key
                        entering_name = False
                    elif event.key == pygame.K_BACKSPACE: # Backspace
                        player_name = player_name[:-1]
                    elif event.unicode.isalnum() and len(player_name) < 15: # Alphanumeric characters only
                        player_name += event.unicode
                elif not game_over: 
                    if event.key == pygame.K_SPACE and len(bullets) < 5: # Hit that Space bar to fire bullets 
                        bullets.append([player_x + 20, player_y - 40]) # Bullet position
                    elif event.key == pygame.K_f:  # Toggle fullscreen
                        fullscreen = not fullscreen 
                        if fullscreen:
                            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Fullscreen mode
                            WINDOW_WIDTH, WINDOW_HEIGHT = screen.get_size()
                        else:
                            screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE) # Default window size
                            WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
                elif game_over and event.key == pygame.K_r:
                    return True

        if not entering_name and not game_over:
            # Player movement scaled to window size
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= PLAYER_SPEED
            if keys[pygame.K_RIGHT] and player_x < WINDOW_WIDTH - 60:
                player_x += PLAYER_SPEED

            # Update bullets
            for bullet in bullets[:]:
                bullet[1] -= BULLET_SPEED # bullets go up
                if bullet[1] < -40: 
                    bullets.remove(bullet) # Remove bullets, if goes off top 

            # Spawn asteroids randomly
            if random.randint(1, 60) == 1:
                asteroids.append([random.randint(0, WINDOW_WIDTH - 50), -50])

            # Update asteroids
            for asteroid in asteroids[:]:
                asteroid[1] += ASTEROID_SPEED # asteroids go down
                if asteroid[1] > WINDOW_HEIGHT:
                    asteroids.remove(asteroid) # Remove asteroids, if goes off bottom

            # Collision detection
            for bullet in bullets[:]:
                bullet_rect = pygame.Rect(bullet[0], bullet[1], 20, 40) # Bullet rectangle 
                for asteroid in asteroids[:]:
                    asteroid_rect = pygame.Rect(asteroid[0], asteroid[1], 50, 50) # Asteroid rectangle
                    if bullet_rect.colliderect(asteroid_rect): # Bullet hit asteroid- overlapping of bullets and asteroids rectangles
                        bullets.remove(bullet)
                        asteroids.remove(asteroid)
                        score += 10
                        break

            # Check for game over
            player_rect = pygame.Rect(player_x, player_y, 60, 60) # Player rectangle
            for asteroid in asteroids:
                asteroid_rect = pygame.Rect(asteroid[0], asteroid[1], 50, 50)
                if player_rect.colliderect(asteroid_rect): # Player hit asteroid- overlapping of player spaceship and asteroids rectangles
                    game_over = True
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    high_scores[player_name] = [score, current_time]
                    with open("high_scores.txt", "w") as f:
                        f.write(str(high_scores))

        # Drawing 🎨🖌️
        screen.fill(BLACK) 
        
        if entering_name:
            # Draw name entry screen
            prompt_text = font.render("Enter your name:", True, WHITE)
            name_text = font.render(player_name, True, WHITE)
            # all this stuff 👇 => Centered text 
            screen.blit(prompt_text, (WINDOW_WIDTH//2 - prompt_text.get_width()//2, WINDOW_HEIGHT//2 - 40)) 
            screen.blit(name_text, (WINDOW_WIDTH//2 - name_text.get_width()//2, WINDOW_HEIGHT//2))
        elif not game_over:
            screen.blit(player_img, (player_x, player_y)) # Player
            for bullet in bullets:
                screen.blit(bullet_img, (bullet[0], bullet[1])) # Bullets
            for asteroid in asteroids:
                screen.blit(asteroid_img, (asteroid[0], asteroid[1]))   # Asteroids
            
            # History of our glourious players scores and dates
            score_text = font.render(f"Score: {score}", True, WHITE)
            date_text = font.render(datetime.now().strftime("%Y-%m-%d %H:%M"), True, WHITE)
            screen.blit(score_text, (10, 10))
            screen.blit(date_text, (10, 50))
        else:
            game_over_text = font.render('GAME OVER - Press R to Restart', True, WHITE)
            score_text = font.render(f'Your Score: {score}', True, WHITE)
            # Centered text
            screen.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, WINDOW_HEIGHT//3))
            screen.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, WINDOW_HEIGHT//3 + 100))
            
            y_pos = WINDOW_HEIGHT//3 + 200 
            high_score_text = font.render('High Scores:', True, WHITE)
            screen.blit(high_score_text, (WINDOW_WIDTH//2 - high_score_text.get_width()//2, y_pos)) 
            y_pos += 40
            sorted_scores = sorted(high_scores.items(), key=lambda x: x[1][0], reverse=True)[:5]
            for name, (high_score, time) in sorted_scores: # Top 5 scores
                score_entry = font.render(f"{name}: {high_score} ({time})", True, WHITE)
                screen.blit(score_entry, (WINDOW_WIDTH//2 - score_entry.get_width()//2, y_pos))
                y_pos += 40 

        pygame.display.flip() # Update screen
        clock.tick(60) # 60 FPS

# Main loop to handle restarts
play_again = True
while play_again:
    play_again = run_game()

pygame.quit()