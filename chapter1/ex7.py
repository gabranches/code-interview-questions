class Matrix:

    def __init__(self, rows, cols):
        self.matrix = self._create_blank(rows, cols)
        self.rows = rows
        self.cols = cols


    def _create_blank(self, rows, cols):
        mat = []
        for i in xrange(0, rows):
            mat.append([])
            for j in xrange(0, cols):
                mat[i].append((i*cols)+(j)+1)
        return mat


    def print_matrix(self):
        for i in xrange(0, self.rows):
            output = '|'
            for j in xrange(0, self.cols):
                output += '  ' + str(self.matrix[i][j])
            output += '  |'
            print(output)


    def get_elem(self, row, col):
        return self.matrix[row-1][col-1]


    def rotate(self):
        new_mat = self._create_blank(self.cols, self.rows)
        for i in xrange(0, self.cols):
            for j in xrange(0, self.rows):
                new_mat[i][j] = self.matrix[self.rows-1-j][i]
        temp = self.cols
        self.cols = self.rows
        self.rows = temp
        self.matrix = new_mat


if __name__ == '__main__':
        
    a = Matrix(4,3)
    a.print_matrix()
    a.rotate()
    print('')
    a.print_matrix()



