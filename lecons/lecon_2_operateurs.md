# 🧠 Leçon 2 – Les Opérateurs en Python

---

## 📘 Introduction
Les opérateurs permettent de manipuler des variables et des valeurs. En Python, on en trouve plusieurs types : arithmétiques, de comparaison, logiques, etc. Ils sont indispensables pour construire des expressions et prendre des décisions.

---

## ➕ Les opérateurs arithmétiques

| Opérateur | Description        | Exemple (`a=10`, `b=3`) | Résultat |
|----------|--------------------|--------------------------|----------|
| `+`      | Addition            | `a + b`                  | `13`     |
| `-`      | Soustraction        | `a - b`                  | `7`      |
| `*`      | Multiplication      | `a * b`                  | `30`     |
| `/`      | Division            | `a / b`                  | `3.333`  |
| `//`     | Division entière    | `a // b`                 | `3`      |
| `%`      | Modulo (reste)      | `a % b`                  | `1`      |
| `**`     | Puissance           | `a ** b`                 | `1000`   |

---

## 🧭 Les opérateurs de comparaison

Ils retournent toujours un booléen (`True` ou `False`).

| Opérateur | Signification      | Exemple (`a=10`, `b=3`) | Résultat |
|----------|--------------------|--------------------------|----------|
| `==`     | Égal à              | `a == b`                 | `False`  |
| `!=`     | Différent de        | `a != b`                 | `True`   |
| `>`      | Supérieur à         | `a > b`                  | `True`   |
| `<`      | Inférieur à         | `a < b`                  | `False`  |
| `>=`     | Supérieur ou égal   | `a >= b`                 | `True`   |
| `<=`     | Inférieur ou égal   | `a <= b`                 | `False`  |

---

## 🧠 Les opérateurs logiques

Utilisés pour combiner plusieurs conditions :

| Opérateur | Signification         | Exemple                          | Résultat |
|----------|------------------------|----------------------------------|----------|
| `and`    | ET logique             | `(a > 5 and b < 5)`              | `True`   |
| `or`     | OU logique             | `(a < 5 or b < 5)`               | `True`   |
| `not`    | Négation logique       | `not(a > 5)`                     | `False`  |

---

## 🧪 Exemple de code commenté
```python
# 🔹 TYPE : Déclaration de variables
# 🔸 BUT : Initialiser des entiers pour tester les opérateurs
x = 10
y = 3

# 🔹 TYPE : Opérations arithmétiques
# 🔸 BUT : Démonstration de tous les opérateurs arithmétiques
print(x + y)     # ➕ Addition
print(x - y)     # ➖ Soustraction
print(x * y)     # ✖️ Multiplication
print(x / y)     # ➗ Division flottante
print(x // y)    # ➗ Division entière
print(x % y)     # 🔁 Modulo
print(x ** y)    # 🔼 Puissance

# 🔹 TYPE : Comparaison
# 🔸 BUT : Comparer deux entiers
print(x == y)    # Égalité
print(x != y)    # Différence
print(x > y)     # Supérieur
print(x < y)     # Inférieur

# 🔹 TYPE : Logique
# 🔸 BUT : Combiner des conditions
print(x > 5 and y < 5)  # Vrai
print(x < 5 or y < 5)   # Vrai
print(not x > 5)        # Faux
```

---

## 🧩 Exercice pratique

📝 **Énoncé :**
Crée un programme qui prend deux entiers `a` et `b` et affiche :
- Leur somme
- Si `a` est plus grand que `b`
- Si `a` est divisible par `b`
- Une condition logique combinée : `a > 10 and b < 5`

---

### ✅ Correction
```python
# 🔹 TYPE : Input utilisateur
# 🔸 BUT : Demander deux entiers à l’utilisateur
a = int(input("Entrez un entier a : "))
b = int(input("Entrez un entier b : "))

# 🔹 TYPE : Opérations de base
# 🔸 BUT : Appliquer les opérateurs étudiés
print("Somme :", a + b)
print("a > b ?", a > b)
print("a divisible par b ?", a % b == 0)
print("a > 10 and b < 5 ?", a > 10 and b < 5)
```

---

## 🧾 `notes_perso.md`

```
[LEÇON 2 – OPÉRATEURS]
- Arithmétiques : +, -, *, /, //, %, **
- Comparaison : ==, !=, >, <, >=, <=
- Logiques : and, or, not
- Bien comprendre que `==` teste l’égalité, pas l’affectation (`=`)
- Le modulo (`%`) est très utile pour savoir si un nombre est pair ou divisible
- Important : les opérateurs retournent des booléens ou des nombres selon le type
- Astuce : bien combiner les conditions pour éviter des `if` imbriqués trop complexes
```

---

📌 *Passe à la leçon 3 quand tu es à l’aise avec tous ces opérateurs !* 💪

