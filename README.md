Análisis de Pruebas - Librería del Centro

Tablas de Particiones de Equivalencia (Reglas 1 y 2)

Regla 1: El precio base debe ser mayor que cero

| Partición | Tipo de Partición  | Valor Representativo | Resultado Esperado |
| P1        | Inválida | -5000   | Rechazado (Lanzar error/mensaje) |
| P2        | Inválida | 0       | Rechazado (Lanzar error/mensaje) |
| P3        | Válida   | 15000   | Aceptado |

Regla 2: El descuento debe estar entre 0% y 40%

| Partición | Tipo de Partición  | Valor Representativo | Resultado Esperado |
| P4        | Inválida           | -10                  | Rechazado |
| P5        | Válida             | 20                   | Aceptado |
| P6        | Inválida           | 50                   | Rechazado |


Análisis de Valores Límite (Regla 2)

Rango válido para el descuento: [0, 40]

| Límite Evaluado             | Valor de Prueba | Resultado Esperado | Justificación 
| Justo por debajo del mínimo |-1 (o -0.01)     | Rechazado          | Es un valor negativo, fuera del rango. 
| En el límite mínimo         | 0               | Aceptado           | El 0% es válido según la regla. 
| Justo por encima del mínimo | 1 (o 0.01)      | Aceptado           | Valor mínimo positivo válido dentro del rango. 
| Justo por debajo del máximo | 39 (o 39.99)    | Aceptado           | Valor cercano al máximo permitido. 
| En el límite máximo         | 40              | Aceptado           | Es el descuento máximo permitido. 
| Justo por encima del máximo | 41 (o 40.01)    | Rechazado          | Supera el tope del 40% establecido. 


Análisis de la Regla 3

Preguntas que aria al administrador:
¿Cómo se deben manejar los redondeos de los decimales resultantes al aplicar el descuento porcentual y el cálculo del IVA?

Las operaciones con porcentajes (tanto el descuento como el IVA del 19%) generalmente producen valores con decimales fraccionarios, y es crítico definir la regla de redondeo exacta para evitar discrepancias financieras y problemas en aserciones de pruebas.

## Casos de Prueba

| ID | Regla | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| TC1 | Regla 1 | Crear producto con precio base válido (>0) | Ninguna | Nombre: "Lápiz", Precio base: 5000 | 1. Instanciar el producto con los datos | Producto creado exitosamente con precio base 5000 | Positivo |
| TC2 | Regla 1 | Crear producto con precio base cero | Ninguna | Nombre: "Borrador", Precio base: 0 | 1. Intentar instanciar el producto | Sistema rechaza la creación con mensaje de error | Borde |
| TC3 | Regla 1 | Crear producto con precio base negativo | Ninguna | Nombre: "Cuaderno", Precio base: -1500 | 1. Intentar instanciar el producto | Sistema rechaza la creación con mensaje de error | Negativo |
| TC4 | Regla 2 | Aplicar un descuento válido intermedio | Producto creado con precio base 10000 | Descuento: 25% | 1. Aplicar el descuento al producto | Descuento del 25% asignado exitosamente | Positivo |
| TC5 | Regla 2 | Aplicar descuento en el límite superior | Producto creado con precio base 2000 | Descuento: 40% | 1. Aplicar el descuento al producto | Descuento del 40% asignado exitosamente | Borde |
| TC6 | Regla 2 | Aplicar descuento superior al máximo permitido | Producto creado con precio base 3000 | Descuento: 45% | 1. Intentar aplicar el descuento al producto | Sistema rechaza el descuento con mensaje de error | Negativo |
| TC7 | Regla 3 | Calcular precio final con descuento y sin resultado negativo | Producto con precio base 10000 y descuento 20% | Ninguna | 1. Calcular precio final del producto | Retorna 9520 (10000 - 2000 = 8000; + 19% = 9520) | Positivo |
| TC8 | Regla 3 | Calcular precio final sin descuento (0%) | Producto con precio base 5000 y descuento 0% | Ninguna | 1. Calcular precio final del producto | Retorna 5950 (5000 - 0 = 5000; + 19% = 5950) | Positivo |

## Reporte de Cobertura

```text
=============================== tests coverage ================================
_______________ coverage: platform win32, python 3.14.0-final-0 _______________

Name              Stmts   Miss  Cover
-------------------------------------
src\__init__.py       0      0   100%
src\producto.py      15      0   100%
-------------------------------------
TOTAL                15      0   100%
============================== 8 passed in 0.10s ==============================
```
