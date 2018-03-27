import copy

epsilon = 10e-10


"""The required implementation of sparse matrix"""
class SparseList:
    def __init__(self, rows=0, columns=0, values=None):
        self.rows = rows
        self.columns = columns
        self.values = values
        if values is None:
            self.values = [[]]

    def __eq__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return False
        for line in range(0, self.rows+1):
            if len(self.values[line]) != len(other.values[line]):
                return False
            self.values[line] = sorted(self.values[line], key=lambda entry: entry[1])
            other.values[line] = sorted(other.values[line], key=lambda entry: entry[1])
            for column in range(0, len(self.values[line])):
                if self.values[line][column][1] != other.values[line][column][1]:
                    return False
                if abs(self.values[line][column][0] - other.values[line][column][0]) > epsilon:
                    return False
        return True

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return None
        else:
            values = [x[:] for x in self.values]
            for i in range(0, self.rows+1):
                if other.values[i]:
                    for j in range(0, len(other.values[i])):
                        found = False
                        for k in range(0, len(values[i])):
                            if values[i][k][1] == other.values[i][j][1]:
                                values[i][k] = (values[i][k][0] + other.values[i][j][0], values[i][k][1])
                                found = True
                                break
                        if not found:
                            values[i].insert(0, other.values[i][j])
            return SparseList(self.rows, self.columns, values)

    def __mul__(self, other):
        if self.columns != other.rows:
            return None

        result = SparseList()

        for i in range(0, self.rows+1):
            for j in range(0, len(self.values[i])):
                entry = self.values[i][j]
                for k in range(0, len(other.values[entry[1]])):
                    result.insert(other.values[entry[1]][k][0] * entry[0], i, other.values[entry[1]][k][1])
        return result

    def __rmul__(self, other: []):
        if len(other) != self.rows+1:
            return None
        else:
            result = []
            for i in range(0, self.rows+1):
                value = 0
                for entry in self.values[i]:
                    value += entry[0] * other[entry[1]]
                result.append(value)
            return result

    def insert(self, value, line, column):
        if line > self.rows:
            for i in range(line - self.rows):
                self.values.append([])
            self.rows = line
        if column > self.columns:
            self.columns = column
        for i in range(0, len(self.values[line])):
            if self.values[line][i][1] == column:
                self.values[line][i] = (self.values[line][i][0] + value, self.values[line][i][1])
                return
        self.values[line].append((value, column))
