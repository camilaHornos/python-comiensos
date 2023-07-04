#esto son los datos #promedio de duracion 
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
dalto_curso=1.5


#diferencia de duracion 

diferencia_con_min= 100 - dalto_curso / otros_cursos_min *100
diferencia_con_max= 100 - dalto_curso *1000 // otros_cursos_max /10 # es distinto y asi para tener solo una como y un numero despues del decimal y que no sea tan dificl para usar el numero despues 
diferencia_con_promedio= 100 - dalto_curso / otros_cursos_promedio *100
print("---------------------------------")
print("diferencia de porcentaje entre curso")
print(f"---el curso de dalto dura {diferencia_con_min}% que el mas rapido")
print(f"---el curso de dalto dura {diferencia_con_max}% que el mas lento")
print(f"---el curso de dalto dura {diferencia_con_promedio}% que el promedio")
print("-----------------------------------------")

# B porcentanje de material vacio borrado 
#Datos 
crudo_promedio= 5
crudo_dalto = 3.5

print("calculando el porsentaje curdo borrado")
print(f' --este curso elimino el {100-crudo_promedio *100//crudo_dalto /10} de timepo vacio')

print("----------------------------------------------------------")
print(f' dalto elimino un {100- crudo_dalto *100// dalto_curso/10}de crudo')
print("--------------------------------------------")

#c mostrar diferencias si los cursos duran 10 horas 

print(f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio*100//dalto_curso/10}horas de otro curso')