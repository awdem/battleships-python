class Ship:
    def __init__(self, length=5, orientation=None, row=None, col=None):
        self.length = length
        self.orientation = orientation
        self.row = row
        self.col = col
    
    def covers(self, row, col):
        if self.orientation == "vertical":
            if col != self.col:
                return False
            return self.row <= row < self.length + self.row
        else:
            if row != self.row:
                return False
            return self.col <= col < self.length + self.col
        
    def __repr__(self):
        return f"Ship(length={self.length}, orientation={self.orientation}, row={self.row}, col={self.col})"
