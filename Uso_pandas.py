import pandas as pd

df = pd.read_csv("datos_pacientes.csv")
hipertensos = df[(df["pas"] >= 140) | (df["pad"] >= 90)]
