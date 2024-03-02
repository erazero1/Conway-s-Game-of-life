import pygame
import os
import Mesh
import pygame_menu

os.environ["SDL_VIDEO_CENTERED"] = '1'

# resolution
width, height = 1280, 720
size = (width, height)

difficulty = "Easy"

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption(f"GAME OF LIFE")

black = (0, 0, 0)
color_of_cube = (47, 86, 233)
white = (255, 255, 255)

scaler = 20  # Размер клеток
offset = 1

Mesh = Mesh.Mesh(width, height, scaler, offset)
Mesh.random2d_array()


def start_game():
    Mesh.random2d_array()
    fps = 26
    pygame.mixer_music.load("sound/background_music.mp3")
    pygame.mixer_music.play(-1)
    pause = False
    run = True
    while run:
        pygame.display.update()
        pygame.display.set_caption(f"GAME OF LIFE FPS:{fps}")
        clock.tick(fps)
        screen.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                Mesh.HandleMouse(mouseX, mouseY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_g:
                    Mesh.random2d_array()
                if event.key == pygame.K_c:
                    Mesh.clear_arr()
                if event.key == pygame.K_LEFT:
                    print("LEFT KEY")
                    Mesh.Conway(off_color=white, on_color=color_of_cube, surface=screen, pause=False)
                    Mesh.set_arr()
                    pygame.display.update()
                if event.key == pygame.K_RIGHT:
                    print("RIGHT KEY")
                    Mesh.Conway(off_color=white, on_color=color_of_cube, surface=screen, pause=False)
                    pygame.display.update()
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    pause = not pause
                if event.key == pygame.K_UP:
                    if fps + 5 > 56:
                        fps = 56
                    else:
                        fps += 5
                if event.key == pygame.K_DOWN:
                    if fps - 5 < 0:
                        fps = 1
                    else:
                        fps -= 5
        Mesh.add_arr()
        Mesh.Conway(off_color=white, on_color=color_of_cube, surface=screen, pause=pause)

        pygame.display.update()


menu = pygame_menu.Menu('Game of Life', 400, 300,
                        theme=pygame_menu.themes.THEME_DARK)

background = pygame_menu.BaseImage(image_path="img/background.jpg")
# menu.add.selector('Difficulty :', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)
menu.add.button('Play', start_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


def main_background():
    background.draw(surface=screen)


menu.mainloop(screen, main_background)
pygame.quit()
