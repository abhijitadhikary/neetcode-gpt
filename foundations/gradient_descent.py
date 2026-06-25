class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        assert iterations >= 0, 'Iterations can not be negative'
        assert learning_rate > 0 and learning_rate < 1, 'Learning rate should be between 0 and 1'
        # assert init != 0, 'You cannot start with 0 as the initial guess'

        for index_iteration in range(iterations):
            init = init - 2*init*learning_rate
        return round(init, 5)

