from pyray import check_collision_point_rec, measure_text,  Vector2, Rectangle, draw_texture, draw_text, WHITE, GRAY

class Button ():
    def __init__(self, x, y, width, height, texture, description):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.texture = texture

        self.description = description

        self.hoverd = False
        self.clicked = False

    def update(self, Mouse_x, Mouse_y, clicked_status):
        if check_collision_point_rec(Vector2(Mouse_x, Mouse_y), Rectangle(self.x, self.y, self.width, self.height)):
            if clicked_status:
                self.hoverd = False
                self.clicked = True

            else:
                self.hoverd = True
                self.clicked = False

        else:
            self.hoverd = False
            self.clicked = False

    def draw_btn(self):
        if not self.clicked and not self.hoverd:
            draw_texture(self.texture, self.x, self.y, WHITE)

        if self.hoverd:
            draw_texture(self.texture, self.x, self.y, WHITE)
            draw_text(self.description, self.x + self.width // 2 - 10, self.y + self.height + 3, 12, WHITE)

        if self.clicked:
            self.clicked = False

class Label_Button:
    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y

        self.text = text
        self.fontsize = fontsize

        self.width = measure_text(self.text, self.fontsize)
        self.height = 35

        self.hasclicked = False
        self.click_time = 0
        self.hoverd = False
        self.clicked = False

    def update(self, Mouse_x, Mouse_y, clicked_status):
        if check_collision_point_rec(Vector2(Mouse_x, Mouse_y), Rectangle(self.x, self.y, self.width, self.height)):
            if clicked_status:
                self.hoverd = False
                self.clicked = True

                self.click_time += 1

            else:
                self.hoverd = True
                self.clicked = False

                self.click_time = 0

        else:
            self.hoverd = False
            self.clicked = False

            self.click_time = 0

        if self.click_time == 1:
            self.hasclicked = True

        else:
            self.hasclicked = False

        
    def draw_lable_btn (self):
        if not self.clicked and not self.hoverd:
            draw_text(self.text, self.x, self.y, self.fontsize, WHITE)

        if self.hoverd:
            draw_text(self.text, self.x, self.y, self.fontsize, GRAY)

        if self.clicked:
            self.clicked = False       