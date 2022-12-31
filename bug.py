import random
from brain import Brain

class Bug:
    choices = {}
    def __init__(self,x,y, brain=None, color=None):
        self.x = x
        self.y = y
        # self.color = random color
        if not brain:
            if random.randint(0,1):
                self.color = (1,1,1)
                # self.brain = Brain([[-1],[1]], [0], [[0,0,1,0,0,0]], [0,0,0,0,0,0])
            else:
                self.color = (255,10,10)
                # self.brain = Brain([[-1],[1]], [0], [[0,0,0,1,0,0]], [0,0,0,0,0,0])
        else:
            self.brain = brain
            self.color = color

    def _move_up(self):
        return self.x, self.y+1

    def _move_down(self):
        return self.x, self.y-1

    def _move_left(self):
        return self.x-1, self.y

    def _move_right(self):
        return self.x+1, self.y

    def _move_random(self):
        move_magnitude = random.randint(-1,1)
        move_direction = random.randint(0,1)
        if move_direction:
            x,y = self.x + move_magnitude, self.y
        else:
            x,y = self.x, self.y + move_magnitude
        return x,y
    
    def next_position(self):
        next_move = self.brain.calculated_next_step([-1,0])
        if next_move == "random":
            return self._move_random()
        elif next_move == "up":
            return self._move_up()
        elif next_move == "down":
            return self._move_down()
        elif next_move == "left":
            return self._move_left()
        elif next_move == "right":
            return self._move_right()
        elif next_move == "stay":
            return self.x,self.y

    def reproduce(self):
        return Bug(0,0,self.brain, self.color)

    # def next_turn(self):
    #     move_magnitude = random.randint(-1,1)
    #     move_direction = random.randint(0,1)
    #     if move_direction:
    #         x,y = self.x + move_magnitude, self.y
    #     else:
    #         x,y = self.x, self.y + move_magnitude
    #     return x,y
    
    def place(self, x, y):
        self.x = x
        self.y = y


        
[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
