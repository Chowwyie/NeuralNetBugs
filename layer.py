import random

def activation_function(input):
    return input if input else 0

class Layer:
    def __init__(self, indegree, outdegree, weights, biases):
        self.indegree = indegree
        self.outdegree = outdegree

        self.weights = weights
        self.biases = biases
        # self.weights = [[0]*outdegree for i in range(indegree)]
        # self.biases = [0] * outdegree

    # def _generate_random_layer(self):
    #     self.weights = [[0]*self.outdegree for i in range(self.indegree)]
    #     self.biases = [0]*self.outdegree
    #     for innode_index in range(self.indegree):
    #         for outnode_index in range(self.outdegree):
    #             self.weights[innode_index][outnode_index] = random.uniform(-100, 100)
    #     for bias_index in range(self.outdegree):
    #             self.biases[bias_index] = random.uniform(-100, 100)

    # def mutate(self):
    #     new_weights = []
    #     for innode_index in range(self.indegree):
    #         for outnode_index in range(self.outdegree):
    #             if random.randint(0,999) == 0:
    #                 weights[innode_index][outnode_index] = random.uniform(-100, 100)
    #     for bias_index in range(self.outdegree):
    #         if random.randint(0,999) == 0:
    #                 biases = random.uniform(-100, 100)
                
    
    def get_output(self, inputs):
        output = []
        for outnode_index in range(self.outdegree):
            output.append(self.biases[outnode_index])
            for innode_index in range(self.indegree):
                output[outnode_index] += inputs[innode_index] * self.weights[innode_index][outnode_index]
            output[outnode_index] = activation_function(output[outnode_index])
        return output
    