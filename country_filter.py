def value_key(dictionary):
    keys = dictionary.keys()
    values = dictionary.values()

    listOfKeys = []
    listOfPopulation = []

    for i in values:
        listOfPopulation.append(i)

    for i in keys:
        listOfKeys.append(i)

    listOfPopulation.pop()
    listOfKeys.pop()
    listOfPopulation = list(map(int, listOfPopulation))

    return listOfKeys, listOfPopulation


def filter(data, pais):
    population = {}
    for d in data:
        if d["Country/Territory"] == pais:
            for key, value in d.items():
                if 'Population' in key:
                    population[key] = value
            break

    return population


if __name__ == '__main__':
    data = filter()
    print(data)
