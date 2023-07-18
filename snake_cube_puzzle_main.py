import time
from typing import Union
import copy
import numpy as np
import matplotlib.pyplot as plt

from connectivity_graph import ConnectivityGraph


def solve_cube(spacegrid: np.array, snake_remainder: list, start_position: np.array, prev_position: np.array,
               connectivity_graph: ConnectivityGraph = None):
    """
    This recursive function tries filling the next link of the snake.
    If it fails in all directions - it returns False
    If no links remain (stopping condition) if returns the solution.
    If it succeeds on one side it recursively attempts the next step (the return value will determine if it's a success)
    :param spacegrid: An n*n*n array representing the space
    :param snake_remainder: a list of numbers representing the snake's link sizes
    :param prev_position: the cube-before-last position
    :param start_position: the last cube position
    :param step_num: the number of steps required to reach a solution
    :param connectivity_graph: a connectivity graph, if added stops solution if solution reaches discontinuity
    :return:
    """
    if not snake_remainder:
        return spacegrid, 1
    dir_grid = get_directions(start_position, prev_position)
    steps = 0
    for direction in dir_grid:
        success = True
        position = copy.deepcopy(start_position)
        temp_graph = copy.deepcopy(connectivity_graph)
        temp_spacegrid = copy.deepcopy(spacegrid)
        for i in range(snake_remainder[0]):
            steps += 1
            position += direction
            if min(position) < 0 or max(position) > (len(spacegrid) - 1) \
                    or spacegrid[position[0], position[1], position[2]]:
                success = False
                break
            temp_spacegrid[position[0], position[1], position[2]] = \
                spacegrid[start_position[0], start_position[1], start_position[2]] + i + 1
            if temp_graph:
                temp_graph.delete_node((position[0], position[1], position[2]))
        if temp_graph and success:
            success = temp_graph.is_connected()
        if success:
            solution, temp_steps = solve_cube(temp_spacegrid, snake_remainder[1:], position, start_position, temp_graph)
            steps += temp_steps
            if solution is not False:
                return solution, steps
    return False, steps


def get_directions(start_position, prev_position):
    """ get the next possible directions according to the  """
    all_directions = np.array([[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]])
    if prev_position is None:
        return all_directions
    prev_direction = start_position - prev_position
    if prev_direction[0]:
        return all_directions[2:]
    if prev_direction[1]:
        return [all_directions[0], all_directions[1], all_directions[4], all_directions[5]]
    if prev_direction[2]:
        return all_directions[:4]


def solve_snake(snake: list, side_size: int, starting_positions: np.array, check_connectivity: bool = False) \
        -> Union[np.array, bool]:
    """ attempts solving the puzzle from different starting positions, if no positions returns a valid solution
        return false
    """
    space_grid = np.zeros(shape=(side_size, side_size, side_size))
    snake[0] -= 1
    step_num = 0
    for position in starting_positions:
        temp_space_grid = space_grid
        connectivity_graph = ConnectivityGraph(side_size) if check_connectivity else None
        temp_space_grid[position[0], position[1], position[2]] = 1
        if connectivity_graph:
            connectivity_graph.delete_node((position[0], position[1], position[2]))
        solution, steps = solve_cube(temp_space_grid, snake, position, None, connectivity_graph)
        step_num += steps
        if solution is not False:
            return solution, step_num
    return False, step_num


def present_solution(spacegrid: np.array):
    nvoxels = np.zeros((4, 4, 4), dtype=int)
    nvoxels[0:len(spacegrid[0, 0, :]), 0:len(spacegrid[0, :, 0]), 0:len(spacegrid[0, 0, :])] = spacegrid

    facecolors = np.where(spacegrid, '#FFD65DC0', '#7A88CCC0')
    edgecolors = np.where(spacegrid, '#BFAB6E', '#7D84A6')
    filled = np.ones(spacegrid.shape)
    filled_2 = explode(filled)
    fcolors_2 = explode(facecolors)
    ecolors_2 = explode(edgecolors)

    # Shrink the gaps
    x, y, z = np.indices(np.array(filled_2.shape) + 1).astype(float) // 2
    x[0::2, :, :] += 0.1
    y[:, 0::2, :] += 0.1
    z[:, :, 0::2] += 0.1
    x[1::2, :, :] += 0.9
    y[:, 1::2, :] += 0.9
    z[:, :, 1::2] += 0.9

    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(x, y, z, filled_2, facecolors=(1, 214/255, 93/255, 0.1), edgecolors=(1, 214/255, 93/255, 0.3))
    # ax.set_aspect('equal')
    for i, layer in enumerate(spacegrid):
        for j, row in enumerate(layer):
            for k, node in enumerate(row):
                ax.text(i + 0.4, j + 0.4, k + 0.4, str(int(node)), color='black')
    coordinates = np.zeros(shape=(len(spacegrid) ** 3, 3))
    for i in range(len(spacegrid) ** 3):
        point_location = np.nonzero(spacegrid == i + 1)
        coordinates[i, :] = [point_location[0] + 0.5, point_location[1] + 0.5, point_location[2] + 0.5]
    ax.plot(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2])
    plt.axis("off")
    plt.show()


def explode(data):
    size = np.array(data.shape) * 2
    data_e = np.zeros(size - 1, dtype=data.dtype)
    data_e[::2, ::2, ::2] = data
    return data_e


if __name__ == '__main__':
    # side_size, snake = 2, [2, 1, 1, 1, 1, 1, 1]
    # side_size, snake = 3, [3, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 2]
    side_size, snake = 4, [2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1,
                           1, 1, 1, 2, 1, 2, 1, 2, 1, 3, 1, 1, 2, 1, 2]
    cube_num = sum(snake)
    print(f'number of cubes: {cube_num}')
    if cube_num != side_size ** 3:
        print(f'wrong parameters, please check the snake array/side size')
    else:
        print('valid cube')

    starting_positions = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1]])
    t = time.time()
    solution_grid, step_num = solve_snake(snake, side_size, starting_positions, check_connectivity=True)
    print(f'running time: {time.time() - t}')
    if solution_grid is not False:
        print('solution has been reached!')
        print(f'complexity report:\nproblem complexity: 4^{len(snake)} ({4**len(snake)} steps)\nsteps performed: {step_num}')
        present_solution(solution_grid)
    else:
        print(f'no solution found, steps performed: {step_num}')
