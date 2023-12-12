import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Параметры модели
p = 100000
a = 0.6
m = 2000
u = 10
cx = 0.05
cy = 0.01
m1 = 0.1
m2 = 0.01
g = 9.81
T = 10

# Функции системы дифференциальных уравнений
def model(t, y):
    x1, x2, x3, x4, x5 = y
    dx1dt = -g*np.sin(x2) + (p - a*cx*x1**2) / (m - u*t)
    dx2dt = (-g + (p*np.sin(x5 - x2) + a*cy*x1**2) / (m - u*t)) / x1
    dx3dt = (m1*a*(x2 - x5)*x1**2 - m2*a*x1**2*x3) / (m - u*t)
    dx4dt = x1*np.sin(x2)
    dx5dt = x3
    return [dx1dt, dx2dt, dx3dt, dx4dt, dx5dt]

# Начальные условия
y0 = [1800, 0.8, 0, 0, 0.8]

# Решение системы с заданным шагом h
def solve_system(h):
    t_span = (0, T)
    t_eval = np.arange(0, T, h)
    sol = solve_ivp(model, t_span, y0, t_eval=t_eval, method='RK45')
    return sol.t, sol.y

# Оценка погрешности
def estimate_error(y, y_half):
    y_end = y[-1, 3]  # x4(T) при шаге h
    y_half_end = y_half[-1, 3]  # x4(T) при шаге h/2
    abs_error = np.abs(y_half_end - y_end)
    rel_error = abs_error / np.abs(y_half_end) * 100
    return abs_error, rel_error

# Автоматический выбор шага интегрирования
h = 0.1  # Начальный шаг
rel_error = 100  # Начальная относительная погрешность
while rel_error > 1:  # Порог погрешности 1%
    t, y = solve_system(h)
    t_half, y_half = solve_system(h / 2)
    _, rel_error = estimate_error(y, y_half)
    h /= 2

# Визуализация результатов
plot_results(t_half, y_half)

print(f"Итоговый шаг интегрирования: {h}")
print(f"Относительная погрешность: {rel_error}%")
