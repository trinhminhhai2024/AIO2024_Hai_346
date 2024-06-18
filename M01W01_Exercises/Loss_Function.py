import random
import math

def calc_loss_func():
  def calc_ae(y,y_hat):
    difference = y - y_hat
    result = abs(difference)
    return result
  
  def calc_se(y,y_hat):
    difference = y - y_hat
    result = (difference)**2
    return result
  
  n = input ("Enter number of sample, n:")
  if not n.isnumeric():
    print("number of samples must be an integer number")
    return
  loss_name = input("Enter name of loss function (mae, mse, rmse):")
  
  valid_func_name = ["mae", "mse", "rmse"]
  if loss_name not in valid_func_name:
      print(f"{loss_name} is not supported")
      return None
  
  final_loss = 0
  n = int(n)
  for i in range(n):
    y = random.random()
    y_hat = random.random()
    if loss_name == "mae":
      loss = calc_ae(y, y_hat)
    elif loss_name == "mse" or loss_name == "rmse":
      loss = calc_se(y, y_hat)
    final_loss += loss
    print(f"loss_name: {loss_name}, sample: {i}: pred: {y} target: {y_hat} loss: {loss}")
  final_loss /= n
  if loss_name == "rmse":
    final_loss = math.sqrt(final_loss)
  print("final loss is:", final_loss)

calc_loss_func()
