import numpy as np
import scipy.integrate as integrate
import scipy.optimize as optimize
import matplotlib.pyplot as plt

# Функция плотности распределения вероятностей
def pdf(z):
    return 1 / (1 + np.sin(z))

# Функция распределения вероятностей
def cdf(z):
    return integrate.quad(pdf, 0, z)[0]

# Обратная функция распределения вероятностей
def inverse_cdf(y):
    return optimize.root_scalar(lambda z: cdf(z) - y, bracket=[0, np.pi/2]).root

# Генерация случайных чисел
def generate_random_numbers(n):
    uniform_randoms = np.random.uniform(0, 1, n)
    return np.array([inverse_cdf(y) for y in uniform_randoms])

# Оценка математического ожидания и дисперсии
def estimate_mean_variance(samples):
    mean = np.mean(samples)
    variance = np.var(samples)
    return mean, variance

# Генерация выборок и оценка
sample_sizes = [50, 100, 1000, 100000]
for size in sample_sizes:
    samples = generate_random_numbers(size)
    mean, variance = estimate_mean_variance(samples)
    print(f"Sample size: {size}, Mean: {mean}, Variance: {variance}")

# Дополнительные шаги для критерия Пирсона и визуализации будут реализованы далее
