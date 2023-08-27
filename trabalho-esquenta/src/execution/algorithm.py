class Algorithm:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def run(self, data):
        return self.function(data)

    def __str__(self):
        return self.name