import sys
import z1

# Types
from z1 import SimpleGraph

if not sys.argv[1:]:
    raise RuntimeError('Nie podano ścieżki do pliku')

def print_adj_list(graph: SimpleGraph) -> None:
    for key, val in graph.adjacency_list.items():
        print(f"{str(key)} -> {', '.join([str(vert) for vert in val])}")

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    simple_graph: SimpleGraph = z1.get_edges_and_verices_from_file(filepath)
    print_adj_list(simple_graph)