import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.producto import Producto

# Esto carga todos los escenarios del archivo .feature
scenarios("precio.feature")

@pytest.fixture
def context():
    return {}

@given(parsers.parse('I have a product named "{nombre}" with base price {precio:d}'))
def given_product(context, nombre, precio):
    context['producto'] = Producto(nombre, precio)

@when(parsers.parse('I apply a discount of {descuento:d} percent'))
def when_apply_discount(context, descuento):
    producto = context['producto']
    try:
        producto.aplicar_descuento(descuento)
    except ValueError as e:
        context['error'] = e

@then(parsers.parse('the product discount should be {descuento:d} percent'))
def then_discount_should_be(context, descuento):
    assert context['producto'].descuento == descuento

@then('the system should reject the discount with an error message')
def then_reject_discount(context):
    assert 'error' in context
    assert str(context['error']) == "El descuento debe estar entre 0% y 40%"

@when('I calculate the final price')
def when_calculate_final_price(context):
    context['precio_final'] = context['producto'].calcular_precio_final()

@then(parsers.parse('the final price should be {precio:f}'))
def then_final_price(context, precio):
    assert context['precio_final'] == precio
