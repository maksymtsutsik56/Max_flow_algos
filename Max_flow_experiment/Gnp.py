import random
import csv


def random_s_t(vert_number):
    while True:
        source = random.randint(0, vert_number - 1)
        sink = random.randint(0, vert_number - 1)

        if source != sink:
            return source, sink


def generate_graph(vert_number, density, max_capacity, source, sink):
    while True:
        graph_matrix = []

        for row in range(0, vert_number):
            row_lst = []
            for column in range(0, vert_number):
                possibility = random.random()

                if possibility < density and column != row:
                    random_capacity = random.randint(1, max_capacity)
                    row_lst.append(random_capacity)
                else:
                    row_lst.append(0)

            graph_matrix.append(row_lst)


        stack = [source]
        visited = [False] * vert_number

        while stack:
            current_vertex = stack.pop()

            if current_vertex == sink:
                with open("../Codes/graph_matrix_sample", "w") as file:
                    writer = csv.writer(file)
                    writer.writerows(graph_matrix)
                return graph_matrix

            for v, cap in enumerate(graph_matrix[current_vertex]):
                if not visited[v] and cap > 0:
                    stack.append(v)
                    visited[v] = True


def matrix_to_list(matrix):
    list_of_lists = []

    for row in matrix:

        adj_list = []
        for vert, cap in enumerate(row):
            if cap > 0:
                adj_list.append([vert, cap])
        list_of_lists.append(adj_list)

    return list_of_lists









