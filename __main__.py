# Code by Giv Sharifi
# sharifigiv5954@gmail.com
# 2022

# Imports
import pyray as pr
import objects as obj
import build as b

from lib.ui import Button, Label_Button

import time

# Consts
Screen_width = 1680
Screen_height = 1050

BackGround_color = pr.BLACK

# Vars
mAllObjects = {}
msAllObjects = []

Mode = ''

Brush_size = 1
Speed_text = 'x1'

clicked_status = False
X = 0
Y = 0

# InIt
pr.init_window(Screen_width, Screen_height, "Sandboxy")
icon = pr.load_image('assets/icon/icon2.png')

pr.set_window_icon(icon)

start_time = time.time()
mAllObjects = b.build()


# Load Textures
Water_img = pr.load_image('assets/gfx/water.png')
Lava_img = pr.load_image('assets/gfx/lava.png')
Wood_img = pr.load_image('assets/gfx/wood.png')
Stone_img = pr.load_image('assets/gfx/stone.png')
Wall_img  = pr.load_image('assets/gfx/wall.png')
Sand_img = pr.load_image('assets/gfx/sand.png')

pr.image_resize(Water_img, Water_img.width // 2, Water_img.height // 2)
pr.image_resize(Lava_img, Lava_img.width // 2, Lava_img.height // 2)
pr.image_resize(Wood_img, Wood_img.width // 4, Wood_img.height // 4)
pr.image_resize(Stone_img, int(Stone_img.width // 4.5), int(Stone_img.height // 4.5))
pr.image_resize(Wall_img, int(Wall_img.width // 1.4), int(Wall_img.height // 1.4))
pr.image_resize(Sand_img, int(Sand_img.width // 2.1), int(Sand_img.height // 2.1))

Water_tx = pr.load_texture_from_image(Water_img)
Lava_tx = pr.load_texture_from_image(Lava_img)
Wood_tx = pr.load_texture_from_image(Wood_img)
Stone_tx = pr.load_texture_from_image(Stone_img)
Wall_tx = pr.load_texture_from_image(Wall_img)
Sand_tx = pr.load_texture_from_image(Sand_img)

pr.unload_image(Water_img)
pr.unload_image(Lava_img)
pr.unload_image(Wood_img)
pr.unload_image(Stone_img)
pr.unload_image(Wall_img)
pr.unload_image(Sand_img)

font = pr.load_font('assets/fonts/font.otf')

# Gui 
Water_btn = Button(15, 50, Water_tx.width, Water_tx.height, Water_tx, 'Water')
Lava_btn = Button(15, Water_tx.height + 80, Lava_tx.width, Lava_tx.height, Lava_tx, 'Lava')
Wood_btn = Button(25, Water_tx.height + Lava_tx.height + 60 + 65, Wood_tx.width, Wood_tx.height, Wood_tx, 'Wood')
Stone_btn = Button(4, Water_tx.height + Lava_tx.height + 60 + 66 + 115, Stone_tx.width, Stone_tx.height, Stone_tx, 'Stone')
Wall_btn  = Button(25, Water_tx.height + Lava_tx.height + 60 + 66 + 115 + 300, Wall_tx.width, Wall_tx.height, Wall_tx, 'Wall')
Sound_btn = Button(15, Water_tx.height + Lava_tx.height + 60 + 66 + 115 + 100, Sand_tx.width, Sand_tx.height, Sand_tx, 'Sand')

Speed_lb_btn = Label_Button(50, 900, Speed_text, 35)

# Main Loop
while not pr.window_should_close():
    # 1. Input

    if pr.is_mouse_button_down(0):
        clicked_status = True

        X = pr.get_mouse_x()
        X -= X % 5

        Y = pr.get_mouse_y()
        Y -= Y % 5 

        if (X, Y) in mAllObjects:
            if mAllObjects[(X, Y)][1]:
                if Mode == 'Stone':
                    OBJ = obj.Sqr(X, Y, (175, 167, 161, 255))
                    mAllObjects[X, Y] = (OBJ , False)
                    msAllObjects.append(OBJ)


                elif Mode == 'Wall':
                    OBJ = obj.Wall(X, Y, (94, 8, 19, 255))
                    mAllObjects[X, Y] = (OBJ , False)
                    msAllObjects.append(OBJ)


                elif Mode == 'Wood':
                    OBJ = obj.Wood(X, Y, (61, 20, 21, 255), 0)
                    mAllObjects[X, Y] = (OBJ , False)
                    msAllObjects.append(OBJ)


                elif Mode == 'Lava':
                    OBJ = obj.Lava(X, Y, (255, 144, 1, 255), 10)
                    mAllObjects[X, Y] = (OBJ , False)
                    msAllObjects.append(OBJ)

                elif Mode == 'Water':
                    OBJ = obj.Liquid(X, Y, (39, 132, 245, 255), 1)
                    OBJ2 = obj.Liquid(X - 5, Y, (39, 132, 245, 255), 1)
                    OBJ3 = obj.Liquid(X + 5, Y, (39, 132, 245, 255), 1)
                    OBJ4 = obj.Liquid(X, Y + 5, (39, 132, 245, 255), 1)
                    OBJ5 = obj.Liquid(X, Y - 5, (39, 132, 245, 255), 1)

                    mAllObjects[X, Y] = (OBJ , False)
                    mAllObjects[X - 5, Y] = (OBJ2 , False)
                    mAllObjects[X + 5, Y] = (OBJ3 , False)
                    mAllObjects[X, Y - 5] = (OBJ5 , False)
                    mAllObjects[X, Y + 5] = (OBJ4 , False)

                    msAllObjects.append(OBJ)
                    msAllObjects.append(OBJ2)
                    msAllObjects.append(OBJ3)
                    msAllObjects.append(OBJ4)
                    msAllObjects.append(OBJ5)

                elif Mode == 'Sand':
                    for i in range (1, Brush_size + 1):
                        OBJ = obj.Sand(X, Y, (255, 189, 115, 255))
                        OBJ2 = obj.Sand(X - 5 * i, Y, (247, 160, 62, 255))
                        OBJ3 = obj.Sand(X + 5 * i, Y, (255, 189, 115, 255))
                        OBJ4 = obj.Sand(X, Y + 5 * i,  (247, 160, 62, 255))
                        OBJ5 = obj.Sand(X, Y - 5 * i, (255, 189, 115, 255))

                        mAllObjects[X, Y] = (OBJ , False)
                        mAllObjects[X - 5 * i, Y] = (OBJ2 , False)
                        mAllObjects[X + 5 * i, Y] = (OBJ3 , False)
                        mAllObjects[X, Y - 5 * i] = (OBJ5 , False)
                        mAllObjects[X, Y + 5 * i] = (OBJ4 , False)

                        msAllObjects.append(OBJ)
                        msAllObjects.append(OBJ2)
                        msAllObjects.append(OBJ3)
                        msAllObjects.append(OBJ4)
                        msAllObjects.append(OBJ5)
           
    elif pr.is_mouse_button_down(1):

        X = pr.get_mouse_x()
        X -= X % 5

        Y = pr.get_mouse_y()
        Y -= Y % 5 

        if (X, Y) in mAllObjects:
            if not mAllObjects[(X, Y)][1]:

                msAllObjects.remove(mAllObjects[X, Y][0])
                mAllObjects[X, Y] = ('null', True)

                time.sleep(0.01)

    else:
        clicked_status = False

    # 2. Process

    

    # 3. Draw
    pr.begin_drawing()

    pr.clear_background(BackGround_color)

    for x in msAllObjects:
        x.update(mAllObjects, msAllObjects)


        pr.draw_rectangle(x.x, x.y, 5,5 , pr.Color(x.color[0], x.color[1], x.color[2], x.color[3]))

    pr.draw_text(str(Mode), 35, 1000, 20, pr.Color(199, 198, 197, 255) )

    # Gui
    Mouse_pos = [pr.get_mouse_x(), pr.get_mouse_y()]

    Water_btn.update(Mouse_pos[0], Mouse_pos[1], clicked_status)
    Lava_btn.update(Mouse_pos[0], Mouse_pos[1], clicked_status)
    Wood_btn.update(Mouse_pos[0], Mouse_pos[1], clicked_status)
    Stone_btn.update(Mouse_pos[0], Mouse_pos[1], clicked_status)
    Wall_btn.update(Mouse_pos[0], Mouse_pos[1], clicked_status)
    Sound_btn.update(Mouse_pos[0], Mouse_pos[1], clicked_status)

    Speed_lb_btn.update(Mouse_pos[0], Mouse_pos[1], clicked_status)

    if Water_btn.clicked:
        Mode = 'Water'

    elif Lava_btn.clicked:
        Mode = 'Lava'

    elif Wood_btn.clicked:
        Mode = 'Wood'

    elif Stone_btn.clicked:
        Mode = 'Stone'

    elif Wall_btn.clicked:
        Mode = 'Wall'

    elif Sound_btn.clicked:
        Mode = 'Sand'

    if Speed_lb_btn.hasclicked:
        print(Speed_text[1])
        

        if int(Speed_text[1]) >= 4:
            Speed_text = 'x1'
            Speed_lb_btn.text = Speed_text

            pr.set_target_fps(60)

        else:
            Speed_text = 'x' + str(int(Speed_text[1]) * 2)
            Speed_lb_btn.text = Speed_text

            pr.set_target_fps(pr.get_fps() + 40)


    Water_btn.draw_btn()
    Lava_btn.draw_btn()
    Wood_btn.draw_btn()
    Stone_btn.draw_btn()
    Wall_btn.draw_btn()
    Sound_btn.draw_btn()

    Speed_lb_btn.draw_lable_btn()

    pr.draw_line(125, 0, 125, 1050, pr.GRAY)

    pr.end_drawing()

print('Process finished in --- %s seconds ---' % (time.time() - start_time))
pr.close_window()