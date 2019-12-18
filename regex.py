import re

#Revisar si la cadena contiene nombre principal y apellido paterno

nombre = "John Davis Alvarez Martinez"

str = nombre

reg = re.findall("John|Alvarez", str)

print(reg)

if (reg):
  print(" Si, hay coincidecia en nombre y apellido ")
else:
  print("No hay coincidencias")


