class Gameset():
    """game set or reset."""

    def __init__(self,sets):
        self.sets = sets
        self.reset()
        self.game_act = False

    def reset(self):
        self.sw_left = self.sets.sw_left
        self.score = 0
