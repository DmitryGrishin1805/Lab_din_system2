import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Заданные параметры
k = 1
l = 12
m = 1
n = 8
kt = 100
b = 30000
i1 = 10
i2 = 1
s = 100
V = 800
T = 11
alpha_max = 0.5

# Начальные условия
x1_0 = 1
x2_0 = 1
x3_0 = 0
x4_0 = 0
x5_0 = 0

# Функция системы дифференциальных уравнений
def system(t, y):
    x1, x2, x3, x4, x5 = y
    alpha = x2 - x1
    alpha_star = alpha if abs(alpha) <= alpha_max else alpha_max * np.sign(alpha)
    theta = (10000 - x5) / (b - V * t)

    dx1dt = k * alpha_star
    dx2dt = x3
    dx3dt = l * x1 - l * x2 - m * x3 + n * x4
    dx4dt = -kt * x4 - i1 * x2 - i2 * x3 + s * (theta - x1)
    dx5dt = V * np.sin(x1)

    return [dx1dt, dx2dt, dx3dt, dx4dt, dx5dt]

# Решение системы
sol = solve_ivp(system, [0, T], [x1_0, x2_0, x3_0, x4_0, x5_0], method='RK45')

# Визуализация результатов
plt.figure(figsize=(12, 6))
for i in range(sol.y.shape[0]):
    plt.plot(sol.t, sol.y[i], label=f'x{i+1}(t)')
plt.xlabel('Time')
plt.ylabel('State Variables')
plt.legend()
plt.show()
