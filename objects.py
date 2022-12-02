class Sqr ():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.type = 'Sqr'

        self.color = color

    def update(self, Objects, msAllObjects):

        if (self.x, self.y + 5) in Objects:
            if Objects[self.x, self.y + 5][1]:
                self.y += 5

                Objects[self.x, self.y - 5] = (self, True)
                Objects[self.x, self.y] = (self, False)

class Wall ():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y

        self.type = 'wall'

        self.color = color

    def update (self, Objects, msAllObjects):
        pass

class Wood ():
    def __init__(self, x, y, color, burning_rate):
        self.x = x
        self.y = y

        self.type = 'wood'
        self.burning_rate = burning_rate

        self.color = color

    def update (self, Objects, msAllObjects):
        pass

class Lava ():
    def __init__(self, x, y, color, hot):
        self.x = x
        self.y = y

        self.type = 'lava'
        self.hot = hot

        self.color = color

        self.density = 3

        self.right_occupied = False
        self.left_occupied = True

        self.moved = False
        self.moved_dt = 0

    def update (self, Objects, msAllObjects):
        # Down
        if (self.x, self.y + 5) in Objects:
            if Objects[self.x, self.y + 5][1]:
                self.y += 5

                Objects[self.x, self.y - 5] = (self, True)
                Objects[self.x, self.y] = (self, False)

            else:
                # Right

                if not self.moved:
                    if not self.right_occupied:
                        if (self.x + 5, self.y) in Objects:
                            if Objects[self.x + 5, self.y][1]:
                                self.x += 5

                                Objects[self.x - 5, self.y] = (self, True)
                                Objects[self.x, self.y] = (self, False)

                                self.moved = True

                            else:
                                self.right_occupied = True
                                self.left_occupied = False

                        else:
                            self.right_occupied = True
                            self.left_occupied = False

                    # Left
                    elif not self.left_occupied:
                        if (self.x - 5, self.y) in Objects:
                            if Objects[self.x - 5, self.y][1]:
                                self.x -= 5

                                Objects[self.x + 5, self.y] = (self, True)
                                Objects[self.x, self.y] = (self, False)

                                self.moved = True

                            else:
                                self.left_occupied = True
                                self.right_occupied = False                        

                        else:
                            self.left_occupied = True
                            self.right_occupied = False

                else:
                    if self.moved_dt < 3:
                        self.moved_dt += 0.1

                    else:
                        self.moved_dt = 0
                        self.moved = False

        # find objects around 

        if (self.x, self.y + 5) in Objects:
            if not Objects[self.x, self.y + 5][1]:
                if Objects[self.x, self.y + 5][0].type == 'wood':
                    Obj = Objects[self.x, self.y + 5][0]
                    Obj.burning_rate += 0.1

                    if Obj.burning_rate >= 1 and Obj.burning_rate < 2:
                        Obj.color = (174, 24, 13, 255)

                    elif Obj.burning_rate >= 2 and Obj.burning_rate < 3:
                        Obj.color = (209, 57, 19, 255)

                    elif Obj.burning_rate >= 3:

                        Obj = Lava(Obj.x, Obj.y, (255, 144, 1, 255), 5)

                        msAllObjects.remove(Objects[self.x, self.y + 5][0])
                        Objects[self.x, self.y + 5] = Lava(Obj.x, Obj.y, (255, 144, 1, 255), 5), False
                        msAllObjects.append(Obj)

                        


        if (self.x, self.y - 5) in Objects:
            if not Objects[self.x, self.y - 5][1]:
                if Objects[self.x, self.y - 5][0].type == 'wood':
                    Obj = Objects[self.x, self.y - 5][0]

                    Obj.burning_rate += 0.1

                    if Obj.burning_rate >= 1 and Obj.burning_rate < 2:
                        Obj.color = (174, 24, 13, 255)

                    elif Obj.burning_rate >= 2 and Obj.burning_rate < 3:
                        Obj.color = (209, 57, 19, 255)

                    elif Obj.burning_rate >= 3:
                        Obj = Lava(Obj.x, Obj.y, (255, 144, 1, 255), 5)

                        msAllObjects.remove(Objects[self.x, self.y - 5][0])
                        Objects[self.x, self.y - 5] = Lava(Obj.x, Obj.y, (255, 144, 1, 255), 5), False
                        msAllObjects.append(Obj) 

        if (self.x - 5, self.y) in Objects:
            if not Objects[self.x - 5, self.y][1]:
                if Objects[self.x - 5, self.y][0].type == 'wood':
                    Obj = Objects[self.x - 5, self.y][0]

                    Obj.burning_rate += 0.1

                    if Obj.burning_rate >= 1 and Obj.burning_rate < 2:
                        Obj.color = (174, 24, 13, 255)

                    elif Obj.burning_rate >= 2 and Obj.burning_rate < 3:
                        Obj.color = (209, 57, 19, 255)

                    elif Obj.burning_rate >= 3:
                        
                        Obj = Lava(Obj.x, Obj.y, (255, 144, 1, 255), 5)

                        msAllObjects.remove(Objects[self.x - 5, self.y][0])
                        Objects[self.x - 5, self.y] = Lava(Obj.x, Obj.y, (255, 144, 1, 255), 5), False
                        msAllObjects.append(Obj)

        if (self.x + 5, self.y) in Objects:
            if not Objects[self.x + 5, self.y][1]:
                if Objects[self.x + 5, self.y][0].type == 'wood':
                    Obj = Objects[self.x + 5, self.y][0]

                    Obj.burning_rate += 0.1

                    if Obj.burning_rate >= 1 and Obj.burning_rate < 2:
                        Obj.color = (174, 24, 13, 255)

                    elif Obj.burning_rate >= 2 and Obj.burning_rate < 3:
                        Obj.color = (209, 57, 19, 255)

                    elif Obj.burning_rate >= 3:

                        Obj = Lava(Obj.x, Obj.y, (255, 144, 1, 255), 5)

                        msAllObjects.remove(Objects[self.x + 5, self.y][0])
                        Objects[self.x + 5, self.y] = Lava(Obj.x, Obj.y, (255, 144, 1, 255), 5), False
                        msAllObjects.append(Obj)

