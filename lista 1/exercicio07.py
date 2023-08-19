i = 0
p1 = (input("TELEFONOU PARA A VITIMA?"))
if p1 == 'sim':
    i += 1
p2 = (input("ESTEVE NO LOCAL DO CRIME?"))
if p2 == 'sim':
    i += 1
p3 = (input("MORAVA PERTO DA VITIMA?"))
if p3 == 'sim':
    i += 1
p4 = (input("DEVIA PARA A VITIMA?"))
if p4 == 'sim':
    i += 1
p5 = (input("TRABALHAVA COM A VITIMA?"))
if p5 == 'sim':
    i += 1
if i == 0 or i == 1:
    print("Inocente")
if i == 2:
    print("Suspeito")
if i  == 3 or i == 4:
    print("Cumplice")
if i == 5:
    print("Assasino")