# 🧠 Notes personnelles Python

## Projet

- Nom : `python-debutant`
- Objectif : Reprendre Python depuis zéro avec une structure claire et progressive.

---

## Organisation

### 📁 Leçons
- Format : `.md` avec blocs de code `python`
- Exemple :
  - `lecons/lecon_1_variables_types.md`
  - `lecons/lecon_2_operateurs.md`

### 📂 Exercices
- Chaque leçon a son dossier :
  - `exercices/01_variables_types/`
  - `exercices/02_operateurs/`
- Fichier principal : `exercice_corrige.py`

### Convention de code

```python
# 🔹 TYPE : int
# 🔸 BUT  : addition de deux variables

### 🧮 Leçon 2 – Résumé clair

#### ➕ Opérateurs arithmétiques
- Addition : a + b  
- Soustraction : a - b  
- Multiplication : a * b  
- Division : a / b  
- Division entière : a // b  
- Reste de la division (modulo) : a % b  
- Puissance : a ** b → Ex : 10 ** 3 = 1000

#### 🔍 Opérateurs de comparaison
- Égalité : a == b  
- Différence : a != b  
- Supérieur / inférieur : a > b, a < b  
- Supérieur ou égal / inférieur ou égal : a >= b, a <= b  
→ Résultat : True ou False

#### 🔗 Opérateurs logiques
- and → les deux conditions doivent être vraies  
- or → une seule suffit  
- not → inverse le résultat

Exemple :  
a > 10 and b < 5  → renvoie True si les deux conditions sont vraies

#### 🧠 À retenir
- Test de divisibilité : a % b == 0  
- Tous les tests peuvent être affichés avec print(...)
- Convention de commentaires :
```python
# 🔹 TYPE : ce que fait la ligne (ex : input)
# 🔸 BUT  : pourquoi on le fait (ex : demander un entier)
```
