""" holds particle object definitions """
class SingleRock():
    """ fallable object that can also accept fallable objects """
    def __init__(self):
        self.can_fall = True
        self.accepts_rocks = True

    def __str__(self):
        return '.'


class EmptySpace():
    """ non-fallable object that can accept fallables """
    def __init__(self):
        self.can_fall = False
        self.accepts_rocks = True

    def __str__(self):
        return ' '


class Table():
    """ non-fallable object that cannot accept fallable objects """
    def __init__(self):
        self.can_fall = False
        self.accepts_rocks = False

    def __str__(self):
        return 'T'


class DoubleRock():
    """ fallable object that cannot accept fallable objects """
    def __init__(self):
        self.can_fall = True
        self.accepts_rocks = False

    def __str__(self):
        return ':'
