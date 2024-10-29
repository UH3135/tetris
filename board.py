# 테트리스 행 열 갯수 설정
WIDTH = 10
HEIGHT = 20

class board:
    def __init__(self):
        self.board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def add_piece(self, points: list):
        for x, y, val in points:
            self.board[x][y] = val

    def show(self):
        for i in self.board:
            for j in i:
                print(j, end=" ")
            print()

if __name__ == "__main__":
    from piece import Piece
    pic = Piece()
    game_board = board()
    game_board.add_piece(pic.get_pos())
    game_board.show()
    