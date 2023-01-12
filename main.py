import read
import charts
import country_filter
import poblacion_mundial


def run():
    # obtengo data, la cual viene desde el modulo read
    data = read.read_file('./database.csv')

    pais = input('Escriba el pais que quiera saber ==> ')

    resultado = country_filter.filter(data, pais)
    value, key = poblacion_mundial.poblacion_mundial(data)

    chart_poblacion_mundial = charts.generate_chart(key, value)
    # si encontro algo en resultado se ejcuta
    if len(resultado) > 0:
        keys, values = country_filter.value_key(resultado)
        chart = charts.generate_chart(keys, values)
    else:
        print('No hemos encontrado el pais deseado')


run()
