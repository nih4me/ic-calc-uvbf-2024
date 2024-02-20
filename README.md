### Calculatrice (Python)

![Etat](https://github.com/nih4me/ic-calc-uvbf-2024/actions/workflows/python-app.yml/badge.svg)

#### Préparation de l'environnement

- Installer Python & Git
- Creer un dossier pour votre projet
- Ouvrir un terminal et se positionner au niveau du dossier, puis y initialiser un depot Git.

```sh
sudo apt update && sudo apt install python3 git
mdkir calculatrice
cd calculatrice
git init .
```

#### Implémentation

Structure et création des fichiers du projets

├── README.md # Documentation
├── calculatrice.py # Le code notre programme
└── tests.py # Va contenir tous les tests

#### Addition

`calculatrice.py`

```python
class Calculatrice:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f'{self.nombre1} + {self.nombre2} = {resultat}')
        return resultat
```

```sh
git add calculatrice.py
git commit -m 'Implementation de `addition`'
```

`tests.py`

```python
import unittest
from calculatrice import Calculatrice

class TestCalculatrice(unittest.TestCase): # TestXXXX
    def test_addition(self):
        calc1 = Calculatrice(1, 2)
        self.assertEqual(calc1.addition(), 3)

        calc2 = Calculatrice(1.5, 2.5)
        self.assertTrue(calc2.addition() == 4)

if __name__ == '__main__':
    unittest.main()
```

```sh
git add test.py
git commit -m 'Ecriture de tests pour `addition`'
```

#### Division

`calculatrice.py`

```python
class Calculatrice:
    def __init__(self, nombre1, nombre2):
        ...

    def addition(self):
        ...

    def division(self):
        resultat = self.nombre1 / self.nombre2
        print(f'{self.nombre1} / {self.nombre2} = {resultat}')
        return resultat
```

```sh
git add calculatrice.py
git commit -m 'Implementation de `division`'
```

`tests.py`

```python
import unittest
from calculatrice import Calculatrice

class TestCalculatrice(unittest.TestCase): # TestXXXX
    def test_addition(self):
        ...

    def test_division(self):
        calc1 = Calculatrice(4, 2)
        self.assertEqual(calc1.division(), 2)

        calc2 = Calculatrice(10, 0)
        self.assertTrue(calc2.addition() == "Erreur")

if __name__ == '__main__':
    unittest.main()
```

```sh
git add test.py
git commit -m 'Ecriture de tests pour `division`'
```
