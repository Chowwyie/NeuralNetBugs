from layer import Layer
import random

class Brain:
    # should be able to modify the number of layers/number of neurons
    def __init__(self, layers=None):
        if not layers:
            self.layers = [Layer(4, 3), Layer(3, 6)]
        else:
            self.layers = layers
        # self.layers = [Layer(2, 1, weights1, biases1), Layer(1, 6, weights2, biases2)]
    
    def _calculate_network_output(self, field_of_vision):
        input = field_of_vision
        for layer in self.layers:
            input = layer.get_output(input)
        return input

    def mutate(self):
        new_layers = []
        for layer in self.layers:
            new_layers.append(layer.mutate())
        return Brain(new_layers)

    def calculated_next_step(self, field_of_vision):
        network_output = self._calculate_network_output(field_of_vision)
        try:
            return random.choices(["stay", "random", "left", "right", "up", "down"], weights=network_output, k=1)[0]
        except:
            return random.choices(["random", "left", "right", "up", "down"], k=1)[0]
    
    