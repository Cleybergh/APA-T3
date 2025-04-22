# -*- coding: utf-8 -*-
"""vectores.ipynb

Archivo generado automáticamente desde Colab.

Documento original disponible en:
    https://colab.research.google.com/drive/1JmyTEjNhyvXcwmVtABPDF28ONRRtWQHV
"""

"""
algebra/vectores.py

Autor: David Bueno Cleybergh

Este archivo contiene la definición de la clase Vector, la cual permite efectuar diversas operaciones con vectores, entre ellas:

- Suma entre vectores
- Multiplicación por un escalar
- Producto de Hadamard (elemento a elemento)
- Producto escalar (dot product)
- Cálculo de las componentes tangencial y normal en relación con otro vector

>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> v1 * 2
Vector([2, 4, 6])
>>> v1 * v2
Vector([4.0, 10.0, 18.0])
>>> v1 @ v2
32
>>> v1 = Vector([2, 1, 2])
>>> v2 = Vector([0.5, 1, 0.5])
>>> v1 // v2
Vector([1.0, 2.0, 1.0])
>>> v1 % v2
Vector([1.0, -1.0, 1.0])
"""

import math

class Vector:
    def __init__(self, componentes):
        self.componentes = list(componentes)

    def __repr__(self):
        return f"Vector({self.componentes})"

    def __add__(self, other):
        return Vector([x + y for x, y in zip(self.componentes, other.componentes)])

    def __mul__(self, other):
        """
        Realiza el producto Hadamard (entre vectores) o la multiplicación por escalar (si se da un número).
        """
        if isinstance(other, (int, float)):
            return Vector([x * other for x in self.componentes])
        elif isinstance(other, Vector):
            return Vector([float(x * y) for x, y in zip(self.componentes, other.componentes)])
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Calcula el producto escalar entre dos vectores.
        """
        return sum(x * y for x, y in zip(self.componentes, other.componentes))

    def __floordiv__(self, other):
        escalar = (self @ other) / (other.norma() ** 2)
        return Vector([round(x * escalar, 6) for x in other.componentes])

    def __mod__(self, other):
        """
        Obtiene la componente normal (perpendicular) de este vector respecto a otro.

        Se calcula como: v1 % v2 = v1 - (v1 // v2)
        """
        return self - (self // other)

    def norma(self):
        """
        Retorna la longitud o magnitud del vector.
        """
        return math.sqrt(sum(x**2 for x in self.componentes))

    def __sub__(self, other):
        return Vector([round(x - y, 6) for x, y in zip(self.componentes, other.componentes)])


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
