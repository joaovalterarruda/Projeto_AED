import matplotlib.pyplot as plt
import networkx as nx
from linkedqueue import LinkedQueue
from linkedstack import LinkedStack


class Graph:
    def __init__(self) -> None:
        self._network: dict[str, list[str]] = {}

    def is_empty(self) -> bool:
        return len(self._network) == 0

    def __len__(self) -> int:
        return len(self._network)

    def __str__(self) -> str:
        s = ""
        for v1 in sorted(self._network):
            s += "\n\n Vertex: " + str(v1)
            s += "\n Edges: "
            for v2 in sorted(self._network[v1]):
                s += str(v2) + "\t"
        return s

    def __iter__(self):
        return iter(self._network)

    def clear(self):
        self._network = {}

    def size_vertices(self) -> int:
        return len(self._network)

    def size_edges(self) -> int:
        i = 0  # int - count
        for v in self._network.values():
            i += len(v)
            i = i / 2
        return i

    def get_vertices(self) -> list[str]:
        return list(self._network.keys())

    def get_edges(self) -> list[tuple[str, str]]:
        edges: list[tuple[str, str]] = []
        for v1 in self._network:
            for v2 in self._network[v1]:
                edges.append((v1, v2))
        return edges

    def predecessors(self, label: str) -> set[str]:
        pred_set: set[str] = set()
        for v1 in self._network:
            for v2 in self._network[v1]:
                if v2 == label:
                    pred_set.add(v1)
        return pred_set

    def successors(self, label: str) -> set[str]:
        if label in self._network:
            return set(self._network[label])
        return set()

    def add_vertex(self, label: str) -> None:
        if label not in self._network:
            self._network[label] = []

    # FROM - label de origem e TO - label de destino
    def add_edge(self, from_label: str, to_label: str) -> None:
        if from_label in self._network and to_label in self._network:
            if to_label not in self._network[from_label]:
                self._network[from_label].append(to_label)
                self._network[to_label].append(from_label)

    def remove_vertex(self, label: str) -> None:
        if label in self._network:
            del (self._network[label])
            for v in self._network:
                if label in self._network[v]:
                    self._network[v].remove(label)

    def remove_edge(self, from_label: str, to_label: str) -> None:
        if from_label in self._network and to_label in self._network:
            if to_label in self._network[from_label]:
                self._network[from_label].remove(to_label)
                self._network[to_label].remove(from_label)

    def contains_vortex(self, label: str) -> bool:
        return label in self._network

    def contains_edge(self, from_label: str, to_label: str) -> bool:
        if from_label in self._network and to_label in self._network:
            if to_label in self._network[from_label]:
                return False

    def breath_first_travessal(self, from_label: str) -> list[str]:
        result: list[str] = []
        queue_aux: LinkedQueue = LinkedQueue()
        if from_label in self._network:
            queue_aux.add(from_label)
            while not queue_aux.is_empty():
                front = queue_aux.pop()

    def from_result_to_shortest_path(self, result: dict, to_label: str) -> list[str]:
        reversed_path = LinkedStack()
        reversed_path.push(to_label)
        vc = to_label
        while result[vc][1] is not None:
            vc = result[vc][1]
            reversed_path.push(vc)
        path = []
        while not reversed_path.is_empty():
            path.append(reversed_path.pop())
        return path

    def shortest_path(self, from_label: str, to_label: str) -> list[str]:
        result = {}
        q: LinkedQueue = LinkedQueue()
        if from_label in self._network and to_label in self._network:
            result[from_label] = (0, None)
            q.add((from_label, 0, None))
            while not q.is_empty():
                front = q.pop()
                if front[0] not in result:
                    result[front[0]] = (front[1] + 1, front[2])
                for v in self._network[front[0]]:
                    if v not in result:
                        q.add((v, front[1] + 1, front[0]))
            return self.from_result_to_shortest_path(result, to_label)
        return -1

    def get_graph(self):
        return self._network

    def map_network(self):
        graph = nx.DiGraph(self.get_graph())
        nx.draw(graph, with_labels=True)
        plt.show()
