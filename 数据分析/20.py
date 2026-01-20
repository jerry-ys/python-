import torch
import numpy as np

np_data = np.arange(6).reshape((2,3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
data = [-1,-2,1,2]
tensor = torch.FloatTensor(data)
_ = [[1,2],[3,4]]
tensor1 = torch.FloatTensor(_)
_ = np.array(_)

print(np_data)
print(torch_data)
print(tensor2array)
print(np.abs(data))
print(torch.abs(tensor))
print(np.mean(data))
print(torch.mean(tensor))
print(np.matmul(_,_))
print(torch.mm(tensor1,tensor1))
print(_.dot(_))