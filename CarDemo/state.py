#State class, from which all other classes derive

class State(object):
    def __init__(self):
        print("Processing current state", str(self))

    def onEvent(self, event):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__
