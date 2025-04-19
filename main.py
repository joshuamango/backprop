import math

class Node:
    def __init__(self):
        self.inputs = []
        self.weights = []

    def run(self):
        total = 0
        for i in range(len(self.inputs)):
            #print(f"{self.inputs[i]} * {self.weights[i]}")
            total += self.inputs[i] * self.weights[i]
        sigmoid = 1 / (1 + math.e ** total)
        return sigmoid

class Layer:
    def __init__(self, num=2, prev_layer=None):
        self.nodes = [Node() for i in range(num)]
        if prev_layer == None:
            self.input = [1.0 for i in range(num)]
        else:
            self.input = prev_layer.run()

    def send_input(self):
        for i in range(len(self.nodes)):
            self.nodes[i].inputs = self.input
            for j in range(len(self.input)):
                self.nodes[i].weights.append(0.5 if j % 2 == 0 else -0.5)

    def run(self):
        result = [node.run() for node in self.nodes]
        print(len(result))
        return result

def main():
    layer1 = Layer()
    layer1.send_input()
    layer2 = Layer(prev_layer=layer1)
    layer2.send_input()
    print(layer1.run())
    print("Layer 2 begin")
    print(layer2.run())


if __name__ == "__main__":
    main()
