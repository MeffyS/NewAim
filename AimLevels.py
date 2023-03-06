from abc import ABC


class AimLevel(ABC):
    def __init__(
        self,
        level=0,
        money=0,
        min_points=0,
        max_points=25,
        change_speed=500,
        hearts=4,
        points_counter=1,
    ):
        self.level = level
        self.money = money
        self.min_points = min_points
        self.max_points = max_points
        self.change_speed = change_speed
        self.hearts = hearts
        self.points_counter = points_counter

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


def points_checker(points):
    a_level = Level_0()
    if points >= 10 and points <= 100:
        a_level = Level_1()
        print(a_level.level)

    if points >= 101 and points < 151:
        a_level = Level_2()

    return a_level


class Level_1(AimLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.level = 1
        self.change_speed = 9700

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
        self.change_speed = 9400

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
        self.change_speed = 9000

    def money_converter(self):
        pass
        # return (self.level + 0) * 2.5

    def count_points(self):
        pass
        # return (self.level + self.min_points) + 20
