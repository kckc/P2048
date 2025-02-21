import random

class FullyConnectedLayer:
    def __init__(self, input_size, output_size):
        # Initialize weights and biases with random values
        self.weights = [[0 for _ in range(output_size)] for _ in range(input_size)]
        self.biases = [0 for _ in range(output_size)]
        for i in range(input_size):
            for j in range(output_size):
                self.weights[i][j] = random.uniform(-1, 1)
                self.input = [0 for _ in range(input_size)]
    
    def forward(self, input):
        # Store the input for backward pass
        self.input = input
        # Initialize output with zeros
        self.output = [0 for _ in range(len(self.biases))]
        # Calculate the dot product of input and weights and add bias
        for i in range(len(self.biases)):
            for j in range(len(self.input)):
                self.output[i] += self.input[j] * self.weights[j][i]
            self.output[i] += self.biases[i]
        # Return the output of the layer
        return self.output
    
    def backward(self, dvalues):
        # Initialize dweights, dbiases, and dinputs with zeros
        self.dweights = [[0 for _ in range(len(self.biases))] for _ in range(len(self.input))]
        self.dbiases = [0 for _ in range(len(self.biases))]
        self.dinputs = [0 for _ in range(len(self.input))]
        # Calculate the gradients of weights, biases, and inputs
        for i in range(len(self.biases)):
            for j in range(len(self.input)):
                self.dweights[j][i] += self.input[j] * dvalues[i]
            self.dbiases[i] += dvalues[i]
        for i in range(len(self.input)):
            for j in range(len(self.biases)):
                self.dinputs[i] += self.weights[i][j] * dvalues[j]
        # print(dvalues, self.dweights, self.dbiases)
        # Normalize weights
        norm = 0
        for i in range(len(self.weights)):
            for j in range(len(self.weights[0])):
                norm += self.dweights[i][j] * self.dweights[i][j]
        norm = norm ** 0.5
        for i in range(len(self.weights)):
            for j in range(len(self.weights[0])):
                self.dweights[i][j] = self.dweights[i][j] / norm
        # Return the gradients of the input
        self.weights = self.dweights
        self.biases = self.dbiases
        return self.dinputs