import csv


def read_file(read):

    population = []

    # leo el archivo
    with open(read, mode='r') as file:
        # guardo en la variable el contenido del archivo utilizando el modulo csv
        database_reader = csv.reader(file, delimiter=',')

        # hago que itere sobre la primera linea del archivo, contiene las claves
        main_information = next(database_reader)
        # recorro la informacion del archivo
        for row in database_reader:
            # el zip lo utilizo para juntar dos listas, en este caso las claves (main_information) y valores (row)
            file_information = zip(main_information, row)

            # genero el diccionario con toda la info
            country_dic = {key: value for key, value in file_information}

            # lo coloco dentro de la lista
            population.append(country_dic)
    return population


if __name__ == '__main__':
    data = read_file('./database.csv')
    print(data)
