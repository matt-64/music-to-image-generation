# Roadmap - Music-to-Image Generation Project

## Phase 1: Préparation des données audio (1-2 semaines)

### 1.1 Extraction des features audio (Semaine 1)
- Extraire les features audio clés pour chaque fichier audio : 
  - Waveform
  - Mel Spectrogram
  - MFCC
  - Chroma Features
  - Zero Crossing Rate
  - Spectral Centroid, Bandwidth, Contrast, Tonnetz
  - RMS Energy
- Validation des sorties et des visualisations pour chaque feature.

### 1.2 Automatisation des features (Semaine 2)
- Créer un script Python qui prend en entrée un fichier audio et sort automatiquement toutes les analyses et visualisations des features.
- Optimisation de la vitesse d'exécution et du traitement en batch de plusieurs fichiers.

---

## Phase 2: Construction du modèle de génération d'images (3-5 semaines)

### 2.1 Recherche et préparation des données d'entraînement (Semaine 3)
- Rechercher et organiser les ensembles de données d'entraînement : Musique et images associées.
- Explorer des datasets ouverts (FMA, Google Music-Image datasets, etc.).

### 2.2 Pré-traitement des données (Semaine 4)
- Mettre en place des techniques de nettoyage et d'amélioration des données d'entraînement.
- Standardiser et normaliser les données pour préparer les entrées du modèle.

### 2.3 Construction du modèle de machine learning (Semaine 5)
- Choisir et implémenter un modèle de génération d'images basé sur les features audio :
  - GANs (Generative Adversarial Networks)
  - Diffusion models ou autres techniques adaptées.
- Créer un notebook pour le prototype du modèle.

---

## Phase 3: Entraînement et évaluation du modèle (4-6 semaines)

### 3.1 Entraînement du modèle (Semaine 6-7)
- Entraîner le modèle de génération d'images avec les données audio.
- Suivi des performances du modèle avec les métriques appropriées.

### 3.2 Optimisation et ajustements (Semaine 8)
- Optimiser les hyperparamètres pour améliorer les performances.
- Comparer les résultats et ajuster le modèle en fonction des observations.

### 3.3 Évaluation et tests (Semaine 9)
- Évaluer les performances du modèle sur un ensemble de test indépendant.
- Effectuer des ajustements en fonction des résultats des tests.

---

## Phase 4: Documentation et mise en production (2-3 semaines)

### 4.1 Documentation (Semaine 10)
- Documenter tout le processus de génération d'images à partir de musique.
- Créer un manuel d'utilisation pour l'outil de génération d'images.

### 4.2 Déploiement et publication (Semaine 11-12)
- Mettre le projet en ligne sur GitHub avec une documentation complète.
- Rendre le projet accessible à travers une API ou une interface utilisateur simple.

