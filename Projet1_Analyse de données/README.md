# 📊 Analyse des projets Kickstarter

##  Objectif du projet

L’objectif de ce projet est de **comprendre les facteurs qui influencent la réussite ou l’échec d’un projet Kickstarter**. À partir d’un fichier CSV contenant les données de milliers de campagnes, nous avons :

- Analysé les caractéristiques des projets (catégorie, montant demandé, pays, etc.)
- Visualisé la répartition des succès/échecs
- Exploré les montants moyens par catégorie
- Créé un **dashboard interactif** avec **Streamlit** pour que tout utilisateur puisse manipuler les filtres et découvrir les insights lui-même.

---

## 📁 Fichier utilisé

Nous avons utilisé le dataset suivant :

- **Nom du fichier** : `Kickstarter.csv`
- **Source** : [Kaggle - Kickstarter Projects](https://www.kaggle.com/kemical/kickstarter-projects)
- **Type** : Données tabulaires (.csv)
- **Taille** : ~320 000 projets

---

## Librairies et technologies utilisées

| Librairie | Rôle dans le projet |
|-----------|---------------------|
| `pandas` | Chargement, nettoyage et manipulation du dataset |
| `numpy` | Calculs statistiques (moyennes, pourcentages, etc.) |
| `matplotlib.pyplot` | Création de graphiques (bar plots, courbes) |
| `seaborn` (optionnel) | Amélioration esthétique de certains graphiques |
| `streamlit` | Création de l’interface web interactive pour présenter les analyses |
| `datetime` | Manipulation des dates de lancement des projets |

---

## 📊 Étapes de l’analyse

### 1. Exploration initiale (`analysis.ipynb`)
Dans le notebook Jupyter, nous avons :

- Chargé le dataset avec `pandas.read_csv()`
- Supprimé les projets annulés ou suspendus
- Observé les valeurs manquantes
- Étudié les proportions de projets réussis vs échoués
- Calculé le montant moyen demandé par catégorie

### 2. Préparation pour Streamlit
Une fois l’analyse faite, nous avons :

- Identifié les variables clés à filtrer : `main_category`, `year`
- Créé des visualisations avec `matplotlib`
- Converti les étapes en fonctions prêtes à être intégrées dans `Streamlit`

---

## Fonctionnalités du Dashboard (`app.py`)

Le dashboard permet :

-  De filtrer par **catégorie principale**
-  De filtrer par **année de lancement**
-  D’afficher le **nombre total de projets**
-  De visualiser le **taux de réussite global**
-  D’afficher un **graphique des succès/échecs**
![Aperçu du Dashboard](succes vs echec.png)

-  De voir le **montant moyen demandé par catégorie**
![Aperçu du Dashboard](montant moyen.png)


Le tout **en temps réel**, en fonction des filtres choisis par l’utilisateur dans la sidebar.



---

##  Comment exécuter le projet

1. Installer les dépendances (dans un environnement virtuel de préférence) :
```bash
pip install pandas matplotlib streamlit

##  Lancer l'applicatio 
```bash
streamlit run app.py

Une page web s’ouvre automatiquement à l’adresse :
http://localhost:8501

---

## 👥 Auteurs : Ikram KOUIBAATI

Ce projet a été réalisé dans le cadre d'un travail d'analyse de données avec Streamlit. 

---