"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # create the new key with the vertex ID
        # set the value to an empty set (no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # find vertex v1 in our vertices
        # add v2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting_vertex
        queue = [starting_vertex]
        # create an empty set to track visited vertices
        visited = set()

        # while the queue is not empty
        while queue:
            # get current vertex (dequeue)
            current = queue.pop(0)
            # check if the current vertex has not been visited
            if current not in visited:
                # print the current vertex
                print(current)
                # mark the current vertex as visited
                visited.add(current)

                # queue up all the current vertex's neighbors (so we can visit them next)
                queue.extend(self.get_neighbors(current))

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a stack with the starting_vertex
        stack = [starting_vertex]
        # create an empty set to track visited vertices
        visited = set()

        # while the stack is not empty
        while stack:
            # get current vertex (pop from stack)
            current = stack.pop(-1)
            # check if the current vertex has not been visited
            if current not in visited:
                # print the current vertex
                print(current)
                # mark the current vertex as visited
                visited.add(current)

                # push up all the current vertex's neighbors (so we can visit them next)
                stack.extend(self.get_neighbors(current))

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # base case: print current vertex
        visited.add(starting_vertex)
        print(starting_vertex)
        # recursive case, dft on neighbors if not already seen
        for next_vertex in self.get_neighbors(starting_vertex):
            if next_vertex not in visited:
                self.dft_recursive(next_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue the PATH TO starting_vertex
        queue = Queue()
        queue.enqueue({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        # can also do queue.enqueue([starting_vertex]), but we're being explicit
        # create an empty set to track visited vertices
        visited_vertices = set()

        # while the queue is not empty
        while queue.size() > 0:
            # get current vertex PATH (dequeue)
            current_obj = queue.dequeue()
            current_path = current_obj['path']
            # set the current vertex
            current_vertex = current_obj['current_vertex']

            # check if the current vertex has not been visited
            if current_vertex not in visited_vertices:
                # check if the current vertex is destination_vertex
                if current_vertex == destination_vertex:
                    # if it is, stop and return
                    return current_path

                # mark the current vertex as visited
                visited_vertices.add(current_vertex)

                # queue up NEW paths with each neighbor:
                for neighbor_vertex in self.get_neighbors(current_vertex):
                    # take current path
                    # append the neighbor to it
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    # queue up NEW path
                    queue.enqueue({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty stack and push the PATH TO starting_vertex
        stack = Stack()
        stack.push({
            'current_vertex': starting_vertex,
            'path': [starting_vertex]
        })
        # can also do stack.push([starting_vertex]), but we're being explicit
        # create an empty set to track visited vertices
        visited_vertices = set()

        # while the stack is not empty
        while stack.size() > 0:
            # get current vertex PATH (pop)
            current_obj = stack.pop()
            current_path = current_obj['path']
            # set the current vertex
            current_vertex = current_obj['current_vertex']

            # check if the current vertex has not been visited
            if current_vertex not in visited_vertices:
                # check if the current vertex is destination_vertex
                if current_vertex == destination_vertex:
                    # if it is, stop and return
                    return current_path

                # mark the current vertex as visited
                visited_vertices.add(current_vertex)

                # push NEW paths with each neighbor:
                for neighbor_vertex in self.get_neighbors(current_vertex):
                    # take current path
                    # append the neighbor to it
                    new_path = list(current_path)
                    new_path.append(neighbor_vertex)
                    # push NEW path
                    stack.push({
                        'current_vertex': neighbor_vertex,
                        'path': new_path
                    })

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=list()):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # base case
        if starting_vertex == destination_vertex:
            return path
        # recursive case
        # recurse for each neighbor if not already seen
        for next_vertex in self.get_neighbors(starting_vertex):
            if next_vertex not in visited:
                new_path = self.dfs_recursive(
                    next_vertex, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
