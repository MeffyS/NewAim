from abc import ABC


class AimLevel(ABC):
    def __init__(
        self,
        level=0,
        money=0,
        min_points=0,
        max_points=25,
        change_speed=1000,
        hearts=4,
        points_counter=1,
        object_width=250,
        object_height=250,
        border_x = 1030,
        border_y = 750

    ):
        self.level = level
        self.money = money
        self.min_points = min_points
        self.max_points = max_points
        self.change_speed = change_speed
        self.hearts = hearts
        self.points_counter = points_counter
        self.object_width = object_width
        self.object_height = object_height
        self.border_x = border_x
        self.border_y = border_y


    
    def money_converter(self):
        pass

    def count_points(self):
        pass


class Level_0(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 0

    def money_converter(self):
        pass
        # return (self.level + 0) * 1.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 10


class Level_1(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 1
        self.change_speed = 5000
        self.object_width = 240
        self.object_height = 240
        self.border_x = 1040
        self.border_y = 760

    def money_converter(self):
        pass
        # return (self.level + 0) * 1.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 10


class Level_2(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 2
        self.change_speed = 4000
        self.object_width = 230
        self.object_height = 230
        self.border_x = 1050
        self.border_y = 770

    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_3(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 3
        self.change_speed = 5000
        self.object_width = 220
        self.object_height = 220
        self.border_x = 1060
        self.border_y = 780

    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_4(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 4
        self.change_speed = 5000
        self.object_width = 210
        self.object_height = 210
        self.border_x = 1070
        self.border_y = 790

    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_5(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 5
        self.change_speed = 5000
        self.object_width = 200
        self.object_height = 200
        self.border_x = 1080
        self.border_y = 800


    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_6(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 6
        self.change_speed = 4000
        self.object_width = 190
        self.object_height = 190
        self.border_x = 1090
        self.border_y = 810

    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_7(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 7
        self.change_speed = 6900
        self.object_width = 180
        self.object_height = 180
        self.border_x = 1100
        self.border_y = 820


    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_8(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 8
        self.change_speed = 6400
        self.object_width = 170
        self.object_height = 170
        self.border_x = 1110
        self.border_y = 830

    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_9(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 9
        self.change_speed = 5900
        self.object_width = 160
        self.object_height = 160
        self.border_x = 1120
        self.border_y = 840

    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_10(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 10
        self.change_speed = 5400
        self.object_width = 150
        self.object_height = 150
        self.border_x = 1230
        self.border_y = 850

    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


def points_checker(points):
    a_level = Level_0()
    levels = {
        "Level_0()": [0, 10],
        "Level_1()": [11, 20],
        "Level_2()": [21, 30],
        "Level_3()": [31, 40],
        "Level_4()": [41, 50],
        "Level_5()": [51, 60],
        "Level_6()": [61, 70],
        "Level_7()": [71, 80],
        "Level_8()": [81, 90],
        "Level_9()": [91, 100],
        "Level_10()": [101, 110],
    }
    for level, determinant in levels.items():
        if determinant[0] <= points and determinant[1] >= points:
            a_level = eval(level)
    return a_level


def set_level_attributes(points):
    a_level = Level_0()
    levels = {
        "Level_0()": [0, 10],
        "Level_1()": [11, 20],
        "Level_2()": [21, 30],
        "Level_3()": [31, 40],
        "Level_4()": [41, 50],
        "Level_5()": [51, 60],
        "Level_6()": [61, 70],
        "Level_7()": [71, 80],
        "Level_8()": [81, 90],
        "Level_9()": [91, 100],
        "Level_10()": [101, 110],
    }
    for level, determinant in levels.items():
        if determinant[0] <= points and determinant[1] >= points:
            a_level = eval(level)
    return a_level


a = points_checker(120)
print(a.level)
