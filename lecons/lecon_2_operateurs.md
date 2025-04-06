# 🧠 Leçon 2 : Les opérateurs en Python

## 🎯 Objectif de la leçon
Comprendre et utiliser les opérateurs arithmétiques, de comparaison et logiques en Python.

---

## 1. 📐 Les opérateurs arithmétiques

| Opérateur | Signification       | Exemple (a=5, b=2) | Résultat |
|----------|---------------------|---------------------|----------|
| `+`      | Addition             | `a + b`             | 7        |
| `-`      | Soustraction         | `a - b`             | 3        |
| `*`      | Multiplication       | `a * b`             | 10       |
| `/`      | Division             | `a / b`             | 2.5      |
| `//`     | Division entière     | `a // b`            | 2        |
| `%`      | Modulo (reste)       | `a % b`             | 1        |
| `**`     | Puissance            | `a ** b`            | 25       |

### 🔍 Exemple avec commentaires :
```python
# 🔹 int : entier, 🔹 float : nombre à virgule
# 🔸 BUT : démontrer les opérations de base

x = 10          # 🔹 int    # 🔸 BUT : valeur initiale
y = 3           # 🔹 int    # 🔸 BUT : valeur initiale

print(x + y)    # 🔸 BUT : addition => 13
print(x - y)    # 🔸 BUT : soustraction => 7
print(x * y)    # 🔸 BUT : multiplication => 30
print(x / y)    # 🔸 BUT : division flottante => 3.333...
print(x // y)   # 🔸 BUT : division entière => 3
print(x % y)    # 🔸 BUT : modulo => 1
print(x ** y)   # 🔸 BUT : puissance => 1000
```

---

## 2. 🧮 Les opérateurs de comparaison

| Opérateur | Signification        | Exemple (a=5, b=2) | Résultat |
|----------|----------------------|---------------------|----------|
| `==`     | Égal à               | `a == b`            | False    |
| `!=`     | Différent de         | `a != b`            | True     |
| `>`      | Supérieur à          | `a > b`             | True     |
| `<`      | Inférieur à          | `a < b`             | False    |
| `>=`     | Supérieur ou égal à  | `a >= b`            | True     |
| `<=`     | Inférieur ou égal à  | `a <= b`            | False    |

### 🔍 Exemple :
```python
# 🔹 int : entier
# 🔸 BUT : vérifier les comparaisons entre deux valeurs

a = 5           # 🔹 int    # 🔸 BUT : valeur de référence
b = 2           # 🔹 int    # 🔸 BUT : valeur comparée

print(a == b)   # 🔸 BUT : égalité => False
print(a != b)   # 🔸 BUT : différence => True
print(a > b)    # 🔸 BUT : supérieur => True
print(a < b)    # 🔸 BUT : inférieur => False
print(a >= b)   # 🔸 BUT : supérieur ou égal => True
print(a <= b)   # 🔸 BUT : inférieur ou égal => False
```

---

## 3. ⚙️ Les opérateurs logiques

| Opérateur | Signification               | Exemple                | Résultat |
|----------|-----------------------------|------------------------|----------|
| `and`    | ET logique (les deux vrais) | `True and False`       | False    |
| `or`     | OU logique (un seul vrai)   | `True or False`        | True     |
| `not`    | NON logique (inversion)     | `not True`             | False    |

### 🔍 Exemple :
```python
# 🔹 bool : booléen (True ou False)
# 🔸 BUT : démontrer les conditions logiques

x = True       # 🔹 bool    # 🔸 BUT : état logique 1
y = False      # 🔹 bool    # 🔸 BUT : état logique 2

print(x and y) # 🔸 BUT : ET logique => False
print(x or y)  # 🔸 BUT : OU logique => True
print(not x)   # 🔸 BUT : NON logique => False
```

---

## 🧪 Exercice pratique corrigé

### ✍️ Enoncé
Crée un script qui prend deux nombres et affiche :
1. Leur somme, produit, et reste de la division
2. S'ils sont égaux ou non
3. Si au moins l’un des deux est supérieur à 10

### ✅ Solution :
```python
# 🔹 int : entier
# 🔸 BUT : tester plusieurs opérateurs sur deux nombres

a = 12            # 🔹 int    # 🔸 BUT : premier nombre
b = 7             # 🔹 int    # 🔸 BUT : deuxième nombre

# 🔸 PARTIE 1 : opérations arithmétiques
print("Somme :", a + b)          # 🔸 BUT : afficher la somme => 19
print("Produit :", a * b)        # 🔸 BUT : afficher le produit => 84
print("Reste :", a % b)          # 🔸 BUT : afficher le modulo => 5

# 🔸 PARTIE 2 : comparaison
print("Égalité ?", a == b)       # 🔸 BUT : vérifier égalité => False

# 🔸 PARTIE 3 : logique
print("Un > 10 ?", a > 10 or b > 10)  # 🔸 BUT : au moins un > 10 => True
```

---

## 📓 notes_perso.md (récapitulatif)

```markdown
# Leçon 2 – Opérateurs

## ✅ Acquis :
- Opérateurs arithmétiques : +, -, *, /, //, %, **
- Opérateurs de comparaison : ==, !=, >, <, >=, <=
- Opérateurs logiques : and, or, not
- Convention de commentaire :
  - # 🔹 TYPE
  - # 🔸 BUT

## 📌 À retenir :
- Toujours bien commenter le type et le but de chaque ligne
- Utiliser des exemples simples pour s’entraîner
```

