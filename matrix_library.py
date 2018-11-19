from random import *


class Matrix:

    def __init__(self, i, j):
        self.rows = i
        self.cols = j
        self.data = [[randint(1, 20) for i in range(j)] for i in range(i)]

    @staticmethod
    def show(matrix):
        print matrix.data

    @staticmethod
    def replace(matrix, i, j, num):
        # Matrix.show(matrix)
        for item in range(matrix.rows):
            for ja in range(matrix.cols):
                if item == i and ja == j:
                    matrix.data[i][j] = num
        return matrix.data

    @staticmethod
    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.cols):
            for j in range(self.rows):
                # print i, j
                # print "break"
                # # print result.data[i][j], self.data[j][i]
                result.data[i][j] = self.data[j][i]
        return result
        # I did this first try!!!!!!!!
        # result which is an transposed version of the matrix you put in
        # use a list comprehension to store the NEW transposed N-D array into a variable called data
        # replace result's data with the new variable data
        # return result
        # Matrix.show(self)
        # print "break"
        # result = Matrix(self.cols, self.rows)
        # result.data = [Matrix.replace(result, j, i, self.data[i][j]) for j in range(self.cols) for i in range(self.rows)]
        # Matrix.show(self)
        # return result

    @staticmethod
    def add(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
        return result

    @staticmethod
    def subtract(self, other):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[i][j] = self.data[i][j] - other.data[i][j]
        return result

    @staticmethod
    def dot(self, other):
        counter = 0
        count = 0
        add2 = []
        result = Matrix(self.rows, other.cols)
        if self.cols != other.rows:
            print "error, Size NOt right"
            return 0
        other = Matrix.transpose(other)
        for i in other.data:
            for j in self.data:
                for k, l in enumerate(i):
                    print j, l
                    if counter >= len(j):
                        counter = 0
                    add = l * j[counter]
                    print add
                    add2.append(add)
                    counter += 1
        print "break"
        print add2
        # counter = self.cols
        print counter
        for i in range(result.cols):
            for j in range(result.rows):
                # print result.data[j][i]
                new = add2[count:counter]
                # print counter, count
                print new
                print sum(new)
                result.data[j][i] = sum(new)
                count += self.cols
                counter += self.cols

        return result

    @staticmethod
    # Reuturns the negitive version of the matrix.
    def neg(self):
        print self.data
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = self.data[i][j] * -1
        return self.data

    @staticmethod
    # Multipys the matrix by a constant.
    def constant(self, con):
        print self.data
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = self.data[i][j] * con
        return self.data

    def set_data(self, data):
        self.data = data


M1 = Matrix(3, 1)
M2 = Matrix(1, 2)

M1.set_data([[-5], [6], [0]])
M2.set_data([[3, -1]])
# # M4 = Matrix.replace(M1, 1, 1, 33)
# # Matrix.show(M4)

M3 = Matrix.dot(M1, M2)
print "break"
Matrix.show(M1)
Matrix.show(M2)
Matrix.show(M3)

# M4 = Matrix.transpose(M1)
# Matrix.show(M1)
# Matrix.show(M4)
# Matrix.transpose(M1)
# # print(M1.add(M2))
# print Matrix.neg(M1)
