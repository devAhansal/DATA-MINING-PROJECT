
data-mining-project/
│
├── data/                    # Dossier pour les données brutes et transformées
│   ├── raw/                 # Données brutes non modifiées
│   │   ├── catalogue.csv
│   │   ├── immatriculations.csv
│   │   ├── clients.csv
│   │   └── marketing.csv
│   ├── processed/           # Données transformées et prêtes pour analyse
│       ├── catalogue_processed.csv
│       ├── clients_processed.csv
│       └── immatriculations_processed.csv
├── notebooks/               # Dossiers pour les notebooks Jupyter (EDA, visualisation, tests)
│   ├── 01-eda-catalogue.ipynb
│   ├── 01-eda-clients.ipynb       
│   ├── 01-eda-Immatriculations.ipynb 
│   ├── 03-clustering.ipynb  # Identification des catégories de véhicules
│   ├── 04-classification.ipynb
│   └── 05-marketing-prediction.ipynb
│
├── src/                     # Code source pour les scripts principaux
│   └── main.py   # Script de nettoyage et transformation des données
│
├── models/                  # Sauvegarde des modèles entraînés
│   ├── clustering_model.pkl
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   └── svm_model.pkl
│
├── reports/                 # Rapport
│   └── reports_project.pdf
│
├── requirements.txt         # Liste des dépendances Python
├── README.md                # Documentation du projet
└── config.yaml              # Fichier de configuration (chemins de fichiers, paramètres globaux)