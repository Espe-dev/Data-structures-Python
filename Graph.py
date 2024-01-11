class GraphNode:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return str(self.value)


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = GraphNode(value)

    def add_edge(self, value1, value2):
        if value1 in self.nodes and value2 in self.nodes:
            node1 = self.nodes[value1]
            node2 = self.nodes[value2]

            if node2 not in node1.neighbors:
                node1.neighbors.append(node2)

            if node1 not in node2.neighbors:
                node2.neighbors.append(node1)

    def __str__(self):
        result = ""
        for node_value, node in self.nodes.items():
            neighbors = ", ".join(str(neighbor) for neighbor in node.neighbors)
            result += f"{node_value} -> [{neighbors}]\n"
        return result


# Exemple d'utilisation
graph = Graph()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)

graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 1)

print("Graph:")
print(graph)
