import matplotlib.pyplot as chart


def generate_chart(labels, values):

    fig, ax = chart.subplots()

    ax.bar(labels, values)
    chart.show()


if __name__ == '__main__':
    data = generate_chart()
    print(data)
