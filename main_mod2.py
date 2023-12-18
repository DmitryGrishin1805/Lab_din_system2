import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Параметры системы
k = 1
l = 10
m = 2
n = 8
kt = 100
b = 22000
i1 = 10
i2 = 1
s = 100
V = 800
T = 11
delta_max = 0.5

# Функция системы дифференциальных уравнений
def system(t, y):
    x1, x2, x3, x4, x5 = y
    theta = (10000 - x5) / (b - V * t)
    delta = -kt * t * x4 - i1 * x2 - i2 * x3 + s * (theta - x2)
    x4_val = delta if abs(delta) <= delta_max else delta_max * np.sign(delta)
    return [
        k * x2 - k * x1,  # dx1/dt
        x3,              # dx2/dt
        l * x1 - l * x2 - m * x3 + n * x4_val,  # dx3/dt
        V * np.sin(x1),  # dx5/dt
        x4_val           # x4 (зависит от delta)
    ]

# Начальные условия
y0 = [1, 1, 0, 0, 0]

# Решение системы
sol = solve_ivp(system, [0, T], y0, method='RK45', max_step=0.1)

# Визуализация результатов
plt.figure(figsize=(12, 6))
for i in range(sol.y.shape[0]):
    plt.plot(sol.t, sol.y[i], label=f'x{i+1}(t)')
plt.xlabel('Time')
plt.ylabel('State Variables')
plt.legend()
plt.show()
