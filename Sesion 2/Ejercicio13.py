mujeres_aula = int(input("Ingrese el número de mujeres en el aula: "))
hombres_aula = int(input("Ingrese el número de hombres en el aula: "))

total_est = mujeres_aula + hombres_aula
porcentaje_mujeres_aula = (mujeres_aula / total_est) * 100
porcentaje_hombres_aula = (hombres_aula / total_est) * 100

print("-" * 100)
print(f"En el aula hay un total de {total_est} estudiantes, el {porcentaje_mujeres_aula}% son mujeres y el {porcentaje_hombres_aula}% son hombres.")
print("-" * 100)