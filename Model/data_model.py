class DataModel:
    def __init__(self):
        self.id = 0

    def get_value(self, attribute):
        return eval('self.' + attribute)
