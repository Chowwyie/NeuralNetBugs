from brain import Brain 

# self.weights = [[0]*outdegree for i in range(indegree)]
# self.biases = [0] * outdegree

test_brain = Brain([[-1],[1]], [0], [[0,0,1,0,0,0]], [0,0,0,0,0,0])
print(test_brain.calculated_next_step([-1,0]))

