from collections import deque

class UndirectedGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        elif v not in self.graph[u]:
            self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = [u]
        elif u not in self.graph[v]:
            self.graph[v].append(u)

    def remove_vertex(self, v):
        if v in self.graph:
            connected_vertices = self.graph[v]
            del self.graph[v]
            for vertex in connected_vertices:
                self.graph[vertex].remove(v)

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def is_adjecent(self,u,v):
        if u in self.graph  and v in self.graph[u]:
            return True
        return False

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def dfs(self, start):
        visited = {v: False for v in self.graph}
        stack = [start]
        result = []

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                stack.extend(reversed(self.graph[vertex]))  # Add neighbors to stack

        return result
    
    def bfs(self, start):
        visited = {v: False for v in self.graph}
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            if not visited[vertex]:
                visited[vertex] = True
                result.append(vertex)
                queue.extend(self.graph[vertex])  # Add neighbors to queue

        return result
        
# Example usage
ug = UndirectedGraph()
ug.add_vertex('A')
ug.add_vertex('B')
ug.add_vertex('C')
ug.add_edge('A', 'B')
ug.add_edge('A', 'C')
ug.add_edge('B', 'C')

print("\nUndirected Graph:")
ug.display()
print("DFS:", ug.dfs("A"))
print("BFS:", ug.bfs("A"))


class Graph:
    def __init__(self) -> None:
        self.graph={}
    def add_vertex(self,v):
        if v not in self.graph:
            self.graph[v]=[]
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[v]
        elif v not in self.graph[u]:
            self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v]=[u]
        elif u not in self.graph[v]:
            self.graph[v].append(u)
    def remove_v(self,v):
        if v in self.graph:
            connected=self.graph[v]
            del self.graph[v]
            for vertex in connected:
                self.graph[vertex].remove(v)
    def remove_edge(self,u,v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def dispaly(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")


  