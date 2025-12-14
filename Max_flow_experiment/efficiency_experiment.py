import copy

from algorithms_garage import *
import timeit
from math import log
from Gnp import *

super_thin1 = lambda x: 2/(x - 1)
super_thin2 = lambda x: 3/(x - 1)

thin = lambda x: log(x) / (x - 1)

moderate1 = lambda x: 8/(x - 1)
moderate2 = lambda x: 16/(x - 1)

dense1 = lambda x: x/(4*(x-1))
dense2 = lambda x: x/(2*(x-1))

near_complete1 = 0.75
near_complete2 = 0.90

vert_numbers = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
densities = [super_thin1, super_thin2, thin, moderate1, moderate2, dense1, dense2, near_complete1, near_complete1, near_complete2]
runs = 100
lambda_runs = 1
max_capacity = 100

with open("bfs_matrix.txt", "w") as file:
    pass
with open("dfs_matrix.txt", "w") as file:
    pass
with open("scaling_matrix.txt", "w") as file:
    pass
with open("dinic_matrix.txt", "w") as file:
    pass
with open("bfs_list.txt", "w") as file:
    pass
with open("dfs_list.txt", "w") as file:
    pass
with open("scaling_list.txt", "w") as file:
    pass
with open("dinic_list.txt", "w") as file:
    pass

for number in vert_numbers:
    for density in densities:
        if callable(density):
            density = density(number)

        with open("bfs_matrix.txt", "a") as file:
            file.write(f"\nnumber: {number} --- density: {density}\n")
        with open("dfs_matrix.txt", "a") as file:
            file.write(f"\nnumber: {number} --- density: {density}\n")
        with open("scaling_matrix.txt", "a") as file:
            file.write(f"\nnumber: {number} --- density: {density}\n")
        with open("dinic_matrix.txt", "a") as file:
            file.write(f"\nnumber: {number} --- density: {density}\n")
        with open("bfs_list.txt", "a") as file:
            file.write(f"\nnumber: {number} --- density: {density}\n")
        with open("dfs_list.txt", "a") as file:
            file.write(f"\nnumber: {number} --- density: {density}\n")
        with open("scaling_list.txt", "a") as file:
            file.write(f"\nnumber: {number} --- density: {density}\n")
        with open("dinic_list.txt", "a") as file:
            file.write(f"\nnumber: {number} --- density: {density}\n")

        for iters in range(0, runs):
            source, sink = random_s_t(number)

            random_graph_matrix =  generate_graph(number, density, max_capacity, source, sink)

            random_graph_list = matrix_to_list(random_graph_matrix)

            one_run_list = copy.deepcopy(random_graph_list)
            timing = timeit.timeit(lambda: ff_dfs_list(one_run_list, source, sink), number=lambda_runs) / lambda_runs
            with open("dfs_list.txt", "a") as file:
                file.write(f"{timing:.20f}\n")


            one_run_list = copy.deepcopy(random_graph_list)
            timing = timeit.timeit(lambda: ff_bfs_list(one_run_list, source, sink), number=lambda_runs) / lambda_runs
            with open("bfs_list.txt", "a") as file:
                file.write(f"{timing:.20f}\n")


            one_run_list = copy.deepcopy(random_graph_list)
            timing = timeit.timeit(lambda: ff_bfs_scaling_list(one_run_list, source, sink), number=lambda_runs) / lambda_runs
            with open("scaling_list.txt", "a") as file:
                file.write(f"{timing:.20f}\n")


            one_run_list = copy.deepcopy(random_graph_list)
            timing = timeit.timeit(lambda: ff_dinic_list(one_run_list, source, sink), number=lambda_runs) / lambda_runs
            with open("dinic_list.txt", "a") as file:
                file.write(f"{timing:.20f}\n")





            one_run_matrix = copy.deepcopy(random_graph_matrix)
            timing = timeit.timeit(lambda: ff_bfs_matrix(one_run_matrix, source, sink), number=lambda_runs) / lambda_runs
            with open("bfs_matrix.txt", "a") as file:
                file.write(f"{timing:.20f}\n")


            one_run_matrix = copy.deepcopy(random_graph_matrix)
            timing = timeit.timeit(lambda: ff_dfs_matrix(one_run_matrix, source, sink), number=lambda_runs) / lambda_runs
            with open("dfs_matrix.txt", "a") as file:
                file.write(f"{timing:.20f}\n")


            one_run_matrix = copy.deepcopy(random_graph_matrix)
            timing = timeit.timeit(lambda: ff_bfs_scaling_matrix(one_run_matrix, source, sink), number=lambda_runs) / lambda_runs
            with open("scaling_matrix.txt", "a") as file:
                file.write(f"{timing:.20f}\n")


            one_run_matrix = copy.deepcopy(random_graph_matrix)
            timing = timeit.timeit(lambda: ff_dinic_matrix(one_run_matrix, source, sink), number=lambda_runs) / lambda_runs
            with open("dinic_matrix.txt", "a") as file:
                file.write(f"{timing:.20f}\n")







