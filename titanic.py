def main():
    titanic()

def titanic():
    # Hacer las probabilidades de vidas recuperadas del 
    # Titanic si hubiera llegado ayuda a las dos horas 
    # luego de reportarse el accidente.
    #Fuente: Wikipedia

    total_people = 2228 
    survivors = 711
    d_peapol = total_people - survivors
    per_d_people = round((d_peapol / total_people) * 100, 2)
    per_surv = round((survivors / total_people) * 100, 2)
    time_help_arrives = 8 # Fuente: https://www.cienciahistorica.com/ aprox 8 horas
    dead_per_hour = round(d_peapol / time_help_arrives)
    per_d_p = round(((dead_per_hour*2)/total_people)*100, 2)
    per_s_p = round(100 - per_d_p, 2)

    print('\n')
    print('-' * 60)
    print(f'En el titanic viajaban {total_people} personas')
    print(f'El porcentaje de personas fallecidas fue de: {per_d_people}%')
    print(f'El porcentaje de personas que sobrevieron fue de: {per_surv}%')
    print('*' * 60)
    print(f'Si la ayuda hubiera llegado a las 2 horas del accidente')
    print(f'El porcentaje de sobrevivientes hubiera sido de: {per_s_p}')
    print('-' * 60)
    print('\n')


if __name__ == '__main__':
    main()
    