class Producto:
    """Clase que representa un producto de la librería."""
    
    def __init__(self, nombre: str, precio_base: float) -> None:
        if precio_base <= 0:
            raise ValueError("El precio base debe ser mayor que cero")
        self.nombre = nombre
        self.precio_base = precio_base
        self.descuento = 0.0
        
    def aplicar_descuento(self, porcentaje: float) -> None:
        """
        Aplica un descuento porcentual al precio base del producto.
        El porcentaje debe estar entre 0 y 40 inclusive.
        """
        if not (0 <= porcentaje <= 40):
            raise ValueError("El descuento debe estar entre 0% y 40%")
        self.descuento = porcentaje

    def calcular_precio_final(self) -> float:
        precio_con_descuento = self.precio_base * (1 - self.descuento / 100)
        precio_final = precio_con_descuento * 1.19
        return max(0.0, precio_final)
