class graph:
    def __init__(self, x, y):
        self.x_axis = x
        self.y_axis = y

    def optimize(self, jump):
        # look for largest slope to find our "sweet spot"
        array = zip(self.x_axis, self.y_axis)
        slope_max = {
            'slope': 0.0,
            'lower_bound': 0.0,
            'upper_bound': 0.0
        }
        i = 0
        # find largest slope between two points and return that point as it's where
        # our optimum number of users is.
        # this is founded on the assumption that the number of users will always
        # correlate to the query time.
        # FIXME this function is not pythonic at all.
        while i < len(array):
            if i+jump >= len(array):
                return slope_max
            rise = (array[i+jump][1] - array[i][1])
            run = (array[i+jump][0] - array[i][0])

            if run == 0.0:
                i += 1
                continue
            slope = rise / run

            if slope > slope_max['slope']:
                slope_max['slope'] = slope
                slope_max['lower_bound'] = array[i]
                slope_max['upper_bound'] = array[i + jump]
            i += 1
        return slope_max
