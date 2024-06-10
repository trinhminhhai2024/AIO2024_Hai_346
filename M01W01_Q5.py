def md_rne(n, p):
  final_loss = 0
  for i in range(1,n):
    y = random.random()
    y_hat = random.random()
    y_root = y**(1/i)
    y_hat_root = y_hat**(1/i)
    difference = y_root = y_hat_root
    loss = difference**p
    final_loss += loss
    #print(f"sample: {i}: pred: {y} target: {y_hat} loss: {loss}")
  final_loss /= n
  return final_loss
md_rne (100000,4)
