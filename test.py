# from brain import Brain 

# # self.weights = [[0]*outdegree for i in range(indegree)]
# # self.biases = [0] * outdegree

# test_brain = Brain([[-1],[1]], [0], [[0,0,1,0,0,0]], [0,0,0,0,0,0])
# print(test_brain.calculated_next_step([-1,0]))
import pygame

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WORLD_SURFACE = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
SCREEN.blit(WORLD_SURFACE, [0, 0])
WORLD_SURFACE.fill((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()

