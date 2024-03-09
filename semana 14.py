def calcular_descuento(monto_compra, porcentaje_descuento=35):
    descuento = monto_compra * porcentaje_descuento / 100
    monto_final = monto_compra - descuento
    return descuento, monto_final

# llamada a la función proporcionando solo el monto de compra
descuento1, monto_final1 = calcular_descuento(200)
print("En la primera llamada:")
print("Descuento:", descuento1)
print("Monto final a pagar:", monto_final1)

# llamada a la función proporcionando el monto de compra y el porcentaje de descuento
descuento2, monto_final2 = calcular_descuento(200, 45)
print("En la segunda llamada:")
print("Descuento:", descuento2)
print("Monto final a pagar:", monto_final2)