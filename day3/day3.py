import numpy as np

data = []
with open("input.dat", "r") as infile:
    for line in infile:
        data.append([])
        for num in line.strip():
            data[-1].append(int(num))
data = np.array(data)
rows = data.shape[0]
data = np.sum(data, axis=0)
gamma = np.where(data > rows//2, 1, 0)
epsilon = np.where(gamma == 0, 1, 0)

gamma = np.array(gamma, dtype=str)
gamma = "".join(gamma)
gamma = int(str(gamma), 2)

epsilon = np.array(epsilon, dtype=str)
epsilon = "".join(epsilon)
epsilon = int(str(epsilon), 2)

print(gamma, epsilon, gamma*epsilon)

