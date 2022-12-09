class Block:
    def __init__(self, x, y, material):
        self.x, self.y = x, y
        self.mat = material

    def checkBlocks(self, Blocks, pos):
        for b in Blocks:
            if b.x == pos[0] and b.y == pos[1]:
                return False

        return True

    def update(self, Blocks):
        if self.y + 5 < 1080:
            if self.checkBlocks(Blocks, [self.x, self.y + 5]):
                self.y += 5

            elif self.x - 5 <= 720 and self.y + 5 <= 1080:
                if self.checkBlocks(Blocks, [self.x - 5, self.y + 5]):
                    self.x -= 5 
                    self.y += 5

                elif self.x + 5 <= 720 and self.y + 5 <= 1080:
                    if self.checkBlocks(Blocks, [self.x + 5, self.y + 5]):
                        self.x += 5
                        self.y += 5