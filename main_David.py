import math

# Значения прогнозов z
z_values = [-2, -4, -4, 0.5, 1.0, -1, -0.5, 7]

# Вычисление вероятностей с помощью формулы логистической регрессии
probabilities = [1 / (1 + math.exp(-z)) for z in z_values]

# Вывод результатов
for z, p in zip(z_values, probabilities):
    print(f"Прогноз {z}: вероятность {p:.4f}")
