import pandas as pd
import matplotlib.pyplot as plt
import os

# Chemin vers les données Gold
path = "data/gold"
df = pd.read_parquet(path)

# 1. On s'assure qu'on ne prend que les monnaies principales pour plus de clarté
# Ou on limite aux 10 premières lignes
df_plot = df.head(10) 

# 2. Création du graphique avec une meilleure gestion des labels
plt.figure(figsize=(10, 6)) # Agrandit la fenêtre
df_plot.plot(kind='bar', x='merchant', y='prix_moyen_mad', color='skyblue', ax=plt.gca())

plt.title('Prix Moyen des Cryptos en MAD (Couche Gold)')
plt.ylabel('Prix (MAD)')
plt.xlabel('Crypto-monnaie')

# 3. Ajustement automatique pour éviter que les noms se touchent
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Sauvegarde
plt.savefig('data/market_report.png')
print("📊 Graphique corrigé généré dans data/market_report.png !")
plt.show()