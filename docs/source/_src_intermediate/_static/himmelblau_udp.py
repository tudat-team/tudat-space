import math

class HimmelblauOptimization:
    """
    This class defines a PyGMO-compatible User-Defined Optimization Problem.
    """

    def __init__(self,
                 x_min: float,
                 x_max: float,
                 y_min: float,
                 y_max: float):
        """
        Constructor for the HimmelblauOptimization class.
        """
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def get_bounds(self):
        """
        Defines the boundaries of the search space.
        """
        return ([self.x_min, self.y_min], [self.x_max, self.y_max])

    def fitness(self,
                x: list):
        """
        Computes the fitness value for the problem.
        """
        function_value = math.pow(x[0] * x[0] + x[1] - 11.0, 2.0) + math.pow(x[0] + x[1] * x[1] - 7.0, 2.0)
        return [function_value]