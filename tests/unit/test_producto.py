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

def test_aplicar_descuento_valido():
    producto = Producto("Lápiz", 10000)
    producto.aplicar_descuento(25)
    assert producto.descuento == 25

def test_aplicar_descuento_limite_superior():
    producto = Producto("Borrador", 2000)
    producto.aplicar_descuento(40)
    assert producto.descuento == 40

def test_aplicar_descuento_superior_al_maximo():
    producto = Producto("Cuaderno", 3000)
    with pytest.raises(ValueError, match="El descuento debe estar entre 0% y 40%"):
        producto.aplicar_descuento(45)

def test_calcular_precio_final_con_descuento():
    producto = Producto("Libro", 10000)
    producto.aplicar_descuento(20)
    precio_final = producto.calcular_precio_final()
    assert precio_final == 9520.0

def test_calcular_precio_final_sin_descuento():
    producto = Producto("Revista", 5000)
    producto.aplicar_descuento(0)
    precio_final = producto.calcular_precio_final()
    assert precio_final == 5950.0
