target = "presentation"
source = "presenton"

def edit_distance(source, target):
    distances = []
    for idx in range(len(source)+1):
      row = [0] * (len(target)+1)
      distances.append(row)
    print(distances)

    for idx in range(len(source)+1):
      distances[idx][0] = idx

    for idx in range(len(target)+1):
      distances[0][idx] = idx

    del_cost = 0
    ins_cost = 0
    sub_cost = 0
    
    for idx in range(1, len(source)+1):
      for jdx in range(1, len(target)+1):
        if source[idx-1] == target[jdx-1]:
          distances [idx][jdx] = distances[idx-1][jdx-1]
        else:
          del_cost = distances[idx-1][jdx]
          ins_cost = distances[idx][jdx-1]
          sub_cost = distances[idx-1][jdx-1]

          if (del_cost <= ins_cost) and (del_cost <= sub_cost):
            distances[idx][jdx] = del_cost + 1
          elif (ins_cost <= del_cost) and (ins_cost <=sub_cost):
            distances[idx][jdx] = ins_cost + 1
          else:
            distances[idx][jdx] = sub_cost + 1

    edit_distance = distances[len(source)][len(target)]
    print(distances)
    return edit_distance


edit_distance(source, target)

  

