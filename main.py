import pygame
import random

# - Inicialisation of game
pygame.init()

# - Window
width = 1600
height = 900
screen = pygame.display.set_mode((width,height))
#screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Click on the pig!")

# - icon
display_icon = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\greenpig.png")
pygame.display.set_icon(display_icon)

# - Game settings
time = pygame.time.Clock()
fps = 60
fullscreen_number = 0

# - Game values
start_lives = 5
lives = start_lives
score = 0
greenpig_starting_speed = 5
greenpig_speed = greenpig_starting_speed
greenpig_speed_acceleration = 0.5

# - Green pig random movement
greenpig_x = random.choice([-1,1])
greenpig_y = random.choice([-1,1])

# - Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkred = (220,0,0)

# - Fonts
AB_font_50 = pygame.font.Font(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\fonts\AngryBirds.ttf", 50)
AB_font_35 = pygame.font.Font(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\fonts\AngryBirds.ttf", 35)

# - Text
score_text = AB_font_35.render(f"Score: {score}", True, darkred)
score_rect = score_text.get_rect()
score_rect.center = ((width//2)-80,25)

lives_text = AB_font_35.render(f"Lives: {lives}", True, darkred)
lives_rect = lives_text.get_rect()
lives_rect.center = ((width//2)+70,25)

game_over_text = AB_font_50.render("GAME OVER", True, darkred)
game_over_rect = game_over_text.get_rect()

game_over_text = AB_font_50.render("GAME OVER", True, darkred)
game_over_rect = game_over_text.get_rect()
game_over_rect.midbottom = (width//2,height//2)

continue_text = AB_font_35.render("Pres SPACE to continue", True, darkred)
continue_rect = continue_text.get_rect()
continue_rect.midbottom = (width//2, (height//2)+70)

# - Sounds
succesful_hit = pygame.mixer.Sound(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\music\hitsound.wav")
succesful_hit.set_volume(0.1)
failed_hit = pygame.mixer.Sound(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\music\lifelost.wav")
failed_hit.set_volume(0.1)
lost_game = pygame.mixer.Sound(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\music\levelfailed.wav")
lost_game.set_volume(0.1)
pygame.mixer.music.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\music\AB_MainTheme.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1,0.0)


# - Images load
greenpig_image = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\greenpig.png")
greenpig_rect = greenpig_image.get_rect()
greenpig_rect.center = (width//2, height//2)

background_image = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\background.jpg")
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)

fullscreen_image = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\full screen.png")
fullscreen_rect = fullscreen_image.get_rect()
fullscreen_rect.bottomright = (width-10,height-10)

halfscreen_image = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\half screen.png")
halfscreen_rect = halfscreen_image.get_rect()
halfscreen_rect.bottomright = (width-10,height-10)

closebutton_image = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\close button.png")
closebutton_rect = closebutton_image.get_rect()
closebutton_rect.topright = (width-10, 10)

# - Main cycle
gamerunning = True
while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
        
    # - Click on pig checker
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]

            if greenpig_rect.collidepoint(click_x,click_y):
                succesful_hit.play(0)
                score += 1
                greenpig_speed += greenpig_speed_acceleration
                score_text = AB_font_35.render(f"Score: {score}", True, darkred)

                previous_greenpig_x = greenpig_x
                previous_greenpig_y = greenpig_y

                while previous_greenpig_x == greenpig_x and previous_greenpig_y == greenpig_y:
                    greenpig_x = random.choice([-1,1])
                    greenpig_y = random.choice([-1,1])

            else:
                if fullscreen_rect.collidepoint(click_x,click_y) or closebutton_rect.collidepoint(click_x,click_y):
                    pass
                else:
                    failed_hit.play(0)
                    lives -= 1
                    lives_text = AB_font_35.render(f"Lives: {lives}", True, darkred)

    # - Full screen
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]
            if fullscreen_rect.collidepoint(click_x,click_y) and fullscreen_number == 0:
                # SETTINGS
                fullscreen_number = 1
                fullscreen_image = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\full screen.png")
                width = 1920
                height = 1080
                # SET FULL SCREEN
                screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                background_image = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\background 1920x1080.jpg")
                    

                # IMAGES
                greenpig_rect.center = (width//2, height//2)
                background_rect.topleft = (0,0)
                fullscreen_rect.bottomright = (width-10,height-10)
                halfscreen_rect.bottomright = (width-10,height-10)
                closebutton_rect.topright = (width-10, 10)


                # TEXT
                score_rect.center = ((width//2)-80,25)
                lives_rect.center = ((width//2)+70,25)
                game_over_rect.midbottom = (width//2,height//2)
                continue_rect.midbottom = (width//2, (height//2)+70)
            
            # - Half screen
            elif fullscreen_rect.collidepoint(click_x,click_y) and fullscreen_number == 1:
                # SETTINGS
                fullscreen_number = 0
                fullscreen_image = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\full screen.png")
                width = 1600
                height = 900
                # SET FULL SCREEN
                screen = pygame.display.set_mode((width,height))
                background_image = pygame.image.load(r"C:\Users\Filip Damborský\Python\Kurz pro středně pokročílé\PyGame 2.0\images\background.jpg")
                    
                # IMAGES
                greenpig_rect.center = (width//2, height//2)
                background_rect.topleft = (0,0)
                fullscreen_rect.bottomright = (width-10,height-10)
                halfscreen_rect.bottomright = (width-10,height-10)
                closebutton_rect.topright = (width-10, 10)


                # TEXT
                score_rect.center = ((width//2)-80,25)
                lives_rect.center = ((width//2)+70,25)
                game_over_rect.midbottom = (width//2,height//2)
                continue_rect.midbottom = (width//2, (height//2)+70)

            # - Close button
            if closebutton_rect.collidepoint(click_x,click_y):
                gamerunning = False
            
    # - Pig movement
    greenpig_rect.x += (greenpig_x) * greenpig_speed
    greenpig_rect.y += (greenpig_y) * greenpig_speed

    # - Pig bounce
    if greenpig_rect.left < 0:
        greenpig_rect.left = 0
        greenpig_x = random.choice([1, -1])
    elif greenpig_rect.right > width:
        greenpig_rect.right = width
        greenpig_x = random.choice([1, -1])

    if greenpig_rect.top < 0:
        greenpig_rect.top = 0
        greenpig_y = random.choice([1, -1])
    elif greenpig_rect.bottom > height:
        greenpig_rect.bottom = height
        greenpig_y = random.choice([1, -1])



    # - Image blit
    screen.blit(background_image,background_rect)
    screen.blit(greenpig_image,greenpig_rect)
    screen.blit(fullscreen_image,fullscreen_rect)
    screen.blit(closebutton_image,closebutton_rect)

    # - Text blit
    screen.blit(score_text,score_rect)
    screen.blit(lives_text,lives_rect)
    
    # - Live check
    if lives <= 0 :
        lost_game.play(0)
        screen.blit(continue_text,continue_rect)
        screen.blit(game_over_text,game_over_rect)
        pygame.display.update()

        # - Game stop
        pygame.mixer.music.stop()
        pause = True
        while pause:
            # - play again?
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score = 0
                        lives = start_lives
                        greenpig_speed = greenpig_starting_speed
                        greenpig_rect.center = (width//2,height//2)
                        pause = False

                        greenpig_x = random.choice([-1,1])
                        greenpig_y = random.choice([-1,1])

                        lost_game.stop()
                        pygame.mixer.music.play()

                elif event.type == pygame.QUIT:
                    pause = False
                    gamerunning = False
    
    # - Display update
    pygame.display.update()
    time.tick(fps)

    


# - Ending of game
pygame.quit()
