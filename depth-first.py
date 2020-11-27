
graph = {"A": ["B", "D", "E"],
         "B": ["A", "C", "D"],
         "C": ["B", "G"],
         "D": ["A", "B", "E", "F"],
         "E": ["A", "D"],
         "F": ["D"],
         "G": ["C"]}

visited_nodes = []

def dfs(graph, currentVertex, visited):
    visited_nodes.append(currentVertex)
    for vertex in graph[currentVertex]:
        if vertex not in visited:
            print(vertex)
            dfs(graph, vertex, visited)
    return visited

print(dfs(graph, "A", visited_nodes))

# The Depth-First Traversal visits every node and edge so...
# The number of operations is therefor n + e
# n -> number of verticies, e -> number of edges
# So this means O(n) (Big-O-Notation)

# However in a graph with maximum edges, the adjecency matrix is full
# So n edges and n^2 edges, therefor giving... giving vn^2 + n
# The Time Complexity: O(n^2)
# This is the max amount of searches to be made.