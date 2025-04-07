## 🧠 GitHub & Git - Notes personnelles de Julien

Bienvenue dans ta forge personnelle, Julien. Ce fichier est ton **grimoire GitHub**, à enrichir au fil de tes découvertes et expérimentations.

---

## 🛍️ 1. Git vs GitHub : comprendre la différence

- **Git** : système local de gestion de versions.
    - Tu prends des "photos" de ton code avec `commit`
    - Tu peux créer des branches pour tester sans danger

- **GitHub** : plateforme en ligne qui héberge tes projets Git.
    - Tu peux partager, collaborer, automatiser
    - Tu pousses ton code avec `push`

---

## 🌱 2. Branches (et pourquoi `dev` existe)

- `main` : branche officielle, propre, publique
- `dev` : branche de test, brouillon, évolution

### ➕ Créer une branche :
```bash
git checkout -b dev
```

### ↺ Fusionner une branche :
```bash
git checkout main
git merge dev
git push origin main
```

---

## 📤 3. Commandes Git essentielles

```bash
git status       # Voir les fichiers modifiés
git add .        # Ajouter tous les fichiers modifiés au prochain commit
git commit -m "message"  # Créer un point de sauvegarde
git push origin nom-de-branche  # Envoyer sur GitHub
```

---

## 🤖 4. GitHub Actions

### 🔧 Objectif : automatiser des actions à chaque push

GitHub Actions te permet d'exécuter automatiquement des étapes (comme tester ton code) à chaque push ou pull request.

- Le fichier `tests.yml` est un **workflow** : un plan d'action pour GitHub.
- Il est placé dans `.github/workflows/tests.yml`
- Il décrit l'environnement, les dépendances et la commande à exécuter.

### Exemple de contenu :
```yaml
name: Tests Python
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt || true
      - name: Run tests
        run: |
          python -m unittest discover -s tests
```

#### 💡 Explication simple des étapes :
- `checkout` : GitHub récupère ton code
- `setup-python` : il installe Python (ici version 3.11)
- `Install dependencies` : installe les bibliothèques
- `Run tests` : exécute les tests via `unittest`

---

## 🏅 5. Badges dans le README

### ✅ Badge standard GitHub Actions :
```markdown
![Tests](https://github.com/beaslay/python-debutant/actions/workflows/tests.yml/badge.svg)
```

Affiché automatiquement selon le statut des actions :
- 🟢 `passing` : tous les tests OK
- 🔴 `failing` : un ou plusieurs tests échouent

---

## 🧪 6. Test unitaire Python : explication simple

Un **test unitaire**, c'est une vérification automatique qu'un bout de ton code fonctionne correctement.

Tu crées un fichier spécial dans un dossier `tests/`, avec une classe de test.

### Exemple de test minimal
Fichier : `tests/test_base.py`
```python
import unittest

class TestBase(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(1 + 1, 2)
```

#### Décryptage :
- `unittest` est la bibliothèque de test intégrée à Python
- `TestBase` est une classe qui contient des tests
- `self.assertEqual(...)` vérifie que le résultat attendu correspond bien au résultat obtenu
- Ici, on teste que 1 + 1 = 2, juste pour valider que le test fonctionne bien

---

## 🤁 7. À venir / À ajouter

- ✅ Comment cloner un dépôt distant
- ✅ Comment créer une `pull request`
- ✅ Ajouter d'autres types de badges (licence, version Python, etc.)
- ✅ Utiliser `.gitignore`
- ✅ Gérer les conflits lors d’un merge

> Tu peux enrichir ce fichier à tout moment : c’est ton espace de progression continue.

