def poblacion_mundial(data):
    percentages_dict = {item["Country/Territory"]: item["World Population Percentage"] for item in data}

    names = percentages_dict.keys()
    per = percentages_dict.values()

    return names, per
