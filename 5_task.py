import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Исходные данные
data = np.array([[0, 0], [0, 0], [1, 0], [0, 1], [2, 1]])

# Стандартизация данных
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Применение PCA
pca = PCA(n_components=2)
pca.fit(data_scaled)

# Первая главная компонента
first_component = pca.components_[0]

# Доля дисперсии, приходящаяся на первую главную компоненту
variance_ratio = pca.explained_variance_ratio_[0]

print("Первая главная компонента:", first_component)
print("Доля дисперсии, приходящаяся на первую главную компоненту:", variance_ratio)
