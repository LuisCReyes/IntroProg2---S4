salario_actual = float(input("Ingrese su salario actual: "))
incremento = salario_actual * 0.08
salario_incre = salario_actual + incremento
descuento = salario_incre * 0.025

salario_final = salario_incre - descuento

print(f"El salario actual que tiene es de: ${salario_incre}, el salario que tendrá con el incremento más el descuento del 25% será de: ${salario_final: .2f}")