class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.__mass = 25
        self.__thickness = 5

    def asphalt_mass_calc(self):
        asphalt_mass = self._length * self._width * self.__mass * self.__thickness
        print(f'{asphalt_mass/1000} т.')


new_road = Road(5000, 20)
new_road.asphalt_mass_calc()
