n1 = float(input("digite a primeira nota:"))
n2 = float(input("digite a segunda nota:"))
media = (n1 + n2)/2
print(f"sua media é {media}")
if media <=  9:
    print("aprovado")
elif media == 10:
    print("aprovado com distinção")
else: 
    print("reprovado")