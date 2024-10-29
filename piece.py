from constants import piece_shape

PIECE_SIZE = 20

colors = {
    "red": (255, 0, 0)
}

class Piece:
    def __init__(self):
        self.shape = "S"
        self.x = 0
        self.y = 0
    def get_pos(self):
        result = []
        for row, l in enumerate(piece_shape[self.shape]):
            for column, val in enumerate(l):
                if val != 0:
                    result.append([row+self.x, column+self.y, val])
        return result
    
if __name__ == "__main__":
    pic = Piece()
    points = pic.get_pos()
