class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        elif id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
