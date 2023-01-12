import read
import charts
import country_filter


def run():
    # obtengo data, la cual viene desde el modulo read
    data = read.read_file('./database.csv')

    pais = input('Escriba el pais que quiera saber ==> ')

    resultado = country_filter.filter(data, pais)

    # si encontro algo en resultado se ejcuta
    if len(resultado) > 0:
        keys, values = country_filter.value_key(resultado)
        chart = charts.generate_chart(keys, values)
    else:
        print('No hemos encontrado el pais deseado')


run()
