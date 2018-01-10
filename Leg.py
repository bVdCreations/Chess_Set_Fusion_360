import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Trapezium import Trapezium
from TransformMatrix import TransMatrix
from ClassCircle import Circle2D
import math


class CreateLeg:

    def __init__(self, height, bottom_dia, top_dia, legs):
        self._height = height
        self._bottom_circle = bottom_dia
        self._top_circle = top_dia
        self._legs = legs
        self._modes = {"rotation mode": "normal", "parameter mode": "dubbel"}
        self._parameter_circles = list()
        self.create_parameter_circles()
        self._trap_list = list()
        self.calculate_trapezium_points()
        self._rad_list = list()
        self.create_rotation_interval_list()



    # this function creates a wireframe of the point in the list Trap_list
    def wireframe_plot(self):

        fig = plt.figure()

        # ax = fig.add_subplot(111, projection='3d')
        ax = Axes3D(fig)

        np_list_x = np.array([])
        np_list_y = np.array([])
        np_list_z = np.array([])

        # get all the point in a numpy array for the wireframe from
        for trap_object in self._trap_list:
            if trap_object == self._trap_list[0]:
                np_list_x = np.array([trap_object.get_wireframe_x()])
                np_list_y = np.array([trap_object.get_wireframe_y()])
                np_list_z = np.array([trap_object.get_wireframe_z()])
            elif trap_object != self._trap_list[0]:
                xtemp = np.array([trap_object.get_wireframe_x()])
                ytemp = np.array([trap_object.get_wireframe_y()])
                ztemp = np.array([trap_object.get_wireframe_z()])
                np_list_x = np.append(np_list_x, xtemp, axis=0)
                np_list_y = np.append(np_list_y, ytemp, axis=0)
                np_list_z = np.append(np_list_z, ztemp, axis=0)
            else:
                raise TypeError("This is not a list with object of the class Trapizium")

        # create the wire frame
        ax.plot_wireframe(np_list_x, np_list_y, np_list_z)
        # add labels to the axis of the wire frame
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.set_zlabel("Z axis")
        # plot the damn thing
        plt.show()

    def create_rotation_interval_list(self, begin_deg=0, end_deg=0, interval=0, mode="normal"):
        self._rad_list = list()
        if mode == "normal":
            for step in range(interval):
                self._rad_list.append((begin_deg+end_deg/interval*step)*2*math.pi/360)
        elif mode == "sinus":
            print("mode under constrution")
        else:
            raise TypeError("the mode's that can be used in this function are: normal and sinus")

    def new_path_rotation_z(self,begin_deg=0, end_deg=0, interval=0, mode="normal"):
        self.create_rotation_interval_list( begin_deg=begin_deg, end_deg=end_deg, interval=interval, mode=mode)

    def rotate_trapliste_z(self):
        for i in range(len(self._trap_list)):
            self._trap_list[i].rotate_trap_z(self._rad_list[i])

    def create_parameter_circles(self):
        if self._modes.get("parameter mode") == "single" or self._modes.get("parameter mode") == "dubbel" or \
                self._modes.get("parameter mode") == "trippel":
            # where we define the parameters of circle equation in x z plane
            # it starts at the bottom circle until the top circle

            # relation between x ad z is defined by an equation of a circle : "(x-h)^2 + (z-k)^2 = r^2"
            # x = ?, z = height_trap ,  h,k = centreCircle, r=radiuscircle
            # this give us x = sqrt( r^2 -(height_trap - k)^2 ) - h
            # the center of the circle is located on the perpendicular line true centerpoint between the two points given
            # the perpendicular line can be discripted as y = x*m + b
            # we want the center to be on 80% of the total height => center_y = total_height*0.8
            # from that we can calculate the x coordinate of the center
            # with pythagoras we calculate the r**2

            circle1 = Circle2D("patch front circle")
            circle1.set_plane("xz")
            m1, b1 = circle1.perpendicular_middel_line(point1=(self._top_circle / 2, self._height),
                                                        point2=(self._bottom_circle / 2, 0))

            circle1.set_z(self._height * 0.8)
            circle1.set_x((circle1.get_z() - b1) / m1)
            circle1.set_radius(math.sqrt((circle1.get_x() - self._bottom_circle / 2) ** 2 + circle1.get_z() ** 2))
            self._parameter_circles.append(circle1)
            if self._modes.get("parameter mode") == "dubbel" or self._modes.get("parameter mode") == "trippel":

                rad = 2*math.pi/(self._legs*2)
                # the second patch formula is in the plane of y z
                # the circle parameters is given by 3 point where the circle runs true
                # point one at the bottom circle
                # point two at the middel of the circle and x % smaller than the bottom part of the leg
                # point three at the top of the top circle

                circle2 = Circle2D("patch sides circle")
                circle2.circle_by_three_points(
                    (math.sin(rad / 2) * self._bottom_circle/2, math.cos(rad / 2) * self._bottom_circle/2, 0),
                    (math.sin(rad / 2) * self._bottom_circle/2, math.cos(rad / 2) * self._bottom_circle/2 * 0.1,
                                                                                                    self._height * 0.5),
                    (math.sin(rad / 2) * self._bottom_circle/2, math.cos(rad/2) * self._top_circle/2, self._height))
                self._parameter_circles.append(circle2)

                if self._modes.get("parameter mode") == "trippel":

                    # the third patch formula is in the plane of x z
                    # the patch formula will use three  circle equations

                    # the middel is the main circle and is the same circle as circle but with a bigger radius
                    circle3_m = Circle2D("patch back middel")
                    circle3_m.set_plane("xz")
                    circle3_m.set_x(circle1.get_x())
                    circle3_m.set_z(circle1.get_z())
                    circle3_m.set_radius(circle1.get_radius()+self._top_circle/2*0.2)

                    self._parameter_circles.append(circle3_m)
                    '''
                    # the bottom circle to give a rounding at the bottom of the leg
                    circle3_b = Circle2D("patch back bottom")
                    self._parameter_circles.append(circle3_b)

                    # the bottom circle to give a rounding at the top of the leg
                    circle3_t = Circle2D("patch back top")
                    self._parameter_circles.append(circle3_t)
                    '''

    def calculate_trapezium_points(self):
        # this function creates a list with object of the class trapezium
        # each object of the class trapezium stores four points these points represent a trapezium in a 2d plane
        # each object of the class trapezium is a cross section of one leg in the chess piece
        # the coordinates per cross section are calculated by looping true the height
        # the formula used for calculating each coordinates is based on the equation of circles
        # each mode is based on the previous one

        rad = 2 * math.pi / (self._legs*2)
        self._trap_list = list()

        # calculating parameters fomula's


        if self._modes.get("parameter mode") == "single":


            # create a list of trapizium that for one leg
            for i_z in range(0, self._height):
                circle1 = self._parameter_circles[0]

                x_center = circle1.get_x() - math.sqrt(circle1.get_radius()**2 - (i_z - circle1.get_z()) ** 2)

                front_point = TransMatrix(x=x_center, z=i_z)
                back_point = TransMatrix(x=x_center-7, z=i_z)
                front_point.z_rotate(rad/2)
                back_point.z_rotate(rad/2)
                self._trap_list.append(Trapezium(front=front_point.get_coordinates(mode="tuple"),
                                             back=back_point.get_coordinates(mode="tuple")))
        elif self._modes.get("parameter mode") == "dubbel":




            # create a list of trapizium that form one leg
            for i_z in range(0, self._height):
                circle1 = self._parameter_circles[0]
                circle2 = self._parameter_circles[1]
                x_path_front = (circle1.get_x() - math.sqrt(
                    circle1.get_radius()**2 - (i_z - circle1.get_z()) ** 2))*math.cos(rad/2)
                y_path_front = (circle2.get_y() - math.sqrt(circle2.get_radius()**2 - (i_z - circle2.get_z()) ** 2))
                x_path_back = x_path_front*0.5
                y_path_back = y_path_front*0.9

                front_point = TransMatrix(x=x_path_front, y=y_path_front, z=i_z)
                back_point = TransMatrix(x=x_path_back, y=y_path_back, z=i_z)

                self._trap_list.append(Trapezium(front=front_point.get_coordinates(mode="tuple"),
                                             back=back_point.get_coordinates(mode="tuple")))
        elif self._modes.get("parameter mode") == "trippel":
            pass

    def plot_2d_x_z(self):

        fig = plt.figure()
        fig.set_size_inches(8, 8)

        for item in self._parameter_circles:
            if item.get_plane() == "xz":
                x_plot = list()
                y_plot = list()
                for i in range(360):

                    x_plot.append(math.cos(i*2*math.pi/360)*item.get_radius()+item.get_x())
                    y_plot.append(math.sin(i * 2 * math.pi / 360) * item.get_radius() + item.get_z())
                plt.plot(x_plot, y_plot, label="circle{}".format(item.get_name()))

        plt.plot([self._bottom_circle/2, self._bottom_circle/2], [0, self._height], label="bottomDia")
        plt.plot([self._top_circle/2, self._top_circle/2], [0, self._height], label="topDia")

        plt.plot([self._top_circle / 2, self._bottom_circle/2], [self._height, 0], label="line between points")

        plt.plot([0, self._bottom_circle/2], [self._height, self._height], label="Height")
        plt.axis([0, self._height+20, 0, self._height+20])
        plt.xlabel("x axis")
        plt.ylabel("z axis")
        plt.title("2d test plot")
        plt.legend()
        plt.show()

    def plot_2d_y_z(self):

        fig = plt.figure()
        fig.set_size_inches(8, 8)

        for item in self._parameter_circles:

            if item.get_plane() == "yz":
                x_plot = list()
                y_plot = list()
                for i in range(360):

                    x_plot.append(math.cos(i*2*math.pi/360)*item.get_radius()+item.get_y())
                    y_plot.append(math.sin(i * 2 * math.pi / 360) * item.get_radius() + item.get_z())

                plt.plot(x_plot, y_plot, label="circle{}".format(item.get_name()))
                print(x_plot)
                print(y_plot)

        plt.plot([self._bottom_circle/2, self._bottom_circle/2], [0, self._height], label="bottomDia")
        plt.plot([self._top_circle/2, self._top_circle/2], [0, self._height], label="topDia")

        plt.plot([self._top_circle / 2, self._bottom_circle/2], [self._height, 0], label="line between points")

        plt.plot([0, self._bottom_circle/2], [self._height, self._height], label="Height")
        plt.axis([0, self._height+20, 0, self._height+20])
        plt.xlabel("y axis")
        plt.ylabel("z axis")
        plt.title("2d test plot")
        plt.legend()
        plt.show()
if __name__ == "__main__":
    pass

    # plot_2d()

    # rotate_trapliste_z(end_deg=360/legs)

    # wireframe_plot()
