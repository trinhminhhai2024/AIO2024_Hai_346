
def max_kernel(num_list , k): 
# Your Code Here
  result = []
  sub_lst = []
  for num in num_list:
    sub_lst.append(num)
    if len(sub_lst) == k:
      result.append(max(sub_lst))
      del sub_lst[0]
  return result
# End Code Here return result

assert max_kernel([3 , 4 , 5 , 1 , -44], 3) == [5, 5, 5] 
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k=3
print(max_kernel(num_list , k))

def char_count(word): 
# Your Code Here 
  char_statistic = {}

  for char in word:
    if char in char_statistic:
      char_statistic[char] += 1
    else:
      char_statistic[char] = 1

# End Code Here 
  return char_statistic

assert char_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1} 

print(char_count('smiles'))

def text_preprocessing(sentence):
    sentence = sentence.lower()
    sentence = sentence.replace('.','').replace(',','')
    words = sentence.split()
    return words

def count_word(file_path):
  counter = {}
# Your Code Here
  with open(file_path, 'r') as f:
    document = f.read()

  word = text_preprocessing(document)
  counter = {}
  for w in word:
    if w in counter:
      counter[w] +=1
    else:
      counter[w] = 1
#print(counter)
# End Code Here
  return counter
#!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
file_path = '/content/P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3 
print(result['man'])

def levenshtein_distance(token1 , token2): 
 # Your Code Here
    distances = []
    for idx in range(len(token1)+1):
      row = [0] * (len(token2)+1)
      distances.append(row)
    print(distances)

    for idx in range(len(token1)+1):
      distances[idx][0] = idx

    for idx in range(len(token2)+1):
      distances[0][idx] = idx

    del_cost = 0
    ins_cost = 0
    sub_cost = 0
    
    for idx in range(1, len(token1)+1):
      for jdx in range(1, len(token2)+1):
        if token1[idx-1] == token2[jdx-1]:
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

    levenshtein_distance = distances[len(token1)][len(token2)]
    print(distances)
    return levenshtein_distance

assert levenshtein_distance("hi", "hello") == 4.0 
print(levenshtein_distance("hola", "hello"))

def check_the_number(N): 
  list_of_numbers = [] 
  result = ""
  for i in range(1, 5):
   #Your code here
    list_of_numbers.append(i)
  
  if N in list_of_numbers: 
      result = "True"
  else: 
      result = "False"
  return result
N=7
assert check_the_number(N) == "False"
N=2
result = check_the_number(N) 
print(result)

def my_function(data, max, min): 
  result = []
  for i in data: #Your code here
    if i < min:
      result.append(min)
    elif i > max: 
      result.append(max)
    else: 
      result.append(i)
  return result

my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max = max, min = min, data = my_list) == [1, 1, 1, 0, 1] 
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max = max, min = min, data = my_list))

def my_function(x, y): #Your code here
  x.extend(y)
  return x
#Su dung extend de noi y vao x #return x

list_num1 = ['a', 2, 5] 
list_num2 = [1, 1] 
list_num3 = [0, 0]

assert my_function(list_num1, my_function(list_num2 ,list_num3))
list_num1 = [1, 2] 
list_num2 = [3, 4] 
list_num3 = [0, 0]

print(my_function(list_num1 ,my_function(list_num2 ,list_num3)))

def find_min(n):
    min_value = n[0]
    for value in n:
        if value < min_value:
            min_value = value
            
    return min_value

my_list = [1, 22, 93, -100]
assert find_min(my_list) == -100

my_list = [1, 2, 3, -1]
print(find_min(my_list)) 

def find_max(n):
    max_value = n[0]
    for value in n:
        if value > max_value:
            max_value = value
            
    return max_value

my_list = [1001, 9, 100, 0]
assert find_max(my_list) == 1001
my_list = [1, 9, 9, 0] 
print(find_max(my_list))

def My_function(integers , number = 1):
  result =[]
  for i in integers:
    if i == number:
      result.append(True)
    else:
      result.append(False)
  return result


my_list = [1, 3, 9, 4]
#assert My_function(my_list , -1) == False
my_list = [1, 2, 3, 4] 
print(My_function(my_list , 2))

def My_function(integers , number = 1):
  result = False
  for i in integers:
    if i == number:
      result = True
      break
  return result


my_list = [1, 3, 9, 4]
assert My_function(my_list , -1) == False
my_list = [1, 2, 3, 4]
print(My_function(my_list , 2))

def my_function(list_nums = [0, 1, 2]): 
  var = 0
  for i in list_nums: 
    var += i
  return var/len(list_nums)
assert my_function([4, 6, 8]) == 6 
print(my_function())

def my_function(data): 
  var = []
  for i in data:
    if i%3 == 0:
      var.append(i)
  return var
assert my_function([3, 9, 4, 5]) == [3, 9] 
print(my_function([1, 2, 3, 5, 6]))

def compute_factorial(y): 
  var = 1
  while(y > 1): #Your code here
    var *= y
    y -= 1
  return var
assert compute_factorial(8) == 40320 
print(compute_factorial(4))

def reversing_char(x): #your code here
  return x[::-1]
x = 'I can do it'
assert reversing_char(x)== "ti od nac I"
x = 'apricot'
print(reversing_char(x))


def function_helper(x):
  result = 0
#Your code here
#Neu x>0 tra ve ’T’, nguoc lai tra ve ’N’
  if x > 0:
    result = 'T'
  else:
    result = 'N'
  return result

def my_function(data):
  res = [function_helper(x) for x in data] 
  return res
data = [10, 0, -10, -1]
assert my_function(data) == ['T','N','N','N']

data = [2, 3, 5, -1] 
print(my_function(data))

def function_helper(x, data): 
  for i in data:
#Your code here
    if x == i: return 0
#Neu x == i thi return 0
  else:
    return 1

def my_function(data):
  res = []
  for i in data:
    if function_helper(i, res): res.append(i)
  return res

lst = [10, 10, 9, 7, 7]
assert my_function(lst)==[10, 9, 7]
lst = [9, 9, 8, 1, 1] 
print(my_function(lst))
