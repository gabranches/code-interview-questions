from ex7 import Matrix

class ZeroMatrix(Matrix):

    def set_null(self, row, col):

        for i in range(0, self.rows):
            self.matrix[i][col] = 0

        for i in range(0, self.cols):
            self.matrix[row][i] = 0

if __name__ == '__main__':
    
    a = ZeroMatrix(3,3)
    a.set_null(0,1)
    print('')
    a.print_matrix()


