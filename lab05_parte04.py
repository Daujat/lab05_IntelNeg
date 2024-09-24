import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
data = pd.read_csv('housing-with-missing.csv', delimiter=';')

#Identificar las variables
variables_con_faltantes = data.columns[data.isnull().any()].tolist()
print("Variables con valores faltantes:")
print(variables_con_faltantes)

#Instancia dMultivariate Imputer
imputer = IterativeImputer(max_iter=10, random_state=0)

#Separar las variables
data_faltantes = data[variables_con_faltantes]

#Imputar valores faltantes utilizando Multivariate Imputer
data_imputada = imputer.fit_transform(data_faltantes)

#Reemplazar valores faltantes en el DataFrame original
data[variables_con_faltantes] = data_imputada
print("\nDataFrame con valores imputados:")
print(data.head())