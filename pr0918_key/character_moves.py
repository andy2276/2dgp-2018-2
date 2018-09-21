from pico2d import *

speed = 3

def handle_events():
    global running
    global tx, ty
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False
        elif e.type == SDL_MOUSEMOTION:
            tx, ty = e.x, 600 - e.y

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

x, y = 800 // 2, 90
tx, ty = x, y
frame = 0
running = True
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    dx, dy = tx - x, ty - y
    dist = math.sqrt(dx ** 2 + dy ** 2)
    x += speed * dx / dist
    y += speed * dy / dist

    if dx < 0 and x < tx: x = tx
    if dx > 0 and x > tx: x = tx
    if dy < 0 and y < ty: y = ty
    if dy > 0 and y > ty: y = ty

    if (x,y) == (tx,ty):
        hide_cursor()
    else:
        show_cursor()
    frame = (frame + 1) % 8
    delay(0.01)

# fill here
    
close_canvas()
