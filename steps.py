import pytest
import sys
sys.path.append("C:/Users/Usuario/Documents/2do/Programación/PYTHON/Carrito2024")
from tiendaonline2024 import productos, buscarProducto



def test_buscar_producto_existente(capfd):

    buscarProducto('001', productos)
    out, err = capfd.readouterr()
    assert "Producto encontrado:" in out
    assert "Iphone 13 mini" in out


def test_buscar_producto_no_existente(capfd):
    buscarProducto ('999', productos)
    out, err = capfd.readouterr()
    assert "El producto que desea buscar no existe" in out
