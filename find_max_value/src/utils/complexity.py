import math

class Complexity:
    @staticmethod
    def o_log_n(n):
        return math.log(n, 2)

    @staticmethod
    def o_n(n):
        return n

    @staticmethod
    def o_n_log_n(n):
        return n * math.log(n, 2)

    @staticmethod
    def o_n_squared(n):
        return n * n

    @staticmethod
    def o_n_cubed(n):
        return n * n * n