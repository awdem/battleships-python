from lib.board import Board

class BoardFormatter():
    def __init__(self) -> None:
        pass

    def format(self, board):
        board_rows = []
        for row in range(1, board.rows + 1):
            row_cells = []
            for col in range(1, board.cols + 1):
                if board.ship_at(row, col):
                    row_cells.append("S")
                else:
                    row_cells.append(".")
            board_rows.append("".join(row_cells))
        return "\n".join(board_rows)
