import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df["pas"], kde=True)
plt.title("Distribución de la presión sistólica")
plt.show()
