import sys
import z1
import z2

# Types
from z1 import Matrix, SimpleGraph

if not sys.argv[1:]:
    raise RuntimeError('Nie podano ścieżki do pliku')

def is_simple_graph(matrix: Matrix) -> bool:
    for row in matrix:
        for cell in row:
            if cell > 1:
                return False
    return True

def print_is_simple_graph(is_simple: bool) -> None:
    print(f"Graf G { 'jest' if is_simple else 'nie jest'} grafem prostym.")

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    simple_graph: SimpleGraph = z1.get_edges_and_verices_from_file(filepath)
    matrix: Matrix = z1.build_adjacency_matrix(simple_graph)
    is_simple: bool = is_simple_graph(matrix)
    print_is_simple_graph(is_simple)