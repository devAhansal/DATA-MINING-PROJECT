
data-mining-project/
│
├── data/                    # Dossier pour les données brutes et transformées
│   ├── raw/                 # Données brutes non modifiées
│   │   ├── catalogue.csv
│   │   ├── immatriculations.csv
│   │   ├── clients.csv
│   │   └── marketing.csv
│   ├── processed/           # Données transformées et prêtes pour analyse
│   │   └── merged_data.csv
│   └── reports/             # Rapports sur les données (statistiques descriptives)
│       └── data_summary.txt
│
├── notebooks/               # Dossiers pour les notebooks Jupyter (EDA, visualisation, tests)
│   ├── 01-data-cleaning.ipynb
│   ├── 02-eda.ipynb         # Analyse exploratoire des données
│   ├── 03-clustering.ipynb  # Identification des catégories de véhicules
│   ├── 04-classification.ipynb
│   └── 05-marketing-prediction.ipynb
│
├── src/                     # Code source pour les scripts principaux
│   ├── data_processing.py   # Script de nettoyage et transformation des données
│   ├── clustering.py        # Script pour les modèles de clustering
│   ├── classification.py    # Script pour les modèles de classification
│   ├── evaluation.py        # Script pour évaluer les modèles
│   └── predict_marketing.py # Script pour prédire les catégories pour les clients marketing
│
├── models/                  # Sauvegarde des modèles entraînés
│   ├── clustering_model.pkl
│   ├── classification_model.pkl
│   └── pipeline.pkl         # Sauvegarde des pipelines si nécessaires
│
├── reports/                 # Rapports et visualisations finales
│   ├── clustering_report.pdf
│   ├── classification_report.pdf
│   └── marketing_prediction.pdf
│
├── requirements.txt         # Liste des dépendances Python
├── README.md                # Documentation du projet
└── config.yaml              # Fichier de configuration (chemins de fichiers, paramètres globaux)