class Liquid ():
    def __init__(self, x, y, color, density):
        self.x = x
        self.y = y
        self.color = color

        self.type = 'liquid'

        self.density = density

        self.right_occupied = False
        self.left_occupied = True

    def update(self,  Objects, msAllObjects):
        # Down
        if (self.x, self.y + 5) in Objects:
            if Objects[self.x, self.y + 5][1]:
                self.y += 5

                Objects[self.x, self.y - 5] = (self, True)
                Objects[self.x, self.y] = (self, False)

            else:
                # Right

                if not self.right_occupied:
                    if (self.x + 5, self.y) in Objects:
                        if Objects[self.x + 5, self.y][1]:
                            self.x += 5

                            Objects[self.x - 5, self.y] = (self, True)
                            Objects[self.x, self.y] = (self, False)

                        else:
                            self.right_occupied = True
                            self.left_occupied = False

                    else:
                        self.right_occupied = True
                        self.left_occupied = False

                # Left
                elif not self.left_occupied:
                    if (self.x - 5, self.y) in Objects:
                        if Objects[self.x - 5, self.y][1]:
                            self.x -= 5

                            Objects[self.x + 5, self.y] = (self, True)
                            Objects[self.x, self.y] = (self, False)

                        else:
                            self.left_occupied = True
                            self.right_occupied = False                        

                    else:
                        self.left_occupied = True
                        self.right_occupied = False

class Sand ():
    def __init__ (self, x, y, color):
        self.x = x
        self.y = y
        self. color = color

        self.type = 'sand'

    def update(self,  Objects, msAllObjects):
        # Moving Down 
        if (self.x, self.y + 5) in Objects:
            if Objects[self.x, self.y + 5][1]:
                self.y += 5

                Objects[self.x, self.y - 5] = (self, True)
                Objects[self.x, self.y ] = (self, False)

            # Left
            elif (self.x - 5, self.y + 5) in Objects:
                if Objects[self.x - 5, self.y + 5][1]:
                    self.x -= 5 
                    self.y += 5

                    Objects[self.x + 5, self.y - 5] = (self, True)
                    Objects[self.x, self.y] = (self, False)


                # Right
                elif (self.x + 5, self.y + 5) in Objects:

                    if Objects[self.x + 5, self.y + 5][1]:
                        self.x += 5
                        self.y += 5 

                        Objects[self.x - 5, self.y - 5] = (self, True)
                        Objects[self.x, self.y] = (self, False)
