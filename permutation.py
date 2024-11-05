def sjt(nums):
    perm = nums
    direction = [0] * len(nums)
    permutations = [perm.copy()]
    largest_mobile = -2

    while largest_mobile != -1:
        largest_mobile = -1
        index = -1
        for i in range(len(perm)):
            if (direction[i] == 0 and i > 0 and perm[i] > perm[i - 1]) or (direction[i] == 1 and i < len(perm) - 1 and perm[i] > perm[i + 1]):
                if perm[i] > largest_mobile:
                    largest_mobile = perm[i]
                    index = i
        if largest_mobile != -1:
            index = swap_largest_movable(direction, index, perm)
            update_direction(perm, direction, largest_mobile)
            permutations.append(perm.copy())

    return permutations

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def update_direction(perm, direction, largest_mobile):
    for i in range(len(perm)):
        if perm[i] > largest_mobile:
            direction[i] = 1 - direction[i]

def swap_largest_movable(direction, index, perm):
    if direction[index] == 0:
        swap(perm, index, index - 1)
        swap(direction, index, index - 1)
        index -= 1
    else:
        swap(perm, index, index + 1)
        swap(direction, index, index + 1)
        index += 1
    return index

def detect_hamiltonian_cycle(graph):
    nums = [i for i in range(len(graph))]
    permutations = sjt(nums)
    for perm in permutations:
        if is_hamiltonian_cycle(graph, perm):
            return perm + [perm[0]]
    return -1

def is_hamiltonian_cycle(graph, perm):
    for i in range(len(perm) - 1):
        if perm[i + 1] not in graph[perm[i]][1]:
            return False
    if 0 not in graph[perm[-1]][1]:
        return False

    return True