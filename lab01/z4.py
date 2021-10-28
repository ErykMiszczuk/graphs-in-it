import sys
from typing import List
import z1
import z2

# Types
from z1 import Matrix, SimpleGraph
IsFullGraph = (bool, List[List[int]])

if not sys.argv[1:]:
    raise RuntimeError('Nie podano ścieżki do pliku')

def is_full_graph(matrix: Matrix) -> IsFullGraph:
    missing: List[(int, int)] = []
    full = True
    rows = len(matrix)
    cols = len(matrix[0])
    for num_row in range(rows):
        for num_col in range(num_row, cols):
            if num_row == num_col:
                continue
            if matrix[num_row][num_col] < 1:
                full = False
                missing.append((num_row + 1, num_col + 1))

    return (full, missing)

def print_is_full_graph(is_full: IsFullGraph) -> None:
    print(f"Graf G { 'jest' if is_full[0] else 'nie jest'} grafem pełnym.")
    print(f"Krawedzie dopelnienia grafu G: {['-'.join([str(vertex) for vertex in edge]) for edge in is_full[1]]}")

if __name__ == "__main__":
    filepath: str = sys.argv[1]
    simple_graph: SimpleGraph = z1.get_edges_and_verices_from_file(filepath)
    matrix: Matrix = z1.build_adjacency_matrix(simple_graph)
    is_simple: bool = is_full_graph(matrix)
    print_is_full_graph(is_simple)