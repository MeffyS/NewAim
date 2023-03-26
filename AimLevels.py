from abc import ABC


class AimLevel(ABC):
    def __init__(
        self,
        level=0,
        money=0,
        min_points=0,
        max_points=25,
        change_speed=2000,
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
        self.change_speed = 2000

    def money_converter(self):

        return ( 1* 0.00)

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 10


class Level_1(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 1
        self.change_speed = 9688
        self.object_width = 240
        self.object_height = 240
        self.border_x = 1040
        self.border_y = 760

    def money_converter(self):
        
        return ( 1* 0.01)

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 10


class Level_2(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 2
        self.change_speed = 9376
        self.object_width = 230
        self.object_height = 230
        self.border_x = 1050
        self.border_y = 770

    def money_converter(self):
        return ( 1* 0.02)

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_3(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 3
        self.change_speed = 9064
        self.object_width = 220
        self.object_height = 220
        self.border_x = 1060
        self.border_y = 780

    def money_converter(self):

        return ( 1* 0.03)

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_4(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 4
        self.change_speed = 8752
        self.object_width = 210
        self.object_height = 210
        self.border_x = 1070
        self.border_y = 790

    def money_converter(self):
        return ( 1* 0.04)

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_5(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 5
        self.change_speed = 8440
        self.object_width = 200
        self.object_height = 200
        self.border_x = 1080
        self.border_y = 800


    def money_converter(self):
        return ( 1* 0.05)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_6(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 6
        self.change_speed = 8118
        self.object_width = 190
        self.object_height = 190
        self.border_x = 1090
        self.border_y = 810

    def money_converter(self):
        return ( 1* 0.06)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_7(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 7
        self.change_speed = 7806
        self.object_width = 180
        self.object_height = 180
        self.border_x = 1100
        self.border_y = 820


    def money_converter(self):
        return ( 1* 0.07)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_8(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 8
        self.change_speed = 7494
        self.object_width = 170
        self.object_height = 170
        self.border_x = 1110
        self.border_y = 830

    def money_converter(self):
        return ( 1* 0.08)

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_9(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 9
        self.change_speed = 7182
        self.object_width = 160
        self.object_height = 160
        self.border_x = 1120
        self.border_y = 840

    def money_converter(self):
        return ( 1* 0.09)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


class Level_10(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 10
        self.change_speed = 6870
        self.object_width = 150
        self.object_height = 150
        self.border_x = 1130
        self.border_y = 850

    def money_converter(self):
        return ( 1* 0.1)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_11(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 11
        self.change_speed = 6558
        self.object_width = 140
        self.object_height = 140
        self.border_x = 1140
        self.border_y = 860

    def money_converter(self):
        return ( 1* 0.11)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_12(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 12
        self.change_speed = 6246
        self.object_width = 130
        self.object_height = 130
        self.border_x = 1150
        self.border_y = 870

    def money_converter(self):
        return ( 1* 0.12)

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_13(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 13
        self.change_speed = 5934
        self.object_width = 120
        self.object_height = 120
        self.border_x = 1160
        self.border_y = 880

    def money_converter(self):
        return ( 1* 0.13)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_14(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 14
        self.change_speed = 5622
        self.object_width = 110
        self.object_height = 110
        self.border_x = 1170
        self.border_y = 890

    def money_converter(self):
        return ( 1* 0.14)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_15(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 15
        self.change_speed = 5310
        self.object_width = 100
        self.object_height = 100
        self.border_x = 1180
        self.border_y = 900

    def money_converter(self):
        return ( 1* 0.15)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_16(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 16
        self.change_speed = 4998
        self.object_width = 95
        self.object_height = 95
        self.border_x = 1185
        self.border_y = 905

    def money_converter(self):
        return ( 1* 0.16)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_17(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 17
        self.change_speed = 4686
        self.object_width = 90
        self.object_height = 90
        self.border_x = 1190
        self.border_y = 910

    def money_converter(self):
        return ( 1* 0.17)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_18(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 18
        self.change_speed = 4374
        self.object_width = 85
        self.object_height = 85
        self.border_x = 1195
        self.border_y = 915

    def money_converter(self):
        return ( 1* 0.18)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_19(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 19
        self.change_speed = 4062
        self.object_width = 80
        self.object_height = 80
        self.border_x = 1200
        self.border_y = 920

    def money_converter(self):
        return ( 1* 0.19)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_20(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 20
        self.change_speed = 3750
        self.object_width = 75
        self.object_height = 75
        self.border_x = 1205
        self.border_y = 925

    def money_converter(self):
        return ( 1.5* 0.2)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_21(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 21
        self.change_speed = 3438
        self.object_width = 70
        self.object_height = 70
        self.border_x = 1210
        self.border_y = 930

    def money_converter(self):
        return ( 1.5* 0.21)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_22(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 22
        self.change_speed = 3126
        self.object_width = 65
        self.object_height = 65
        self.border_x = 1215
        self.border_y = 935

    def money_converter(self):
        return ( 1.5* 0.22)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_23(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 23
        self.change_speed = 2814
        self.object_width = 60
        self.object_height = 60
        self.border_x = 1220
        self.border_y = 940

    def money_converter(self):
        return ( 1.5* 0.23)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_24(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 24
        self.change_speed = 2502
        self.object_width = 55
        self.object_height = 55
        self.border_x = 1225
        self.border_y = 945

    def money_converter(self):
        return ( 1.5* 0.24)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_25(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 25
        self.change_speed = 2190
        self.object_width = 50
        self.object_height = 50
        self.border_x = 1230
        self.border_y = 950

    def money_converter(self):
        return ( 1.5* 0.25)
 

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_26(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 26
        self.change_speed = 1878
        self.object_width = 45
        self.object_height = 45
        self.border_x = 1235
        self.border_y = 955

    def money_converter(self):
        return ( 1.5* 0.26)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_27(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 27
        self.change_speed = 1566
        self.object_width = 40
        self.object_height = 40
        self.border_x = 1240
        self.border_y = 960

    def money_converter(self):
        return ( 1.5* 0.27)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_28(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 28
        self.change_speed = 1254
        self.object_width = 35
        self.object_height = 35
        self.border_x = 1245
        self.border_y = 965

    def money_converter(self):
        return ( 1.5* 0.28)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_29(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 29
        self.change_speed = 942
        self.object_width = 30
        self.object_height = 30
        self.border_x = 1250
        self.border_y = 970

    def money_converter(self):
        return ( 1.5* 0.29)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_30(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 30
        self.change_speed = 630
        self.object_width = 25
        self.object_height = 25
        self.border_x = 1255
        self.border_y = 975

    def money_converter(self):
        return ( 2* 0.3)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20

class Level_31(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 31
        self.change_speed = 318
        self.object_width = 20
        self.object_height = 20
        self.border_x = 1260
        self.border_y = 980

    def money_converter(self):
        return ( 2* 0.31)


    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20


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
        "Level_11()": [111, 120],
        "Level_12()": [121, 130],
        "Level_13()": [131, 140],
        "Level_14()": [141, 150],
        "Level_15()": [151, 160],
        "Level_16()": [161, 170],
        "Level_17()": [171, 180],
        "Level_18()": [181, 190],
        "Level_19()": [191, 200],
        "Level_20()": [201, 210],
        "Level_21()": [211, 220],
        "Level_22()": [221, 230],
        "Level_23()": [231, 240],
        "Level_24()": [241, 250],
        "Level_25()": [251, 260],
        "Level_26()": [261, 270],
        "Level_27()": [271, 280],
        "Level_28()": [281, 290],
        "Level_29()": [291, 300],
        "Level_30()": [301, 310],
        "Level_31()": [311, 210],
    }

def points_checker(points):
    a_level = Level_0()

    for level, determinant in levels.items():
        if determinant[0] <= points and determinant[1] >= points:
            a_level = eval(level)
    return a_level


def set_level_attributes(points):
    a_level = Level_0()

    for level, determinant in levels.items():
        if determinant[0] <= points and determinant[1] >= points:
            a_level = eval(level)
    return a_level


a = points_checker(120)
print(a.level)
