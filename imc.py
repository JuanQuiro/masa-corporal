def imc(estatura, peso):
    return peso / estatura**2
    


peso = float(input('Escriba su peso '))
estatura = float(input('Escriba su estatura '))

masa= imc(estatura, peso);
masa = round(masa, 2)

print("Su masa corporal es {}".format(masa))
