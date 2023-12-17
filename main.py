import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Заданные параметры
c = 9000
u = 10
g = 9.81
htb = 8480
T = 11

# Функция для r(x1)
def r(x1):
    return 0.1 * np.exp(-x1 / htb)

# Функция системы дифференциальных уравнений
def system(t, y):
    x1, x2, x3 = y
    dx1dt = x2
    dx2dt = c * u / x3 - g - r(x1) * x2**2 / x3
    dx3dt = -u
    return [dx1dt, dx2dt, dx3dt]

# Начальные условия
x1_0 = 0
x2_0 = 0
x3_0 = 600

# Решение системы
sol = solve_ivp(system, [0, T], [x1_0, x2_0, x3_0], method='RK45')

# Визуализация результатов
plt.figure(figsize=(12, 6))
plt.plot(sol.t, sol.y[0], label='x1(t)')
plt.plot(sol.t, sol.y[1], label='x2(t)')
plt.plot(sol.t, sol.y[2], label='x3(t)')
plt.xlabel('Time')
plt.ylabel('State Variables')
plt.legend()
plt.show()
