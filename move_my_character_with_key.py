from pico2d import *


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 1024
open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)

character = load_image('character.png')
background = load_image('TUK_GROUND.png')

frame_delay = 0.05


while True:
    clear_canvas()
    background.draw(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
    update_canvas()
    delay(frame_delay)



close_canvas()