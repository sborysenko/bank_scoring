import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import matplotlib.pyplot as plt


def run(df):
    scaler = StandardScaler()

    x = df[['Н1 - Регулятивний капітал',
            'Н2 - Норматив достатності регулятивного капіталу',
            'Н3 - Норматив достатності основного капіталу',
            'LCR - Коефіцієнт покриття ліквідністю',
            # 'Н6 - Норматив короткострокової ліквідності',
            'Н7 - Норматив максимального розміру кредитного ризику на одного контрагента',
            'Н8 - Норматив великих кредитних ризиків',
            'Н9 - Норматив максимального розміру кредитного ризику за операціями з пов’язаними особами',
            # 'Н11 - Норматив інвестування в цінні папери окремо за кожною установою',
            # 'Н12 - Норматив загальної суми інвестування',
            # 'Н13-1 - Норматив ризику загальної довгої відкритої валютної позиції',
            # 'Н13-2 - Норматив ризику загальної короткої відкритої валютної позиції',
            'Коефіцієнт автономії',
            'Адекватність капіталу',
            'Частка резервів під знецінення кредитів',
            'NIM - Чиста процентна маржа',
            'CIR - Ефективність витрат',
            'OROA - Операційна рентабельність',
            'ROA - Рентабельність активів',
            'ROE - Рентабельність власного капіталу',
            "Відношення грошових коштів до зобов'язань",
            'Відношення грошових коштів до активів',
            'Частка ліквідних активів у загальних активах',
            'Частка непрофільних активів банку',
            'Доступ до ресурсів і надійність бенефіціара']]
    y = df['Індекс']

    scaled = scaler.fit_transform(x)
    x = pd.DataFrame(scaled, columns=[
            'Н1 - Регулятивний капітал',
            'Н2 - Норматив достатності регулятивного капіталу',
            'Н3 - Норматив достатності основного капіталу',
            'LCR - Коефіцієнт покриття ліквідністю',
            # 'Н6 - Норматив короткострокової ліквідності',
            'Н7 - Норматив максимального розміру кредитного ризику на одного контрагента',
            'Н8 - Норматив великих кредитних ризиків',
            'Н9 - Норматив максимального розміру кредитного ризику за операціями з пов’язаними особами',
            # 'Н11 - Норматив інвестування в цінні папери окремо за кожною установою',
            # 'Н12 - Норматив загальної суми інвестування',
            # 'Н13-1 - Норматив ризику загальної довгої відкритої валютної позиції',
            # 'Н13-2 - Норматив ризику загальної короткої відкритої валютної позиції',
            'Коефіцієнт автономії',
            'Адекватність капіталу',
            'Частка резервів під знецінення кредитів',
            'NIM - Чиста процентна маржа',
            'CIR - Ефективність витрат',
            'OROA - Операційна рентабельність',
            'ROA - Рентабельність активів',
            'ROE - Рентабельність власного капіталу',
            "Відношення грошових коштів до зобов'язань",
            'Відношення грошових коштів до активів',
            'Частка ліквідних активів у загальних активах',
            'Частка непрофільних активів банку',
            'Доступ до ресурсів і надійність бенефіціара'])
    print(x)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    model = LinearRegression()
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)

    # выведем корень среднеквадратической ошибки
    # сравним тестовые и прогнозные значения цен на жилье
    print('Root Mean Squared Error (RMSE):', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
    print('R2:', np.round(metrics.r2_score(y_test, y_pred), 2))

    plt.figure(figsize=(10, 6))
    plt.plot(list(range(1, len(y_pred) + 1)), y_pred, label="Predicted")
    plt.plot(list(range(1, len(y_test) + 1)), y_test, label="Test values")
    plt.legend()
    plt.show()


data = pd.read_csv("dataframe.csv")

run(data)
