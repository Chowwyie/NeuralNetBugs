import pygame
import sys
from bug import Bug
import random

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

class World:
    BLACK = (0,0,0)
    WHITE = (255, 255, 255)

    def __init__(self, row_size, column_size, number_of_bugs):
        self.row_size = row_size
        self.column_size = column_size
        self.block_size = WINDOW_WIDTH//row_size
        self.number_of_bugs = number_of_bugs
        self.grid = self.generate_grid()
        self.bugs = self.generate_bugs()

    def generate_grid(self):
        return [[0] * self.row_size for i in range(self.column_size)]

    def successful_bugs(self):
        successful_bugs = []
        for i in range(self.row_size//4, self.row_size//4*3):
            for j in range(self.column_size//4, self.column_size//4*3):
                if self.grid[i][j]:
                     successful_bugs.append(self.grid[i][j])
        return successful_bugs

    def repopulate_bugs(self):
        successful_bugs = self.successful_bugs()
        self.grid = self.generate_grid()
        number_of_bugs = 0
        self.bugs = []
        while number_of_bugs < self.number_of_bugs:
            bug = random.choice(successful_bugs)
            # bug = successful_bugs.pop(0)
            # successful_bugs.append(bug)
            child_bug = bug.reproduce()
            x,y = self._find_vacated_coordinate()
            child_bug.place(x,y)
            self.bugs.append(child_bug)
            self.grid[x][y] = child_bug
            number_of_bugs += 1

    def _find_vacated_coordinate(self):
        x = random.randint(0, self.row_size - 1)
        y = random.randint(0, self.column_size - 1)
        while (self.grid[x][y]):
            x = random.randint(0, self.row_size - 1)
            y = random.randint(0, self.column_size - 1)
        return x,y

    def generate_bugs(self):
        bugs = []
        for i in range(self.number_of_bugs):
            x,y = self._find_vacated_coordinate()
            new_bug = Bug(x,y)
            bugs.append(new_bug)
            self.grid[x][y] = new_bug
        return bugs

    def run_world(self):
        global WORLD_SURFACE, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        WORLD_SURFACE = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        CLOCK = pygame.time.Clock()
        self.draw_grid()
        generation_steps = 150
        generations = 0
        number_of_generations = 0
        generation_string = "Generation: 0"
        
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render(generation_string, True, (255,255,255), (0,0,0))
        while True:
            i = 0
            number_of_generations += 1
            generation_string = "Generation: " + str(number_of_generations)
            text = font.render(generation_string, True, (255,255,255), (0,0,0))
            while i < generation_steps:
                # pygame.clock.tick(40)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.process_turns()
                if number_of_generations > generations:
                    self.draw_grid()
                    CLOCK.tick(100000000)
                    pygame.display.update()
                    # SCREEN.blit(text, (320, 60))
                    SCREEN.blit(text, (330, 720))
                    SCREEN.blit(WORLD_SURFACE, (100, 100))
                
            self.repopulate_bugs()


    def draw_grid(self):
        WORLD_SURFACE.fill((255,255,255))
        # WORLD_SURFACE.fill((100,255,100), (WORLD_SURFACE.get_width()//4, WORLD_SURFACE.get_height()//4, WORLD_SURFACE.get_width()//2, WORLD_SURFACE.get_height()//2))
        self.draw_bugs()

    def draw_bugs(self):
        for bug in self.bugs:
            self.draw_bug(bug)

    def draw_bug(self, bug):
        x, y = bug.x*self.block_size + self.block_size/2, bug.y*self.block_size + self.block_size/2
        pygame.draw.circle(WORLD_SURFACE, bug.color, (x, y), self.block_size/2)

    def process_turns(self):
        for bug in self.bugs:
            x,y = bug.next_position([bug.x, bug.y, self.row_size-bug.x, self.column_size-bug.y])
            if 0 <= x < self.row_size and 0 <= y < self.column_size and not self.grid[x][y]:
                self.grid[bug.x][bug.y] = 0
                bug.place(x,y)
                self.grid[x][y] = bug

