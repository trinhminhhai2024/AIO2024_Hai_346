import torch
import torch.nn as nn

class MySoftmax(nn.Module):
  def __init__(self):
    super().__init__()
  
  def forward(self,x):
    x_exp = torch.exp(x)
    partition = x_exp.sum(0, keepdims = True)
    return x_exp /partition

class StableSoftmax(nn.Module):
  def __init__(self):
    super().__init__()
  
  def forward(self,x):
    x_max = torch.max(x, dim = 0, keepdims = True)
    x_exp = torch.exp(x - x_max.values)
    partition = x_exp.sum(0, keepdims = True)
    return x_exp /partition
data = torch.Tensor([1, 2, 3])
my_softmax = MySoftmax()
stable_softmax = StableSoftmax()
output1 = my_softmax(data)
output2 = stable_softmax(data)
