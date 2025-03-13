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

class Link:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getValue(self):
        return self.src.getValue() * self.weight
    def grad(self, n):
        return 2/n*self.src.value
    def learn(self,  n, dest_grad_times_error):
        self.weight -= self.grad(n) * dest_grad_times_error * Node.l_rate
        self.src.back(self.grad(n) * dest_grad_times_error)

class Node:
    l_rate=0.01
    def __init__(self):
        self.value = None
        self.links = []
        self.bias = Node.initW()
    def initW():
        # return 1
        return random.uniform(-1, 1)
    def link(self, node):
        l = Link(self, node, Node.initW())
        node.links.append(l)
    def cal(self):
        self.value = sum([l.getValue() for l in self.links]) + self.bias
        return self.value
    def getValue(self):
        return self.value if self.value is not None else self.cal()
    def back(self, expected):
        self.bias -= (self.value - expected) * Node.l_rate
        for l in self.links:
            l.learn(len(self.links), self.value - expected)


class Layer:
    def __init__(self, in_dim, out_dim, inlayer = None):
        self.in_dim = in_dim
        self.out_dim = out_dim
        self.inlayer = [Node() for i in range(in_dim)] if inlayer is None else inlayer
        self.outlayer = [Node() for i in range(out_dim)]
        for i in self.inlayer:
            for j in self.outlayer:
                i.link(j)
    def forward(self):
        return [n.getValue() for n in self.outlayer]
    def backward(self, dvalues):
        [n.back(dvalues[i]) for i, n in enumerate(self.outlayer)]
    def print(self):
        for i in self.outlayer:
            print([link.weight for link in i.links], i.bias)
