from math import inf

class FlowNetworkGraph:
    def __init__(self, residual, source, sink):
        self.residual = residual
        self.length = len(residual)
        self.source = source
        self.sink = sink
        self.delta = 0 # dummie

    def update_residual_matrix(self, path):

        max_path_flow = inf
        node = self.sink

        path_vertices = [node]

        while True:

            node, max_capacity = path[node]
            max_path_flow = min(max_capacity, max_path_flow)
            path_vertices.append(node)

            if node == self.source:
                break


        for ind in range(0, len(path_vertices) - 1):
            from_node, to_node = path_vertices[ind + 1], path_vertices[ind]

            self.residual[from_node][to_node] -= max_path_flow
            self.residual[to_node][from_node] += max_path_flow

        return max_path_flow

    def update_residual_list(self, path):

        if not path:
            return False

        max_path_flow = inf
        node = self.sink

        path_vertices = [node]

        while True:

            node, max_capacity = path[node]
            max_path_flow = min(max_capacity, max_path_flow)
            path_vertices.append(node)

            if node == self.source:
                break


        for ind in range(0, len(path_vertices) - 1):
            from_node, to_node = path_vertices[ind + 1], path_vertices[ind]


            for item in self.residual[from_node]:
                if item[0] == to_node:
                    item[1] -= max_path_flow

            for item in self.residual[to_node]:
                if item[0] == from_node:
                    item[1] += max_path_flow
            else:
                self.residual[to_node].append([from_node, max_path_flow])

        return max_path_flow






