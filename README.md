# Projet Big Data

Ce projet implémente un pipeline d'ingestion et de traitement de données (Big Data).

## Structure du Projet

- `scripts/` : Contient les scripts Python pour l'ingestion et la visualisation.
  - `producer.py` : Producteur de données.
  - `ingestion_bronze.py` : Ingestion des données brutes (Bronze).
  - `ingestion_silver.py` : Nettoyage et transformation (Silver).
  - `ingestion_gold.py` : Agrégation et données prêtes pour l'analyse (Gold).
  - `visualisation.py` : Script pour visualiser les résultats.
- `notebooks/` : Notebooks pour l'analyse exploratoire.
- `data/` : Dossier pour le stockage des données.

## Utilisation

1. Activez l'environnement virtuel :
   ```powershell
   .\venv\Scripts\Activate
   ```
2. Lancez les scripts dans l'ordre du pipeline (Bronze -> Silver -> Gold).
