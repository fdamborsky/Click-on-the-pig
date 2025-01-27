
# Click on the pig! 

## Description:

"Click on the Pig!" is a simple game where the player's objective is to click on a moving green pig character that appears on the screen.

## Gameplay:

1. **Objective**: The main objective of the game is to click on the green pig character as it moves around the screen.

2. **Scoring**: Each successful click on the green pig earns the player points, increasing their score. The player's score is displayed prominently on the screen.

3. **Lives**: The player starts with a certain number of lives, typically five, which are displayed on the screen. Clicking on incorrect elements or failing to click on the pig deducts one life.

4. **Obstacles**: Apart from the pig, there may be other elements on the screen that the player must avoid clicking on. Clicking on these obstacles deducts lives from the player.

5. **Speed and Difficulty**: As the game progresses, the green pig's movement speed increases, making it more challenging for the player to click on it accurately. Additionally, the game may introduce more obstacles or increase their frequency.

6. **Game Over**: The game ends when the player runs out of lives. A game over screen is displayed, allowing the player to either quit or restart the game.

Features:

- **Dynamic Environment**: The game provides a dynamic environment with a moving green pig character and various interactive elements.

- **Responsive Controls**: Players can easily interact with the game using simple mouse clicks.

- **Audio Feedback**: Engaging sound effects enhance the gaming experience, providing feedback for successful clicks, failures, and game over scenarios.

- **Scoring System**: The game keeps track of the player's score, motivating them to achieve higher scores with each playthrough.

- **Adaptive Difficulty**: The game's difficulty increases gradually as the player progresses, providing a suitable challenge for both beginners and experienced players.




## Screenshot:

![App Screenshot](https://github.com/fdamborsky/Click-on-the-pig/blob/main/screenshot.png?raw=true)


## Code:

### Initialization

```
width = root.winfo_screenwidth()//1.5
height = root.winfo_screenheight()//1.5

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Click on the pig!")
```

- game opens in 2/3 of screen size

=> Then there is setting which i think you can understand

### Game start

```
# - Main cycle
gamerunning = True
while gamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerunning = False
```

- variable `gamerunning` will be created and will be set to `True` in order to run the game after python file starts

### Collision with the pig
- first we will get position mouse of when click happened
```
click_x = event.pos[0]
click_y = event.pos[1]
```
- then we'll use built-in fuction `greenpig_rect.collidepoint(click_x,click_y` that checks if point of click was inside of `greenpig_rect` and changes some game stats.

```
while previous_greenpig_x == greenpig_x and previous_greenpig_y == greenpig_y:
                    greenpig_x = random.choice([-1,1])
                    greenpig_y = random.choice([-1,1])
```

- this ensures that after you click on the pig in changes direction of pig movement


### Fullscreen
```
if event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1]
            if fullscreen_rect.collidepoint(click_x,click_y) and fullscreen_number == 0:
```

- if event of mouse click (right, left or middle) is registered then we'll save info to the variables of `click_x` and `click_y`
- right after we check if point of click collided with position with fullscreen button and if fullscreen is set to OFF

```
width = int(root.winfo_screenwidth())
height = int(root.winfo_screenheight())

# SET FULL SCREEN
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
background_image = pygame.image.load(r"images/background 1920x1080.jpg")
```

### Pig movement
- Because whole game is in `while` loop we use simple code to make pig move:

```
greenpig_rect.x += (greenpig_x) * greenpig_speed
greenpig_rect.y += (greenpig_y) * greenpig_speed
```
- `greenpig_x` or `greenpig_y` haves value of 1 or -1 and we multiply it with value `greenpig_speed` that increases everytime we hit pig

### Pig bouce
- if pig hits top, bottom , left or right we set that value to zero to prevent pig going off the screen
- then we set greenpig_x/y to 1 or 2 through `random.choice([1,-1])`

### Lives ran out
- on the end of each cycle we check if lives didn't ran out, if they do we display text that says that we need to pres space to continue

### Screen update
- at end of each loop we update display at the rate of 60 fps
```
pygame.display.update()
time.tick(fps)
```
