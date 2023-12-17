import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Функция плотности распределения вероятностей
def pdf(z):
    return 1 / (1 + np.sin(z))

# Генерация случайных чисел
def generate_random_numbers(n):
    return np.random.uniform(0, np.pi/2, n)

# Расчет критерия хи-квадрат
def chi_square_test(samples, pdf, bins):
    frequency, edges = np.histogram(samples, bins=bins, density=True)
    mid = (edges[:-1] + edges[1:]) / 2
    expected_freq = pdf(mid) * np.diff(edges)
    observed_freq = frequency * np.diff(edges)
    chi_square_stat = np.sum((observed_freq - expected_freq) ** 2 / expected_freq)
    return chi_square_stat

# Генерация выборки
sample_size = 1000
samples = generate_random_numbers(sample_size)

# Построение гистограммы выборочного закона распределения
plt.hist(samples, bins=20, density=True, alpha=0.5, label='Выборочное распределение')

# Построение гистограммы теоретического закона распределения
z = np.linspace(0, np.pi/2, 1000)
plt.plot(z, pdf(z), label='Теоретическое распределение', color='red')

# Расчет критерия хи-квадрат
chi_square_value = chi_square_test(samples, pdf, bins=20)
print(f"Значение критерия χ²: {chi_square_value}")

plt.legend()
plt.show()
