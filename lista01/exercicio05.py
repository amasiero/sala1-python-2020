import math

raio = float(input("Informe o raio do circulo: "))
area = math.pi * (raio**2)
area_arredondada = round(area, 2)
print(f"A area do circulo eh {area_arredondada}")