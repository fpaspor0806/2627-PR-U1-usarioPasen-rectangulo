def calcular_medidas(base: float, altura: float) -> tuple[float, float]:

    perimetro:float = (base * 2) + (altura * 2)
    area:float = base * altura
    return area, perimetro

def determinar_forma(base: float, altura: float) -> str:
    if base == altura:
        return "cuadrado"

    if base > altura:
        return "Horizontal"
    else:
        return "Vertical"

def main():
    base = float(input("Introduce una base:"))
    altura = float(input("Introduce una altura:"))

    if base <= 0 or altura <= 0:
        print("Error, no se puede poner un valor menos o igual a 0")
    else:
        area = calcular_medidas(base, altura)[0]
        perimetro = calcular_medidas(base, altura)[1]
        forma = determinar_forma(base, altura)

        print(f"Forma:{forma}")
        print(f"Area:{area} cm²")
        print(f"Perimetro:{perimetro} cm")

if __name__ == "__main__":
    main()