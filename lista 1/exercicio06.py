print("para matutino escreva (M)")
print("para vespertino escreva (V)")
print("para noturno escreva (N")
turno = input("qual turno você estuda?")
if turno == "M":
    print("Bom dia")
elif turno == "V":
    print("Boa tarde")
elif turno == "N":
    print("Boa noite")
else:
    print ("Turno invalido!")
