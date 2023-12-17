from matplotlib import pyplot
# Загрузка библиотек

from pandas import read_csv



# Загрузка библиотек
from pandas import read_csv

# Загрузка датасета
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# shape
print(dataset.shape)

# Срез данных head
print(dataset.head(20))

# Стастические сводка методом describe
print(dataset.describe())

# Распределение по атрибуту class
print(dataset.groupby('class').size())
# Диаграмма размаха
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

