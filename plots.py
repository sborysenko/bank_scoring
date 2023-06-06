import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("dataframe.csv")


def plot(x, y, x_title, y_title, title):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.xlabel(x_title, fontsize=15)
    plt.ylabel(y_title, fontsize=15)
    plt.title(title, fontsize=18)


exclude_columns = [
    'Н6 - Норматив короткострокової ліквідності',
    'Н11 - Норматив інвестування в цінні папери окремо за кожною установою',
    'Н12 - Норматив загальної суми інвестування',
    'Н13-1 - Норматив ризику загальної довгої відкритої валютної позиції',
    'Н13-2 - Норматив ризику загальної короткої відкритої валютної позиції'
]

data = data.drop(columns=exclude_columns)

columns = data.columns
for j in range(len(columns)):
    if j != 0:
        # if columns[j] not in exclude_columns:
        plot(data[columns[j]], data[columns[0]], columns[j], columns[0], "'" + columns[0] + "' від '" + columns[j] + "'")
plt.show()

corr = data.corr().round(2)
print(corr)
sns.heatmap(corr, annot=True, square=True)
plt.title("Матриця кореляціі", fontsize=15)
plt.show()
