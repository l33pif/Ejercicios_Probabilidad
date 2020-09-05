def main():
    gripe_or_covid()

def gripe_or_covid():
    # Predecir la probabilidad de contraer gripe en esta etapa de pandemia, 
    # pero que las persona la confundan con COVID19.
    # Fuente: https://espanol.cdc.gov/
    sintomas_covid = 11
    sintomas_gripe = 8
    sintomas_parecidos = 6

    prob_co = round((sintomas_parecidos / sintomas_gripe) * 100, 2)

    print('\n')
    print('-' * 60)
    print(f'El covid tiene {sintomas_covid} sintomas y la gripe tiene {sintomas_gripe}')
    print(f'El covid y la gripe son parecidos en {sintomas_parecidos} sintomas')
    print(f'La probabilidad de que la gente confunda la enfermedad es de {prob_co}%')
    print('-' * 60)
    print('\n')


if __name__ == '__main__':
    main()
    