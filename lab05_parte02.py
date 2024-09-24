import pandas as pd
import numpy as np
data = {'x1': [1, 2, 3, 4, 5, 6],
        'x2': [1, 2, np.nan, 1, np.nan, 7],
        'x3': [32, 30, np.nan, np.nan, 27, 44],
        'x4': [102, np.nan, 343, np.nan, 121, np.nan]}

df = pd.DataFrame(data)
print("DataFrame original:")
print(df)

df_imputado = df.fillna(df.median())
print("\nDataFrame con datos faltantes imputados mediante la mediana:")
print(df_imputado)