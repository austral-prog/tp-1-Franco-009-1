def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    segundoporhora= 3600
    horas_completa= total_segundos // segundoporhora
    print(horas_completa)
    minutos_completa = total_segundos % segundoporhora // 60
    print(minutos_completa)
    segundosrestantes = total_segundos % 60
    print(segundosrestantes)
time()

