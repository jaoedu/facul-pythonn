password = "Muleta"
i = 0
while i < 4:
    password = input("Digite a senha")
    i+= 1
    if password == "Muleta":
        print ("Acesso permitido!")
        break 
    elif i == 3:
        print("Resta mais uma chance")
    elif i == 4:
        print("ACESSO NEGADO.")
    else:
        print("Senha incorreta")