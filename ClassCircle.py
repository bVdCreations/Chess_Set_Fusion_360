class Circle2D:

    def __init__(self, name):
        self._coordinate_x = 0
        self._coordinate_y = 0
        self._coordinate_z = 0
        self._plane = "xy"
        self._radius = 0
        self._name = name

    def get_x(self):
        return self._coordinate_x

    def get_y(self):
        return self._coordinate_y

    def get_z(self):
        return self._coordinate_z

    def get_radius(self):
        return self._radius

    def get_plane(self):
        return self._plane

    def get_name(self):
        return self._name

    def get_data(self):
        if self._plane == "xy":
            return self._coordinate_x, self._coordinate_y, self._radius
        elif self._plane == "xz":
            return self._coordinate_x, self._coordinate_z, self._radius
        elif self._plane == "yz":
            return self._coordinate_y, self._coordinate_z, self._radius

    def set_plane(self, plane):
        self._plane = plane

    def set_x(self, x_coordinate):
        self._coordinate_x = x_coordinate

    def set_y(self, y_coordinate):
        self._coordinate_y = y_coordinate

    def set_z(self, z_coordinate):
        self._coordinate_z = z_coordinate

    def set_radius(self, radius):
        self._radius = radius

    def set_name(self, name):
        self._name = name

    def circle_by_three_points(self, point1=(0, 0, 0), point2=(0, 0, 0), point3=(0, 0, 0)):
        print(point1)
        print(point2)
        print(point3)
        self.set_plane_by_three_points(point1=point1, point2=point2, point3=point3)

        if self._plane == "xy":
            m1, b1 = self.perpendicular_middel_line(point1=(point1[0], point1[1]), point2=(point2[0], point2[1]))
            m2, b2 = self.perpendicular_middel_line(point1=(point2[0], point2[1]), point2=(point3[0], point3[1]))
            self.set_x((b2 - b1) / (m1 - m2))
            self.set_y(m1 * self.get_x() + b1)
            self.set_radius((self.get_x() - point1[0]) ** 2 + (self.get_y() - point1[1]) ** 2)
        elif self._plane == "xz":
            m1, b1 = self.perpendicular_middel_line(point1=(point1[0], point1[2]), point2=(point2[0], point2[2]))
            m2, b2 = self.perpendicular_middel_line(point1=(point2[0], point2[2]), point2=(point3[0], point3[2]))
            self.set_x((b2 - b1) / (m1 - m2))
            self.set_z(m1 * self.get_x() + b1)
            self.set_radius((self.get_x() - point1[0]) ** 2 + (self.get_z() - point1[2]) ** 2)
        elif self._plane == "yz":
            print("here")
            print("wrong math")
            m1, b1 = self.perpendicular_middel_line(point1=(point1[1], point1[2]), point2=(point2[1], point2[2]))
            print(m1,b1)
            m2, b2 = self.perpendicular_middel_line(point1=(point2[1], point2[2]), point2=(point3[1], point3[2]))
            print(m2,b2)
            self.set_y((b2 - b1) / (m1 - m2))
            self.set_z(m1 * self.get_y() + b1)
            self.set_radius((self.get_y() - point1[1]) ** 2 + (self.get_z() - point1[2]) ** 2)

    def perpendicular_middel_line(self, point1=(0, 0), point2=(0, 0)):
        # a line can is discriped as y = x m + b
        # m and b are returned as a tuple
        middel = ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

        delta_yonx = (point1[1] - point2[1]) / (point1[0] - point2[0])
        m = -1 / delta_yonx
        b = middel[1] - middel[0] * m
        return m, b

    def set_plane_by_three_points(self, point1=(0, 0, 0), point2=(0, 0, 0), point3=(0, 0, 0)):
        if point1[0] == point2[0] == point3[0]:
            self.set_plane("yz")
        elif point1[1] == point2[1] == point3[1]:
            self.set_plane("xz")
        elif point1[2] == point2[2] == point3[2]:
            self.set_plane("xy")