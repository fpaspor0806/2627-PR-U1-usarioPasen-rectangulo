def calcular_medidas(base: float, altura: float) -> tuple[float, float]:
    """
    :param base:Se introduce para comparar
    :param altura:Se introduce para comparar
    :return:Devuelve el perimetro y el area

    """

    """
    :param base:Se introduce para comparar
    :param altura:Se introduce para comparar
    :return:Devuelve el perimetro y el area

    """

    perimetro:float = (base * 2) + (altura * 2)
    area:float = base * altura
    return area, perimetro

def determinar_forma(base: float, altura: float) -> str:
<<<<<<< HEAD
    """
=======
     """
>>>>>>> 99bd9a5321e8ad9c25467698500499ba381c64bf
    :param base:Se introduce para comparar la forma
    :param base:Se introduce para comparar la forma
    :param return:Devuelve la forma del cuadrado

    """
    
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
