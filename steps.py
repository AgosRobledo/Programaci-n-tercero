import pytest
import sys
sys.path.append("C:/Users/Usuario/Documents/2do/Programación/PYTHON/Carrito2024")
from tiendaonline2024 import productos, carrito, agregar_al_carrito, ver_carrito, validar_opcion, buscarProducto
from unittest import mock


def test_buscar_producto_existente(capfd):
    # Busca un producto que existe
    buscarProducto('001', productos)
    
    # Captura la salida de la función
    out, err = capfd.readouterr()
    
    assert "Producto encontrado:" in out
    assert "Iphone 13 mini" in out

def test_buscar_producto_no_existente(capfd):
    # Busca un producto que no existe
    buscarProducto('999', productos)
    
    # Captura la salida de la función
    out, err = capfd.readouterr()

    assert "El producto que desea buscar no existe" in out


