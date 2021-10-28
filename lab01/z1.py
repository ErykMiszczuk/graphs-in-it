import sys
from typing import List, Tuple, Dict

# Types
VertexList = List[int]
EdgePair = Tuple[int, int]
EdgeList = List[EdgePair]
AdjacencyList = Dict[int, List[int]]
Matrix = List[List[int]]

class SimpleGraph():
    def __init__(self, adjacency_list: AdjacencyList, vertices: VertexList, edges: EdgeList, vertices_num: int, edges_num: int) -> None:
        self.adjacency_list = adjacency_list
        self.vertices = vertices
        self.edges = edges
        self.vertices_num = vertices_num
        self.edges_num = edges_num

if not sys.argv[1:]:
    raise RuntimeError('Nie podano ścieżki do pliku')

def get_edges_and_verices_from_file(filepath: str) -> SimpleGraph:
    with open(filepath) as f:
        adjacency_list: AdjacencyList = dict()
        edges: EdgeList = list()
        vertices: VertexList = list()
        for line_num, text in enumerate(f):
            if line_num == 0:
                vertices_num, edges_num = text.strip().split(" ")
            else:
                edge = [int(num, base=10) for num in text.strip().split(" ")]

                if edge[0] == edge[1]:
                    adjacency_list[edge[0]].append(edge[0])
                elif edge[0] in adjacency_list:
                    adjacency_list[edge[0]].append(edge[1])
                elif edge[0] not in adjacency_list:
                    adjacency_list[edge[0]] = [edge[1]]
                if edge[0] == edge[1]:
                    pass
                elif edge[1] in adjacency_list:
                    adjacency_list[edge[1]].append(edge[0])
                elif edge[1] not in adjacency_list:
                    adjacency_list[edge[1]] = [edge[0]]

                edges.append(edge)
        vertices = list(adjacency_list.keys())
    return SimpleGraph(adjacency_list, vertices, edges, vertices_num, edges_num)

def build_adjacency_matrix(graph: SimpleGraph) -> Matrix:
    matrix = [[0 for _ in graph.vertices] for _ in graph.vertices]
    for vert, adjacent_verts in graph.adjacency_list.items():
        for adjacent in adjacent_verts:
            if matrix[vert-1][adjacent-1] >= 0:
                if vert == adjacent:
                    matrix[vert-1][adjacent-1] += 2
                else:
                    matrix[vert-1][adjacent-1] += 1
            else:
                matrix[vert-1][adjacent-1] = 0
    return matrix

def build_incident_matrix(graph: SimpleGraph) -> Matrix:
    matrix = [[0 for _ in graph.edges] for _ in graph.vertices]
    for vert in graph.vertices:
        for num_edge, edge in enumerate(graph.edges):
            if vert in edge:
                matrix[vert-1][num_edge] += 1
    return matrix

def print_simple_graph(data: SimpleGraph) -> None:
    print(f"Liczba wierzchołków grafu G wynosi {data.vertices_num}")
    print(F"Zbiór wierzchołków V = {str(data.vertices)}")
    print("")
    print(f"Liczba krawędzi grafu G wynosi {data.edges_num}")
    print(f"Zbiór krawędzi {['-'.join([str(num) for num in edge]) for edge in data.edges]}")

def print_matrix(matrix: Matrix, header: str = "") -> None:
    print(header)
    for row in matrix:
        print(f"| {' '.join([str(num) for num in row])} |")

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    simple_graph: SimpleGraph = get_edges_and_verices_from_file(filepath)
    print_simple_graph(simple_graph)
    adj_matrix: Matrix = build_adjacency_matrix(simple_graph)
    print_matrix(adj_matrix, "Macierz sasiedztwa A =")
    inc_matrix: Matrix = build_incident_matrix(simple_graph)
    print_matrix(inc_matrix, "Macierz incydencji M =")

