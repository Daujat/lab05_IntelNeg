import pandas as pd
import numpy as np
data = {'x1': [1, 2, 8, 4, 1, 6],
        'x2': [100, 2, 3, 1, 2, 7],
        'x3': [34, np.nan, np.nan, np.nan, 27, 44],
        'x4': [102, 121, 343, np.nan, 121, 125]}

df = pd.DataFrame(data)
print("DataFrame original:")
print(df)

df_imputado = df.fillna(df.median())
print("\nDataFrame con datos faltantes imputados mediante la mediana:")
print(df_imputado)