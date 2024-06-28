target = "presentation"
source = "presenton"

def initialize_distances(source, target):
    distances = [[0] * (len(target) + 1) for _ in range(len(source) + 1)]
    
    for idx in range(len(source) + 1):
        distances[idx][0] = idx
    
    for idx in range(len(target) + 1):
        distances[0][idx] = idx
    
    return distances

def calculate_edit_distance(distances, source, target):
    for idx in range(1, len(source) + 1):
        for jdx in range(1, len(target) + 1):
            if source[idx - 1] == target[jdx - 1]:
                distances[idx][jdx] = distances[idx - 1][jdx - 1]
            else:
                del_cost = distances[idx - 1][jdx] + 1
                ins_cost = distances[idx][jdx - 1] + 1
                sub_cost = distances[idx - 1][jdx - 1] + 1
                distances[idx][jdx] = min(del_cost, ins_cost, sub_cost)
    
    return distances[len(source)][len(target)]

def edit_distance(source, target):
    distances = initialize_distances(source, target)
    result = calculate_edit_distance(distances, source, target)
    return result

print(edit_distance(source, target)) 