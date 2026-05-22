import pytest
from src.producto import Producto

def test_crear_producto_precio_valido():
    producto = Producto("Lápiz", 5000)
    assert producto.nombre == "Lápiz"
    assert producto.precio_base == 5000

def test_crear_producto_precio_cero():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto("Borrador", 0)

def test_crear_producto_precio_negativo():
    with pytest.raises(ValueError, match="El precio base debe ser mayor que cero"):
        Producto("Cuaderno", -1500)
