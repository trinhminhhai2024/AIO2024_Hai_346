import math

def is_number(n):
      try:
        float(n)
      except ValueError:
        return False
      return True

def act_func(x, af_name):

  def calc_sig(x):
    result = 1 / (1 + math.e ** (-x))
    return result

  def calc_relu(x):
    result = max(0, x)
    return result

  def calc_elu(x):
    alpha = 0.01
    if x <= 0:
        result = alpha * (math.e ** x - 1)
    else:
        result = x
    return result
    
  result = None
    
  if af_name == "sig":
        result = calc_sig(x)
  elif af_name == "relu":
        result = calc_relu(x)
  elif af_name == "elu":
        result = calc_elu(x)
  return result

def solution():
    x = input("Enter x value: ")
    af_name = input("Activation function name (sig, relu, elu): ")

    if not is_number (x):
        print("x must be a number")
        return None

    x = float(x)
    valid_func_name = ["sig", "relu", "elu"]
    if af_name not in valid_func_name:
        print(f"{af_name} is not supported")
        return None

    result = act_func(x, af_name)
    print(f"{af_name}({x}) = {result}")

solution()


