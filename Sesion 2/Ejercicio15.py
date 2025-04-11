nombre_producto = input("Porfavor ingrese el nombre del producto: ")
precio_producto = float(input("Porfavor ingrese el precio del producto: "))
ingresar_descuento = float(input("Ingrese el descuento a aplicar: "))

ingresar_descuento /= 100
descuento = precio_producto * ingresar_descuento 
precio_final = precio_producto - descuento

print(f"Su descuento del producto será: {precio_final: .2f}")
