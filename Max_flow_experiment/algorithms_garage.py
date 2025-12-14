import timeit
from collections import deque
from Skelet import FlowNetworkGraph
from math import inf

def ff_bfs_matrix(residual, source, sink):
    def bfs():
        source = object1.source
        sink = object1.sink

        queue = deque() # main queue for BFS search
        queue.append(source)

        path = [-1] * object1.length
        path[source] = -2

        while queue:
            current_vertex = queue.popleft()

            if current_vertex == sink:
                return path

            for v, capacity_to in enumerate(object1.residual[current_vertex]):
                if path[v] == -1 and capacity_to > 0:
                    queue.append(v)
                    path[v] = (current_vertex, capacity_to)
        else:
            return False

    object1 = FlowNetworkGraph(residual, source, sink)
    total_flow = 0

    while True:
        path = bfs()
        if not path:
            break
        total_flow += object1.update_residual_matrix(path)

    return total_flow

def ff_bfs_scaling_matrix(residual, source, sink):
    def bfs_delta():
        source = object1.source
        sink = object1.sink

        queue = deque()  # main queue for BFS search
        queue.append(source)

        path = [-1] * object1.length
        path[source] = -2

        while queue:
            current_vertex = queue.popleft()

            if current_vertex == sink:
                return path

            for v, capacity_to in enumerate(object1.residual[current_vertex]):
                if path[v] == -1 and capacity_to >= object1.delta:
                    queue.append(v)
                    path[v] = (current_vertex, capacity_to)
        else:
            return False

    object1 = FlowNetworkGraph(residual, source, sink)
    total_flow = 0

    max_capacity = 0
    for row in object1.residual:
        for capacity in row:
            if capacity > max_capacity:
                max_capacity = capacity
    delta = 1
    while True:
        if delta * 2 <= max_capacity:
            delta *= 2
        else:
            object1.delta = delta
            break


    while True:
        path = bfs_delta()
        if not path:
            if object1.delta > 1:
                object1.delta //= 2
                continue
            else:
                break
        total_flow += object1.update_residual_matrix(path)

    return total_flow

def ff_dfs_matrix(residual, source, sink):
    def dfs():
        source = object1.source
        sink = object1.sink

        stack = [source] # Creating stack for storing vertices

        path = [-1] * object1.length
        path[source] = -2

        while stack:
            current_vertex = stack.pop()

            if current_vertex == sink:
                return path

            for v, capacity_to in enumerate(object1.residual[current_vertex]):
                if path[v] == -1 and capacity_to > 0:
                    stack.append(v)
                    path[v] = (current_vertex, capacity_to)
        else:
            return False

    object1 = FlowNetworkGraph(residual, source, sink)
    total_flow = 0

    while True:
        path = dfs()
        if not path:
            break
        total_flow += object1.update_residual_matrix(path)

    return total_flow


def ff_bfs_list(residual, source, sink):
    def bfs_list():
        source = object1.source
        sink = object1.sink

        queue = deque() # main queue for BFS search
        queue.append(source)

        path = [-1] * object1.length
        path[source] = -2

        while queue:
            current_vertex = queue.popleft()

            if current_vertex == sink:
                return path

            for v, capacity_to in object1.residual[current_vertex]:
                if path[v] == -1 and capacity_to > 0:
                    queue.append(v)
                    path[v] = (current_vertex, capacity_to)
        else:
            return False

    object1 = FlowNetworkGraph(residual, source, sink)
    total_flow = 0

    while True:
        path = bfs_list()
        if not path:
            break
        total_flow += object1.update_residual_list(path)
    return total_flow

def ff_bfs_scaling_list(residual, source, sink):
    def bfs_delta_list():
        source = object1.source
        sink = object1.sink

        stack = [source] # main queue for BFS search

        path = [-1] * object1.length
        path[source] = -2

        while stack:
            current_vertex = stack.pop()

            if current_vertex == sink:
                return path

            for v, capacity_to in object1.residual[current_vertex]:
                if path[v] == -1 and capacity_to > 0:
                    stack.append(v)
                    path[v] = (current_vertex, capacity_to)
        else:
            return False

    object1 = FlowNetworkGraph(residual, source, sink)
    total_flow = 0

    max_capacity = 0

    for row in object1.residual:
        for edge in row:
            capacity = edge[1]
            if capacity > max_capacity:
                max_capacity = capacity

    delta = 1
    while True:
        if delta * 2 <= max_capacity:
            delta *= 2
        else:
            break

    object1.delta = delta

    while True:
        path = bfs_delta_list()
        if not path:
            if object1.delta > 1:
                object1.delta //= 2
                continue
            else:
                break
        total_flow += object1.update_residual_list(path)

    return total_flow

