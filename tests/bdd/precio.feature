Feature: Cálculo del precio de productos
  As an administrator of "Librería del Centro"
  I want to apply discounts and calculate final prices of products
  So that I can sell products with the correct final price and taxes applied

  Background:
    Given I have a product named "Libro" with base price 10000

  @descuento @valido
  Scenario Outline: Aplicar descuentos válidos
    When I apply a discount of <discount_percent> percent
    Then the product discount should be <discount_percent> percent

    Examples:
      | discount_percent |
      | 0                |
      | 20               |
      | 40               |

  @descuento @error
  Scenario: Aplicar un descuento mayor al máximo permitido
    When I apply a discount of 45 percent
    Then the system should reject the discount with an error message

  @precio_final @valido
  Scenario Outline: Calcular el precio final con IVA y descuento
    When I apply a discount of <discount_percent> percent
    And I calculate the final price
    Then the final price should be <expected_final_price>

    Examples:
      | discount_percent | expected_final_price |
      | 0                | 11900.0              |
      | 20               | 9520.0               |
      | 40               | 7140.0               |
