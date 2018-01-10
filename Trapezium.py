from TransformMatrix import TransMatrix
import numpy as np


class Trapezium(TransMatrix):
    """
    This class stores for object from the class transform Matrix
    every class is a point of a trapizium

    -------------------------------------

    front_left-----------front_right
    \              |             /
     \             |             /
      \                        /
       \                      /
        back_left---back_right
                   |
                   x-axis
---------y-axis----
    """

    def __init__(self, front=(0, 0, 0), back=(0, 0, 0)):
        self.front_left = TransMatrix(x=front[0], y=front[1], z=front[2])
        self.front_right = TransMatrix(x=front[0], y=-front[1], z=front[2])
        self.back_left = TransMatrix(x=back[0], y=back[1], z=back[2])
        self.back_right = TransMatrix(x=back[0], y=-back[1], z=back[2])
        self.trap = [self.front_left, self.front_right, self.back_right, self.back_left]

    # get all the x cooridnates of the points in this class
    def get_all_x(self):
        all_x = np.array([self.front_left.get_x(),
                          self.front_right.get_x(),
                          self.back_right.get_x(),
                          self.back_left.get_x()])
        return all_x

    # get all the y cooridnates of the points in this class
    def get_all_y(self):
        all_y = np.array([self.front_left.get_y(),
                          self.front_right.get_y(),
                          self.back_right.get_y(),
                          self.back_left.get_y()])
        return all_y

    # get all the z cooridnates of the points in this class
    def get_all_z(self):
        all_z = np.array([[self.front_left.get_z(),
                           self.front_right.get_z(),
                           self.back_right.get_z(),
                           self.back_left.get_z()]])
        return all_z

    # get all the x cooridnates as a loop of the points in this class
    def get_wireframe_x(self):
        wire_x = np.array([self.front_left.get_x(),
                           self.front_right.get_x(),
                           self.back_right.get_x(),
                           self.back_left.get_x(),
                           self.front_left.get_x()])
        return wire_x

    # get all the y cooridnates as a loop of the points in this class
    def get_wireframe_y(self):
        wire_y = np.array([self.front_left.get_y(),
                           self.front_right.get_y(),
                           self.back_right.get_y(),
                           self.back_left.get_y(),
                           self.front_left.get_y()])
        return wire_y

    # get all the z cooridnates as a loop of the points in this class
    def get_wireframe_z(self):
        wire_z = np.array([self.front_left.get_z(),
                           self.front_right.get_z(),
                           self.back_right.get_z(),
                           self.back_left.get_z(),
                           self.front_left.get_z()])
        return wire_z

    def rotate_trap_z(self, theta=0):

        for point in self.trap:
            point.z_rotate(theta)




if __name__ == "__main__":
    pass
