"""The required implementation of sparse matrix"""
class SparseList:
    def __init__(self, rows=0, columns=0, values=None):
        self.rows = rows
        self.columns = columns
        self.values = values
        if values is None:
            self.values = [[]]

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return None
        else:
            pass

    def insert(self, value, line, column):
        if line > self.rows:
            for i in range(line - self.rows):
                self.values.append([])
            self.rows = line
        if column > self.columns:
            self.columns = column
        if line == column:
            self.values[line].append((value, column))
        else:
            self.values[line].insert(0, (value, column))


class SparseCSR:
    """An implementation of Compressed sparse row sparse matrix"""
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.values = []
        self.column_idx = []
        self.row_start = []

