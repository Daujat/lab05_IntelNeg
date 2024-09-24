import pandas as pd
from sklearn.impute import KNNImputer
data = pd.read_csv('housing-with-missing.csv', delimiter=';')

#Las variables con valores faltantes
variables_con_faltantes = data.columns[data.isnull().any()].tolist()
print("Variables con valores faltantes:")
print(variables_con_faltantes)

#Instncia del KNN
imputer = KNNImputer(n_neighbors=5)

#Separar las variables con valores faltantes
data_faltantes = data[variables_con_faltantes]

#Imputar los valores faltantes utilizando KNN
data_imputada = imputer.fit_transform(data_faltantes)

#Reemplazar los valores
data[variables_con_faltantes] = data_imputada
print("\nDataFrame con valores imputados:")
print(data.head())