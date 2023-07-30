import random

def activation_function(input):
    return input if input else 0

class Layer:
    def __init__(self, indegree, outdegree, weights=None, biases=None):
        self.indegree = indegree
        self.outdegree = outdegree

        if weights and biases:
            self.weights = weights
            self.biases = biases
        else:
            self._generate_random_layer()

    def _generate_random_layer(self):
        self.weights = [[0]*self.outdegree for i in range(self.indegree)]
        self.biases = [0]*self.outdegree
        for innode_index in range(self.indegree):
            for outnode_index in range(self.outdegree):
                self.weights[innode_index][outnode_index] = random.uniform(-100, 100)
        for bias_index in range(self.outdegree):
                self.biases[bias_index] = random.uniform(-100, 100)

    def mutate(self):
        # new_weights = self.weights
        # new_biases = self.biases
        mutation_rate = 100
        new_weights = [weight[:] for weight in self.weights]
        new_biases = self.biases[:]
        for innode_index in range(self.indegree):
            for outnode_index in range(self.outdegree):
                if random.randint(0,mutation_rate) == 0:
                    new_weights[innode_index][outnode_index] = random.uniform(-100, 100)
        for bias_index in range(self.outdegree):
            if random.randint(0,mutation_rate) == 0:
                    new_biases[bias_index] = random.uniform(-100, 100)
        return Layer(self.indegree, self.outdegree, weights=new_weights, biases=new_biases)
                
    
    def get_output(self, inputs):
        output = []
        for outnode_index in range(self.outdegree):
            output.append(self.biases[outnode_index])
            for innode_index in range(self.indegree):
                output[outnode_index] += inputs[innode_index] * self.weights[innode_index][outnode_index]
            output[outnode_index] = activation_function(output[outnode_index])
        return output
    