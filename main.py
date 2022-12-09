import pyray as pr 
from transform import Block

pr.init_window(720, 1080, "SanBoxy")

Blocks = []

pr.set_target_fps(30)

while not pr.window_should_close():
    if pr.is_mouse_button_down(0):
        x = pr.get_mouse_x() 
        y = pr.get_mouse_y() 

        x -= x % 5
        y -= y % 5

        occupied = False

        for b in Blocks:
            if b.x == x and b.y == y:
                occupied = True

        if not occupied:
            Blocks.append(Block(x, y, 'Sand'))


    pr.clear_background(pr.BLACK)

    pr.begin_drawing()

    for b in Blocks:
        b.update(Blocks)

        if b.mat == 'Sand':
            pr.draw_rectangle(b.x, b.y, 5, 5, pr.Color(255, 189, 115, 255))

    pr.draw_text(str(pr.get_fps()), 50, 50, 22, pr.BLUE)

    pr.end_drawing()