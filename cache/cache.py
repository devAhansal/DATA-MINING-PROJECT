
# %% [markdown]
# ## 2. Vérification des valeurs incohérentes

# %%
# Calcul de l'IQR pour chaque colonne numérique
Q1 = clients_dropped[['age', 'taux', 'nbEnfantsAcharge']].quantile(0.25)
Q3 = clients_dropped[['age', 'taux', 'nbEnfantsAcharge']].quantile(0.75)
IQR = Q3 - Q1

# Définition des bornes pour détecter les outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Sélectionner les lignes contenant des valeurs aberrantes
outliers = clients_dropped[((clients_dropped[['age', 'taux', 'nbEnfantsAcharge']] < lower_bound) | 
                   (clients_dropped[['age', 'taux', 'nbEnfantsAcharge']] > upper_bound)).any(axis=1)]

# Afficher les outliers
print(outliers)

# %%
# Vérification des valeurs non numériques dans des colonnes numériques
invalid_age = clients_dropped[~clients_dropped['age'].apply(pd.to_numeric, errors='coerce').notnull()]
invalid_taux = clients_dropped[~clients_dropped['taux'].apply(pd.to_numeric, errors='coerce').notnull()]
invalid_enfants = clients_dropped[~clients_dropped['nbEnfantsAcharge'].apply(pd.to_numeric, errors='coerce').notnull()]

# Affichage des résultats
print(invalid_age)
print(invalid_taux)
print(invalid_enfants)


# %%
# Vérification des doublons
print(clients_dropped.duplicated().sum())

# Supprimer les doublons si nécessaire
clients = clients_dropped.drop_duplicates()


# %%
import matplotlib.pyplot as plt
import seaborn as sns

# Afficher des histogrammes pour les colonnes numériques
clients[['age', 'taux', 'nbEnfantsAcharge']].hist(bins=15, figsize=(15, 10))
plt.show()

# Boxplot pour détecter les outliers
sns.boxplot(data=clients[['age', 'taux', 'nbEnfantsAcharge']])
plt.show()


# %%
# Matrice de corrélation
correlation_matrix = clients[['age', 'taux', 'nbEnfantsAcharge']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.show()


# %%
# Scatter plot pour examiner la relation entre 'age' et 'taux'
sns.scatterplot(x='age', y='taux', data=clients)
plt.show()

# Diagramme en barres pour la relation entre 'sexe' et 'taux'
sns.barplot(x='sexe', y='taux', data=clients)
plt.show()


# %%



