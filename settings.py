class Settings():
    """A class to set all settongs."""

    def __init__(self):
        """foundational settings."""
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 700
        self.bgc = (135,206,250)
        #sw settings
        self.sw_speed = 1
        self.sw_left = 1   #1 >> two chance
        #bullet settings
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (25,25,112)
        self.bullet_num = 3
        #cats settings
        self.cat_speed = 1
        self.cat_drop_speed = 10
        self.team_direction = 1  # right and left
        
