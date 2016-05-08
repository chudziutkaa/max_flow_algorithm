import pprint

class Matrix(object):
    def __init__(self, row, column):
        self.row=row
        self.column=column
        self.matrix=[[0 for i in range(column)] for j in range(row)]
        for i in range(self.row):
            self.matrix[0][i]=i
        for j in range(self.column):
            self.matrix[j][0]=j
            