num_lst = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1] 
k=3
result = []
sub_lst = []

for num in num_lst:
  sub_lst.append(num)
  if len(sub_lst) == k:
    result.append(max(sub_lst))
    del sub_lst[0]

print(result)

