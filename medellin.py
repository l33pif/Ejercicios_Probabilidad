import numpy as np
import matplotlib.pyplot as plt

def main():
    medellin_covid()

def medellin_covid():
    # Hacer una predicción de las probabilidades 
    # que tienen los hombres de la cuidad de Medellin 
    # en ser contagiados de COVID19
    #Fuente de los datos: https://www.medellin.gov.co/

    #Nuevos casos por mil hab por semana
    y = np.array([0.13, 0.19, 0.38, 0.59, 1, 1.23, 1.5, 1.39, 1.04, 1.10, 0.88])
    x = np.array(range(1, 12))
    plt.scatter(x, y)

    x = np.array([np.ones(11), x]).T
    B = np.linalg.inv (x.T @ x)@ x.T @ y

    plt.plot([1, 11], [ B[0]+B[1]*1, B[0]+B[1]*11 ], c="red")
    plt.show()

    poblacion_female = 1596844
    poblacion_male = 1336250
    poblacion_total = poblacion_female + poblacion_male
    total_active_cases_male = 1239
    total_active_cases_female = 1428
    total_active_cases = total_active_cases_female + total_active_cases_male
    per_male = round((total_active_cases_male / total_active_cases)*100, 2)
    per_female = round((total_active_cases_female / total_active_cases)*100, 2)
    per_prob_male = round((total_active_cases/poblacion_male)*100, 2)

    print('\n')
    print('-' * 60)
    print(f'La poblacion de Medellin, Colombia es de {poblacion_total} personas')
    print(f'{poblacion_female} Mujeres y {poblacion_male} Hombres')
    print(f'El numero de casos activos de Covid19 es de: {total_active_cases}')
    print(f'{per_male}% hombres y {per_female}% mujeress')
    print('*' * 60)
    print(f'La probabilidad de que los hombres se contagien con Covid19 es de {per_prob_male}%')
    print('-' * 60)
    print('\n')


if __name__ == '__main__':
    main()
    