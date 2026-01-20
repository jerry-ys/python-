import torch
import matplotlib.pyplot as plt

torch.manual_seed(1)

# fake data
x = torch.unsqueeze(torch.linspace(-1,1,100),dim = 1)
y = x.pow(2) + 0.2 * torch.rand(x.size())

def save():
    net1 = torch.nn.Sequential(
        torch.nn.Linear(1,10),
        torch.nn.ReLU(),
        torch.nn.Linear(10,1)
    )
    optimizer = torch.optim.SGD(net1.parameters(),lr=0.3)
    loss_func = torch.nn.MSELoss()

    for t in range(100):
        prediction = net1(x)
        loss = loss_func(prediction,y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    torch.save(net1,'net.pkl')
    torch.save(net1.state_dict(),'net_params.pkl')

    # plot result
    plt.figure(1,figsize=(10,3))
    plt.subplot(131)
    plt.title('Net1')
    plt.scatter(x.numpy(),y.numpy())
    plt.plot(x.numpy(),prediction.detach().numpy(),'r-',lw=5)

def restore_net():
    net2 = torch.load('net.pkl',weights_only=False)
    prediction = net2(x)
    # plot result
    plt.subplot(132)
    plt.title('Net2')
    plt.scatter(x.numpy(),y.numpy())
    plt.plot(x.numpy(),prediction.detach().numpy(),'r-',lw=5)

def restore_params():
    net3 = torch.nn.Sequential(
        torch.nn.Linear(1,10),
        torch.nn.ReLU(),
        torch.nn.Linear(10,1)
    )
    net3.load_state_dict(torch.load('net_params.pkl',weights_only=False))
    prediction = net3(x)

    # plot result
    plt.subplot(133)
    plt.title('Net3')
    plt.scatter(x.numpy(),y.numpy())
    plt.plot(x.numpy(),prediction.detach().numpy(),'r-',lw=5)

save()

restore_net()

restore_params()

plt.show()