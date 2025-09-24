from sklearn.ensemble import RandomForestClassifier
X = df[["edad", "peso", "colesterol"]]
y = df["hipertension"]
modelo = RandomForestClassifier()
modelo.fit(X, y)