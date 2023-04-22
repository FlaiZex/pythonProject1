class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        filtered_data = [str(num) for num in self.data if Graph.LIMIT_Y[0] <= num <= Graph.LIMIT_Y[1]]
        print(" ".join(filtered_data))

graph_1 = Graph()
data_list = [int(num) for num in input("Введите числа через пробел: ").split()]
graph_1.set_data(data_list)
graph_1.draw()
