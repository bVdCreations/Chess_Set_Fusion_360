import numpy as np
import math


class TransMatrix:

    # noinspection PyTypeChecker
    def __init__(self, x=0, y=0, z=0, mode="1x4"):
        if mode == "1x4":
            self.trans_matrix = np.array([[x],
                                          [y],
                                          [z],
                                          [1]])
        elif mode == "4x4":
            self.trans_matrix = np.array([[1, 0, 0, x],
                                          [0, 1, 0, y],
                                          [0, 0, 1, z],
                                          [0, 0, 0, 1]])
        else:
            raise TypeError("mode can only be 1x4 or 4x4")

    def dot(self, other):
        return self.trans_matrix.dot(other.trans_matrix)

    def distance_between(self, other):
        return abs(other.get_coordinates()-self.get_coordinates())

    # print out the matrix
    def print_matrix(self):
        print("-" * 50)
        print(self.trans_matrix)
        print("-" * 50)

    # transforms the vector by x, y, and/or z and saves the result to it self
    def linear_move(self, x=0, y=0, z=0):
        self.trans_matrix = (np.array([[1, 0, 0, x],
                                       [0, 1, 0, y],
                                       [0, 0, 1, z],
                                       [0, 0, 0, 1]])).dot(self.trans_matrix)
        return self.trans_matrix

    # rotate around the X axis and saves the result to it self
    def x_rotate(self, alpha):
        self.trans_matrix = (np.array([[1, 0, 0, 0],
                                       [0, math.cos(alpha), - math.sin(alpha), 0],
                                       [0, math.sin(alpha), math.cos(alpha), 0],
                                       [0, 0, 0, 1]])).dot(self.trans_matrix)
        return self.trans_matrix

    # rotate around the Y axis and saves the result to it self
    def y_rotate(self, omega):
        self.trans_matrix = (np.array([[math.cos(omega), 0, math.sin(omega), 0],
                                       [0, 1, 0, 0],
                                       [-math.sin(omega), 0, math.cos(omega), 0],
                                       [0, 0, 0, 1]])).dot(self.trans_matrix)
        return self.trans_matrix

    # rotate around the Z axis and saves the result to it self
    def z_rotate(self, theta):
        self.trans_matrix = np.array([[math.cos(theta), - math.sin(theta), 0, 0],
                                      [math.sin(theta), math.cos(theta), 0, 0],
                                      [0, 0, 1, 0],
                                      [0, 0, 0, 1]]).dot(self.trans_matrix)
        return self.trans_matrix

    # return the x value
    def get_x(self):
        return self.trans_matrix[0][-1]

    # return the x value
    def get_y(self):
        return self.trans_matrix[1][-1]

    # return the x value
    def get_z(self):
        return self.trans_matrix[2][-1]

    # return a numpy list with [x , y , z] coordinates
    def get_coordinates(self, mode="numpy"):
        if mode == "numpy":
            return np.array([self.get_x(), self.get_y(), self.get_z()])
        elif mode == "tuple":
            return self.get_x(), self.get_y(), self.get_z()
        else:
            raise TypeError("mode is not reconnised")

if __name__ == "__main__":
    tm = TransMatrix(x=3, mode="4x4")
    pm = TransMatrix(x=-9, y=-20, mode="4x4")

    print(tm.dot(pm))

    print(tm.distance_between(pm))
