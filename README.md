# Análisis de Pruebas - Librería del Centro

## Tablas de Particiones de Equivalencia (Reglas 1 y 2)

**Regla 1: El precio base debe ser mayor que cero**

| Partición | Tipo de Partición | Valor Representativo | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| P1 | Inválida | -5000 | Rechazado (Lanzar error/mensaje) |
| P2 | Inválida | 0 | Rechazado (Lanzar error/mensaje) |
| P3 | Válida | 15000 | Aceptado |

**Regla 2: El descuento debe estar entre 0% y 40%**

| Partición | Tipo de Partición | Valor Representativo | Resultado Esperado |
| :--- | :--- | :--- | :--- |
| P4 | Inválida | -10 | Rechazado |
| P5 | Válida | 20 | Aceptado |
| P6 | Inválida | 50 | Rechazado |

## Análisis de Valores Límite (Regla 2)

**Rango válido para el descuento: [0, 40]**

| Límite Evaluado | Valor de Prueba | Resultado Esperado | Justificación |
| :--- | :--- | :--- | :--- |
| Justo por debajo del mínimo | -1 (o -0.01) | Rechazado | Es un valor negativo, fuera del rango. |
| En el límite mínimo | 0 | Aceptado | El 0% es válido según la regla. |
| Justo por encima del mínimo | 1 (o 0.01) | Aceptado | Valor mínimo positivo válido dentro del rango. |
| Justo por debajo del máximo | 39 (o 39.99) | Aceptado | Valor cercano al máximo permitido. |
| En el límite máximo | 40 | Aceptado | Es el descuento máximo permitido. |
| Justo por encima del máximo | 41 (o 40.01) | Rechazado | Supera el tope del 40% establecido. |

## Análisis de la Regla 3

**Pregunta para el administrador:**
¿Cómo se deben manejar los redondeos de los decimales resultantes al aplicar el descuento porcentual y el cálculo del IVA (ej. redondear al entero más cercano, redondear hacia arriba)?

**Justificación:**
Las operaciones con porcentajes (tanto el descuento como el IVA del 19%) generalmente producen valores con decimales fraccionarios, y es crítico definir la regla de redondeo exacta para evitar discrepancias financieras y problemas en aserciones de pruebas.
