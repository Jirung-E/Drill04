from pico2d import *

from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, rhs):
        return Point(self.x + rhs.x, self.y + rhs.y)

class Vector:   # 이름만 구분
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, rhs):
        return Vector(self.x * rhs, self.y * rhs)


class State:
    def __init__(self):
        self.frame_delay = 0.05
        self.frame = 0
        
    def animation(self, image: Image, x, y, flip=False, size=1):
        pass

class IdleState(State):
    def __init__(self):
        super().__init__()
        self.frame_delay = 0.1
        self._clip_points: List[Point] = [Point(229, 306), Point(255, 307), Point(284, 308), 
                                          Point(316, 308), Point(344, 309), Point(374, 310),
                                          Point(404, 309)]
        self._clip_width = [25, 26, 26, 25, 24, 25, 25]
        self._clip_height = [47, 47, 47, 47, 46, 46, 47]

    def animation(self, image: Image, x, y, flip, size):
        if flip == False:
            image.clip_draw(
                self._clip_points[self.frame].x, 
                self._clip_points[self.frame].y, 
                self._clip_width[self.frame], 
                self._clip_height[self.frame], 
                x, 
                y, 
                self._clip_width[self.frame] * size, 
                self._clip_height[self.frame] * size
            )
        else:
            image.clip_composite_draw(
                self._clip_points[self.frame].x, 
                self._clip_points[self.frame].y, 
                self._clip_width[self.frame], 
                self._clip_height[self.frame], 
                0,
                'h',
                x, 
                y,
                self._clip_width[self.frame] * size, 
                self._clip_height[self.frame] * size
            )
        self.frame = (self.frame + 1) % len(self._clip_points)


class Character:
    def __init__(self, image: Image):
        self.image: Image = image
        self.position: Point = Point(BACKGROUND_X, BACKGROUND_Y)
        self.direction: Vector = Vector(0, 0)
        self.flip = False
        self.size = 3
        self.state: State = IdleState()

    def draw(self):
        self.state.animation(self.image, self.position.x, self.position.y, self.flip, self.size)

    def update(self):
        self.position += self.direction * 5


WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 1024
BACKGROUND_X = WINDOW_WIDTH // 2
BACKGROUND_Y = WINDOW_HEIGHT // 2

open_canvas(WINDOW_WIDTH, WINDOW_HEIGHT)

character_img = load_image('character.png')
background_img = load_image('TUK_GROUND.png')

character = Character(character_img)
repeat = True

def handle_events():
    global character
    global repeat

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            repeat = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                repeat = False
            elif event.key == SDLK_LEFT:
                character.flip = True
                character.direction.x -= 1
            elif event.key == SDLK_RIGHT:
                character.flip = False
                character.direction.x += 1
            elif event.key == SDLK_UP:
                character.direction.y += 1
            elif event.key == SDLK_DOWN:
                character.direction.y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                character.direction.x += 1
            elif event.key == SDLK_RIGHT:
                character.direction.x -= 1
            elif event.key == SDLK_UP:
                character.direction.y -= 1
            elif event.key == SDLK_DOWN:
                character.direction.y += 1


while repeat:
    clear_canvas()

    background_img.draw(BACKGROUND_X, BACKGROUND_Y)
    character.draw()
    character.update()

    handle_events()
    update_canvas()

    delay(character.state.frame_delay)



close_canvas()