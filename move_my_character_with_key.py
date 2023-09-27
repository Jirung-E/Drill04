from pico2d import *

from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class State:
    def __init__(self, img):
        self.image: Image = img
        self.direction = 0
        self.frame_delay = 0.05
        self.frame = 0
        self.size = 3
        
    def animation(self, x, y):
        pass

class IdleState(State):
    def __init__(self, img):
        super().__init__(img)
        self.frame_delay = 0.1
        self._clip_points: List[Point] = [Point(229, 306), Point(255, 307), Point(284, 308), 
                                          Point(316, 308), Point(344, 309), Point(374, 309),]
        self._clip_width = [25, 26, 26, 25, 24, 24]
        self._clip_height = [47, 47, 47, 47, 46, 46]

    def animation(self, x, y):
        if self.direction >= 0:
            self.image.clip_draw(
                self._clip_points[self.frame].x, 
                self._clip_points[self.frame].y, 
                self._clip_width[self.frame], 
                self._clip_height[self.frame], 
                x, 
                y, 
                self._clip_width[self.frame] * self.size, 
                self._clip_height[self.frame] * self.size
            )
        else:
            self.image.clip_composite_draw(
                self._clip_start_point.x + self.frame * self._clip_size_width, 
                self._clip_start_point.y + self.frame * self._clip_size_height, 
                self._clip_size_width, 
                self._clip_size_height, 
                0, 
                'h', 
                x, 
                y, 
                self._clip_size_width * self.size, 
                self._clip_size_height * self.size
            )
        self.frame = (self.frame + 1) % len(self._clip_points)


class Character:
    def __init__(self, img):
        self.image: Image = img
        self.x, self.y = BACKGROUND_X, BACKGROUND_Y
        self.state: State = IdleState(self.image)

    def draw(self):
        self.state.animation(self.x, self.y)


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 1024
BACKGROUND_X = WINDOW_WIDTH // 2
BACKGROUND_Y = WINDOW_HEIGHT // 2

open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)

character_img = load_image('character.png')
background_img = load_image('TUK_GROUND.png')

character = Character(character_img)


while True:
    clear_canvas()

    background_img.draw(BACKGROUND_X, BACKGROUND_Y)
    character.draw()

    update_canvas()

    delay(character.state.frame_delay)



close_canvas()