import numpy as np
import pandas as pd
from scipy.interpolate import interp1d
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


data = pd.read_csv("dataframe.csv")
data = data.sort_values(by=['Частка непрофільних активів банку'])
# data = data.sort_values(by=['Н2 - Норматив достатності регулятивного капіталу'])
# data = data.sort_values(by=['Доступ до ресурсів і надійність бенефіціара'])

# Задані дані
x = data['Частка непрофільних активів банку'].values.tolist()  # Задані значення x
y = data['Індекс'].values.tolist()  # Задані значення y

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

# Створення інтерполяційної функції
interp_func = interp1d(x_train, y_train, kind='linear')

# Виконання інтерполяції та екстраполяції
y_interp = interp_func(x_test)

# Виведення результатів
print("Значення y для інтерпольованих точок:", interp_func(x))
print("Значення y для екстрапольованих точок:", y_interp)

plt.figure(figsize=(10, 6))
plt.plot(list(range(1, len(y_interp) + 1)), y_interp, label="Predicted")
plt.plot(list(range(1, len(y_test) + 1)), y_test, label="Test values")
plt.legend()
plt.show()