def ff_dfs_list(residual, source, sink):
    def dfs_list():
        source = object1.source
        sink = object1.sink

        stack = [source] # main queue for BFS search

        path = [-1] * object1.length
        path[source] = -2

        while stack:
            current_vertex = stack.pop()

            if current_vertex == sink:
                return path

            for v, capacity_to in object1.residual[current_vertex]:
                if path[v] == -1 and capacity_to > 0:
                    stack.append(v)
                    path[v] = (current_vertex, capacity_to)
        else:
            return False

    object1 = FlowNetworkGraph(residual, source, sink)
    total_flow = 0

    while True:
        path = dfs_list()
        if not path:
            break
        total_flow += object1.update_residual_list(path)
    return total_flow


def ff_dinic_matrix(residual, source, sink):
    def level_graph_matrix():
        source = object1.source
        sink = object1.sink

        queue = deque()
        queue.append(source)

        level = [-1] * object1.length
        level[source] = 0

        while queue:
            current_vertex = queue.popleft()
            for v, capacity_to in enumerate(object1.residual[current_vertex]):
                if level[v] == -1 and capacity_to > 0:
                    queue.append(v)
                    level[v] = level[current_vertex] + 1

        if level[sink] != -1:
            return level
        else:
            return False

    def dfs_push_matrix(choice: list, current_vertex, current_flow, level: list):
        if current_flow == 0:
            return 0

        if current_vertex == object1.sink:
            return current_flow

        while choice[current_vertex] < object1.length:

            next_vertex = choice[current_vertex]
            next_flow = object1.residual[current_vertex][next_vertex]

            if level[next_vertex] == level[current_vertex] + 1 and next_flow > 0:

                pushed_flow = min(current_flow, next_flow)
                path_flow = dfs_push_matrix(choice, next_vertex, pushed_flow, level)

                if path_flow > 0:
                    object1.residual[current_vertex][next_vertex] -= path_flow
                    object1.residual[next_vertex][current_vertex] += path_flow

                    return path_flow

            choice[current_vertex] += 1

        return 0

    object1 = FlowNetworkGraph(residual, source, sink)
    total_flow = 0

    if object1.source == object1.sink:
        return "wtf dude ???"

    level = level_graph_matrix()

    while level:
        choice = [0] * object1.length

        while True:
            flow = dfs_push_matrix(choice, object1.source, inf, level)

            if flow == 0:
                break

            total_flow += flow
        level = level_graph_matrix()

    return total_flow

def ff_dinic_list(residual, source, sink):
    def level_graph_list():
        source = object1.source
        sink = object1.sink

        queue = deque()
        queue.append(source)

        level = [-1] * object1.length
        level[source] = 0

        while queue:
            current_vertex = queue.popleft()
            for v, capacity_to in object1.residual[current_vertex]:
                if level[v] == -1 and capacity_to > 0:
                    queue.append(v)
                    level[v] = level[current_vertex] + 1

        if level[sink] != -1:
            return level
        else:
            return False

    def dfs_push_list(choice: list, current_vertex, current_flow, level: list):
        if current_flow == 0:
            return 0

        if current_vertex == object1.sink:
            return current_flow

        while choice[current_vertex] < len(object1.residual[current_vertex]):
            chosen = choice[current_vertex]

            next_vertex, next_flow = object1.residual[current_vertex][chosen]

            if level[next_vertex] == level[current_vertex] + 1 and next_flow > 0:

                pushed_flow = min(current_flow, next_flow)
                path_flow = dfs_push_list(choice, next_vertex, pushed_flow, level)

                if path_flow > 0:

                    object1.residual[current_vertex][chosen][1] -= path_flow

                    for item in object1.residual[next_vertex]:
                        if item[0] == current_vertex:
                            item[1] += path_flow
                            break
                    else:
                        object1.residual[next_vertex].append([current_vertex, path_flow])

                    return path_flow

            choice[current_vertex] += 1

        return 0

    object1 = FlowNetworkGraph(residual, source, sink)
    total_flow = 0

    if object1.source == object1.sink:
        return "wtf dude ???"

    level = level_graph_list()

    while level:
        choice = [0] * object1.length

        while True:
            flow = dfs_push_list(choice, object1.source, inf, level)

            if flow == 0:
                break

            total_flow += flow
        level = level_graph_list()

    return total_flow



