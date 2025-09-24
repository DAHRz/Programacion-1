import pandas as pd

df = pd.read_csv("datos_pacientes.csv")
hipertensos = df[(df["pas"] &gt;= 140) | (df["pad"] &gt;= 90)]
