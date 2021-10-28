import sys
from typing import List
import z1
from z1 import SimpleGraph

# Types
VertexDegreeList = List[List[int]]

if not sys.argv[1:]:
    raise RuntimeError('Nie podano ścieżki do pliku')

def get_graph_degree(graph: SimpleGraph) -> int:
    return len(graph.vertices)

def get_graph_size(graph: SimpleGraph) -> int:
    return len(graph.edges)

def get_vertices_degree(graph: SimpleGraph) -> VertexDegreeList:
    vertices_degree = []
    for vert, adj_verts in graph.adjacency_list.items():
        vertices_degree.append((vert, len(adj_verts)))
    return vertices_degree

def print_vertices_degree(vert_deg: VertexDegreeList) -> None:
    for vert, deg in vert_deg:
        print(f"deg({vert}) = {deg}")

def get_series_of_vertices_degree(vert_deg: VertexDegreeList) -> VertexDegreeList:
    return sorted([deg for _ , deg in vert_deg])

def print_series_of_vertices_degree(vert_deg_series: List[int]) -> None:
    print(f"Ciag stopni grafu G: {', '.join([str(num) for num in vert_deg_series])}")

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    simple_graph: SimpleGraph = z1.get_edges_and_verices_from_file(filepath)
    print(f"Rzad grafu G wynosi {get_graph_degree(simple_graph)}")
    print(f"Rozmiar grafu G wynosi {get_graph_size(simple_graph)}")
    vert_deg = get_vertices_degree(simple_graph)
    print_vertices_degree(vert_deg)
    vert_deg_series = get_series_of_vertices_degree(vert_deg)
    print_series_of_vertices_degree(vert_deg_series)
